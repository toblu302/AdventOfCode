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
	colliding: times 2000 dq 0
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
			add	rax, rdx	; rax now contains index
			mov	rdx, QWORD [rax]	; fet last write to memory position
			mov	r8, QWORD [id]
			mov	QWORD [rax], r8	; write own id to memory position
			cmp	rdx, 0
			je	ok
				; We have some overlap! id1 in rdx and id2 in [id]
				mov	r8, 8
				mov	rax, rdx
				mul	r8
				lea	rdx, [colliding]
				add	rax, rdx	; id1 index in rax
				mov	QWORD [rax], 1
				mov	rax, QWORD [id]
				mul	r8
				lea	rdx, [colliding]
				add	rax, rdx	; id2 index in rax
				mov	QWORD [rax], 1
			ok:
		cmp	rcx, 0
		jne	inner_loop

	cmp	rbx, 0
	jne	outer_loop

	jmp	loop

	end:
	; go through the list of colliding stuff and find the one which does not collide
	mov	rax, [id]
	mov	QWORD [answer], rax
	finding_loop:
	dec	QWORD [answer]
	mov	rax, QWORD [answer]
	mov	rdx, 8
	mul	rdx
	lea	rcx, [colliding]
	add	rcx, rax
	mov	rbx, QWORD [rcx]	
	cmp	rbx, 0
	je	fin
	cmp	QWORD [answer], 0
	jne	finding_loop

	fin:
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

