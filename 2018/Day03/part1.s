extern printf
extern scanf

section .data
	printint: db "%d", 10, 0
	scanformat: db 35, "%ld @ %ld,%ld: %ldx%ld%*c", 0
	id: dq 0
	offx: dq 0
	offy: dq 0
	x: dq 0
	y: dq 0
	side: dq 1100
	grid: times 1100*1100 dq 0
	answer: dq 0

section .text
	global main

main:
	push	rbp
	mov	rbp, rsp

	loop:
	; Read a line
	mov	rdi, scanformat
	lea	rsi, [id]
	lea	rdx, [offx]
	lea	rcx, [offy]
	lea	r8, [x]
	lea	r9, [y]
	mov	rax, 0
	call	scanf

	; If we did not manage to read a line, exit
	cmp	rax, 5
	jne	end

	; Loop through the defined grid
	; increment each element by 1
	; rbx: y
	; rcx: x
	mov	rbx, [y]
	outer_loop:
		dec	rbx
		mov	rcx, [x]
		inner_loop:
			dec	rcx
			; rax = (offy+rbx)*side + (offx+rcx) is the index
			mov	rax, QWORD [offy]
			add	rax, rbx
			mul	QWORD [side]
			add	rax, QWORD [offx]
			add	rax, rcx
			mov	rdx, 8
			mul	rdx
			lea	rdx, [grid]
			add	rax, rdx
			inc	QWORD [rax]
		cmp	rcx, 0
		jne	inner_loop

	cmp	rbx, 0
	jne	outer_loop

	jmp	loop

	end:
	; go through the entire grid and count number which are higher than 2
	mov	rax, QWORD [side]	; rax = side
	mul	QWORD [side]		; rax = side*side
	mov	rdx, 8
	mul	rdx
	counting_loop:
	sub	rax, 8
	lea	rcx, [grid]
	add	rcx, rax
	mov	rbx, QWORD [rcx]	
	cmp	rbx, 2
	jl	skip
	inc	QWORD [answer]
	skip:
	cmp	rax, 0
	jne	counting_loop

	mov	rdi, printint
	mov	rsi, [answer]
	mov	rax, 0
	call	printf

	; Exit
	mov	rsp, rbp
	pop	rbp
	mov	rax, 60 ; exit
	mov	rbx, 0
	syscall   ; exit(0)

