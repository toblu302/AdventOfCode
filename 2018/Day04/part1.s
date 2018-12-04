extern printf
extern scanf

section .data
	; scanf/printf helpers
	printint: db "%d", 10, 0
	printstr: db "%s", 10, 0
	readstr: db "%s%*c", 0
	skipformat: db "%[^", 10, "]%*c", 0
	scanformat: db "%*c%ld-%ld-%ld %ld:%ld]", 0

	; Input data
	year: dq 0
	month: dq 0
	day: dq 0
	hour: dq 0
	minute: dq 0
	str1: times 16 db 0
	str2: times 16 db 0
	garbage: times 64 db 0

	; Sorted list of events
	; Each event is 16 bytes long
	; First 8 bytes are the number to sort on (date)
	; Second 8 bytes are the event "#id", "up", "asleep"
	events: times 1500*(8+8) db 0
	num_sorted: dq 0

	; Guards
	; 8 bytes id
	; 4 bytes total time slept
	; 60 bytes markers for which minutes the guard sleeps
	sleep_schedule: times 1000*(8+4+60) db 0

	; Variables used when parsing
	current_id: dq 0
	fell_asleep_time: db 0
	currently_awake: db 1
	
	best_id: dq 0
	best_total_time: dq 0
	best_time_marker: db 0

section .text
	global main

main:
	; reserve things on stack
	push	rbp
	mov	rbp, rsp

	loop:
	mov	QWORD [str2], 0
	; Read all the data
	mov	rdi, scanformat
	lea	rsi, [year]
	lea	rdx, [month]
	lea	rcx, [day]
	lea	r8, [hour]
	lea	r9, [minute]
	mov	rax, 0
	call	scanf

	; If we did not manage to read data, exit
	cmp	rax, 5
	jne	end

	; Read rest of data
	mov	rdi, readstr
	lea	rsi, [str1]
	mov	rax, 0
	call	scanf

	mov	rdi, readstr
	lea	rsi, [str2]
	mov	rax, 0
	call	scanf
	
	; If we have a '#', then we have some garbage to clean up
	mov	al, 35
	mov	bl, BYTE [str2]
	cmp	al, bl
	jne	no_garbage

	mov	rdi, skipformat
	lea	rsi, [garbage]
	mov	rax, 0
	call	scanf
	no_garbage:
	; Finished reading data

	; Convert input to a good integer (which can be sorted on!)
	mov	r8, 256
	mov	rax, QWORD [month]
	mul	r8
	add	rax, QWORD [day]
	mul	r8
	add	rax, QWORD [hour]
	mul	r8
	add	rax, QWORD [minute]
	mov	r11, rax ; r11 now contains date as integer
	mov	r12, QWORD [str2]

	; Step through the list of sorted stuff
	mov	r8, 16
	mov	rax, QWORD [num_sorted]
	mul	r8
	lea	rcx, [events]
	add	rax, rcx
	sorting_loop:
		; Are we at the beginnging? End.
		cmp	rax, events
		je 	sorting_loop_end

		; Copy the string
		mov	rbx, QWORD [rax-8]  ; rbx: entry at i-1
		mov	[rax+8], rbx

		; Copy the value
		mov	rbx, QWORD [rax-16]  ; rbx: entry at i-1
		mov	[rax], rbx
		

		; Are we at the insertion point?
		cmp	r11, rbx
		jg	sorting_loop_end
		
		sub	rax, 16
	jmp	sorting_loop
	sorting_loop_end:
	; Insert the value at the current index
	mov	QWORD [rax], r11
	mov	QWORD [rax+8], r12
	inc	QWORD [num_sorted]

	jmp loop

	end:

	; Now we have a sorted list of events, so we need to parse it
	lea	rax, [events]
	mov	rbx, 0
	parse:
		movzx	r8, BYTE [rax]	; r8 = minute marker
		movzx	r9, BYTE [rax+8] ;r9 = first char of string

		; Is is guard change?
		cmp	r9, 35
		jne	switch_awake
			; Guard change
			push	rax
			push	rbx

			mov	r10, rax
			add	r10, 9
			mov	rax, 0 ; result
			mov	r12, 10
			parse_num_loop:
				movzx	rbx, BYTE [r10]
				cmp	rbx, 0
				je	finished_number
				sub	rbx, 0x30
				mul	r12
				add	rax, rbx
				inc	r10
				jmp	parse_num_loop

			finished_number:
			mov	BYTE [currently_awake], 1
			mov	QWORD [current_id], rax
			
			pop	rbx
			pop	rax
		jmp done
		switch_awake:
			xor	BYTE [currently_awake], 1
			cmp	BYTE [currently_awake], 1
			jne	fell_asleep
			woke_up:
				push	rax
				push	rbx
				push	rcx
				push	r8

				lea	rax, [sleep_schedule]
				mov	rbx, QWORD [current_id]
				; find the guard with correct id
				guard_finding_loop:
				
				cmp	QWORD [rax], rbx
				je	guard_found
				cmp	QWORD [rax], 0
				je	guard_found

				add	rax, 8+4+60
				jmp guard_finding_loop
				guard_found: ; rax points to correct guard (rax+12 schedule)
				mov	QWORD [rax], rbx	; store the id here

				mov	rbx, rax
				add	rbx, 12
				movzx	rax, BYTE [fell_asleep_time]
				add	rbx, rax
				mov	rcx, r8
				movzx	rax, BYTE [fell_asleep_time]
				sub	rcx, rax
				marking_loop:
				inc	BYTE [rbx]
				inc	rbx
				loop marking_loop
				
				pop	r8
				pop	rcx
				pop	rbx
				pop	rax

			fell_asleep:
				push	rax
				mov	rax, r8
				mov	BYTE [fell_asleep_time], al
				pop	rax
		done:
		add 	rax, 16
		inc rbx
	cmp	rbx, QWORD [num_sorted]
	jne	parse

	; Now we have array of how all the guards sleep!
	lea	rbx, [sleep_schedule]
	find_best_loop:
		mov	r8, 0	; sum
		mov	r10, 0	; best time marker time
		mov	r11, 0	; best time marker index
		mov	r9, rbx	; current pointer
		add	r9, 12
		mov	rcx, 60
		inner_loop:
			movzx	rdx, BYTE [r9]
			add	r8, rdx
			inc	r9
			cmp	rdx, r10
			jl	not_better_time_marker
				mov	r10, rdx
				mov	r11, 60
				sub	r11, rcx
			not_better_time_marker:
		loop inner_loop
		; r8 is now the total sum
		cmp	r8, QWORD [best_total_time]
		jl	not_better
			mov	QWORD [best_total_time], r8
			mov	QWORD [best_time_marker], r11
			mov	r11, QWORD [rbx]
			mov	QWORD [best_id], r11
			
		not_better:
	
	add	rbx, 8+4+60
	cmp	QWORD [rbx], 0
	jne	find_best_loop

	; Write the answer
	mov	rdi, printint
	mov	rsi, QWORD [best_id]
	movzx	rax, BYTE [best_time_marker]
	mul	rsi
	mov	rsi, rax
	mov	rax, 0
	call	printf

	; Exit
	mov	rsp, rbp
	pop	rbp
	mov	rax, 60 ; exit
	mov	rbx, 0
	syscall   ; exit(0)

