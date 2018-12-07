extern printf
extern scanf

section .data
	; Scanf/printf stuff
	readcoords: db "%d, %d", 0
	printint: db "%lld", 10, 0
	answer: dq 0

	; Input data
	x: dd 0
	y: dd 0

	; Grid
	; 4 bytes current sum for the square
	grid: times 1000*1000*(4) db 0

section .text
	global main

; Count the entires with total sum less than rsi
count_less:
	push	rbp
	mov	rbp, rsp
	push	rbx
	push	rcx
	push	rdx
	
	mov	rax, 0
	mov	rcx, 1000*1000
	lea	rbx, [grid]
	counting_loop:
		mov	edx, DWORD [rbx]
		cmp	rdx, rsi
		jge	skip
		inc	rax
		skip:
	add	rbx, 4
	loop counting_loop

	pop	rdx
	pop	rcx
	pop	rbx
	mov	rsp, rbp
	pop	rbp
	ret

; Calculate distance between r8 and r9, returns val in ebx
dist:
	push	rbp
	mov	rbp, rsp

		mov	r10, r8
		mov	rbx, r9
		cmp	r10, rbx
		jg	is_greater
		sub	rbx, r10
		jmp	done_dist

		is_greater:
		sub	r10, rbx
		mov	rbx, r10
	
	done_dist:
	mov	rsp, rbp
	pop	rbp
	ret

; Fills the grid from [x] and [y]
fill_grid:
	push	rax
	push	r10
	push	rbx
	push	rcx
	push	rdx
	push	rbp
	mov	rbp, rsp


	mov	rdi, 0 ; y
	outer_loop:
		mov	rsi, 0 ; x
		inner_loop:
			; calculate index into grid (into rax)
			push	rdx
			mov	eax, edi
			mov	r10, 1000
			mul	r10
			add	eax, esi
			mov	r10, 4
			mul	r10
			lea	ebx, [grid]
			add	eax, ebx
			pop	rdx

			; Calculate manhattan distance (into rcx)
			mov	r8, 0
			mov	r9, 0
			mov	r8d, DWORD [x]
			mov	r9d, esi
			call	dist
			mov	rcx, rbx
			mov	r8d, DWORD [y]
			mov	r9d, edi
			call	dist
			add	rcx, rbx

			; Add the sum to the square
			mov	rbx, 0
			mov	ebx, DWORD [rax]
			add	ebx, ecx
			mov	DWORD [rax], ebx


		continue:
		inc	rsi
		cmp	rsi, 1000
		jl	inner_loop

	inc	rdi
	cmp	rdi, 1000
	jl	outer_loop


	end_fill_grid:
	mov	rsp, rbp
	pop	rbp
	pop	rdx
	pop	rcx
	pop	rbx
	pop	r10
	pop	rax
	ret

main:
	; reserve things on stack
	push	rbp
	mov	rbp, rsp

	reading_loop:
	; Read coordinates
	mov	rdi, readcoords
	lea	rsi, [x]
	lea	rdx, [y]
	mov	rax, 0
	call	scanf

	; If we did not manage to read digits, exit
	cmp	rax, 2
	jne	end_reading_loop

	; Fill the grid
	mov	rsi, 0
	mov	rdi, 0
	mov	esi, DWORD [x]
	mov	edi, DWORD [y]
	call	fill_grid

	jmp reading_loop
	end_reading_loop:

	; Count less thans
	mov	rsi, 10000
	call	count_less

	; Write the answer
	mov	rdi, printint
	mov	esi, eax
	mov	rax, 0
	call	printf

	; Exit
	mov	rsp, rbp
	pop	rbp
	ret
