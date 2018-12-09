extern printf
extern scanf

section .data
	; Scanf/printf stuff
	readcoords: db "%d, %d", 0
	printint: db "%lld", 10, 0
	printchar: db "%c", 0
	scanformat: db "Step %c must be finished before step %c can begin.", 10, 0
	answer: dq 0

	; Input data
	ch1: db 0
	ch2: db 0

	; Dependencies
	; Every node has a list of the stuff it depends on
	; For each entry: 1 byte for "printed" (0) and "unprinted" (1)
	; For each entry: 26 bytes for "depends on" (1) and "does not depend on" (0)
	deps: times 26*27 db 0

	; Workers
	; One byte for how many more seconds until the worker is available again (0 = worker is available)
	num_workers: equ 5
	workers: times num_workers db 0
	working_on: times num_workers db 255 ; which work the worker is currently doing
	time_constant: equ 61 ; A=0

section .text
	global main


; Add dependency "x depends on y", x in rsi, y in rdi
add_deps:
	push	rbp
	mov	rbp, rsp
	push	rax

	; mark x as "unprinted"
	mov	rax, rsi
	sub	rax, 65
	mov	r8, 27
	mul	r8
	lea	rax, [deps+rax]
	mov	BYTE [rax], 1

	; mark dependency
	sub	rdi, 64
	add	rax, rdi
	mov	BYTE [rax], 1

	; mark y as "unprinted"
	dec	rdi
	mov	r8, 27
	mov	rax, rdi
	mul	r8
	lea	rax, [deps+rax]
	mov	BYTE [rax], 1

	pop	rax
	mov	rsp, rbp
	pop	rbp
	ret

; Check if the character which rsi points to is allowed to be printed
; rax=1 if allowed to be printed, rax=0 otherwise
check_dependencies:
	push	rbp
	mov	rbp, rsp
	push	rcx
	push	rbx
	push	r8

	mov	r8, 1 ; return value

	inc	rsi
	mov	rcx, 0
	dep_check_loop:
		movzx	rbx, BYTE [rsi]
		cmp	rbx, 0
		je	no_dep

		; If we have a dependency, check if we've already printed it
		mov	rax, rcx
		mov	r9, 27
		mul	r9
		lea	rbx, [deps+rax]
		movzx	rbx, BYTE [rbx]
		cmp	rbx, 0
		je	no_dep
		mov	r8, 0
		jmp	done_checking

		no_dep:
	inc	rsi
	inc	rcx
	cmp	rcx, 26
	jne	dep_check_loop

	done_checking:
	mov	rax, r8
	pop	r8
	pop	rbx
	pop	rcx
	mov	rsp, rbp
	pop	rbp
	ret

; gets work for one of the workers, returns how many seconds the work will take
; returns 0 (rax) if no work is available
get_work:
	push	rbp
	mov	rbp, rsp
	push	rbx
	push	rcx
	push	r9
	push	r10
	push	r13

	mov	r8, 0

	; Loop through all the characters
	lea	rbx, [deps]
	mov	rcx, 0
	find_char_loop:
		; Is it a zero? Skip it.
		movzx	rdx, BYTE [rbx]
		cmp	rdx, 0
		je	skip

		; Not a zero? Check if dependencies has been printed.
		mov	rsi, rbx
		call	check_dependencies

		; If we are allowed to print character, print it
		cmp	rax, 0
		je	skip

		; Check if the work is in the taken list
		push	rbx
		lea	rbx, [working_on]
		mov	r15, 0
		wloop:
			movzx	r10, BYTE [rbx]
			cmp	r10, rcx
			jne	wloop_skip
			; oops, work was already taken...
			pop	rbx
			jmp	skip

		wloop_skip:
		inc	r15
		inc	rbx
		cmp	r15, num_workers ; number of workers
		jne	wloop
		
		pop	rbx

		; If not, mark work as taken
		mov	r8, rcx
		add	r8, time_constant

		jmp	done_printing

	skip:
	add	rbx, 27
	inc	rcx
	cmp	rcx, 26
	jne	find_char_loop

	done_printing:
	mov	rax, r8
	pop	r13
	pop	r10
	pop	r9
	pop	rcx
	pop	rbx
	mov	rsp, rbp
	pop	rbp
	ret

; Step one second
; Returns 1 if something happened, 0 otherwise
tic:
	push	rbp
	mov	rbp, rsp

	push	rbx
	push	rcx
	push	r8
	push	r9
	push	r10

	mov	r10, 0

	; dec time for all workers
	lea	r9, [workers]
	lea	r13, [working_on]
	mov	rcx, 0
	dec_worker_loop:
		movzx	r8, BYTE [r9]
		cmp	r8, 0
		je	next_worker_1
		dec	BYTE [r9]
		mov	r10, 1

		; If we just finished work, mark it as done
		cmp	BYTE [r9], 0
		jne	next_worker_1

		mov	r8, 0
		movzx	r8, BYTE [r13]
		mov	rax, r8
		mov	r8, 27
		mul	r8
		lea	rbx, [deps+rax]
		mov	BYTE [rbx], 0

		mov	BYTE [r13], 255
	
	next_worker_1:
	inc	rcx
	inc	r9
	inc	r13
	cmp	rcx, num_workers	; number of workers
	jne	dec_worker_loop


	; Loop over all the workers to see if there is anyone available
	lea	r9, [workers]
	lea	r13, [working_on]
	mov	rcx, 0
	find_worker_loop:
		movzx	r8, BYTE [r9]
		cmp	r8, 0
		jne	next_worker

		; Found a worker!
		call	get_work
		cmp	rax, 0
		je	find_worker_loop_end ; no work for the poor guy
		mov	BYTE [r9], al
		sub	rax, time_constant
		mov	BYTE [r13], al
		mov	r10, 1
	
	next_worker:
	inc	rcx
	inc	r9
	inc	r13
	cmp	rcx, num_workers	; number of workers
	jne	find_worker_loop

	find_worker_loop_end:

	mov	rax, r10

	pop	r10
	pop	r9
	pop	r8
	pop	rcx
	pop	rbx
	mov	rsp, rbp
	pop	rbp
	ret

; main function
main:
	; reserve things on stack
	push	rbp
	mov	rbp, rsp

	reading_loop:
	; Read the two characters
	mov	rdi, scanformat
	lea	rsi, [ch1]
	lea	rdx, [ch2]
	mov	rax, 0
	call	scanf

	; If we did not manage to read characters, exit
	cmp	rax, 2
	jne	end_reading_loop

	; Add dependency
	movzx	rdi, BYTE [ch1]
	movzx	rsi, BYTE [ch2]
	call	add_deps


	jmp reading_loop
	end_reading_loop:

	; Print characters in order
	mov	r14, 0
	working_loop:
		inc	r14
		call	tic
		cmp	rax, 1
		je	working_loop

	; Write new line
	mov	rdi, printint
	mov	rsi, r14
	sub	rsi, 2
	mov	rax, 0
	call	printf

	; Exit
	mov	rax, 0
	mov	rsp, rbp
	pop	rbp
	ret
