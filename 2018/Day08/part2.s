extern printf
extern scanf

section .data
	; Scanf/printf stuff
	readint: db "%lld", 0
	printint: db "%lld", 10, 0

	; Data
	input: dq 0
	answer: dq 0
	num_children: equ 20 ; max number of children
	

section .text
	global main

; returns its score in rax
read_tree:
	push	rbp
	mov	rbp, rsp

	push	r14	; number of child nodes
	push	r15	; number of metadata entries
	push	rcx	; loop counter
	push	rbx	; read items
	push	r8	; return value
	sub	rsp, num_children*8

	; Set all the children values to 0
	mov	rcx, 0
	clearing_loop:
		mov	QWORD [rsp+rcx*8], 0
	inc	rcx
	cmp	rcx, num_children
	jne	clearing_loop

	; Read number of child nodes
	mov	rdi, readint
	lea	rsi, [input]
	mov	rax, 0
	call	scanf
	mov	r14, QWORD [input]

	; Read number of metadata entries
	mov	rdi, readint
	lea	rsi, [input]
	mov	rax, 0
	call	scanf
	mov	r15, QWORD [input]

	; Read each child node
	mov	rcx, 0
	cmp	r14, 0
	je	child_loop_skip
	child_loop:
		call	read_tree
		mov	QWORD [rsp+8+rcx*8], rax
	inc	rcx
	cmp	rcx, r14
	jne	child_loop
	child_loop_skip:

	; Read each metadata entry
	mov	rcx, r15
	metadata_loop:
		; Read digit
		push	rcx
		push	r8
		mov	rdi, readint
		lea	rsi, [input]
		mov	rax, 0
		call	scanf
		pop	r8
		pop	rcx

		; Do we have 0 children? Add to r8
		cmp	r14, 0
		je	no_children
			; Skip invalid stuff
			cmp	QWORD [input], num_children
			jge	continue
			cmp	QWORD [input], 0
			je	continue

			mov	rbx, QWORD [input]
			mov	rbx, QWORD [rsp+rbx*8]
			add	r8, rbx
		jmp	continue
		no_children:
			mov	rbx, QWORD [input]
			add	r8, rbx

	continue:
	loop	metadata_loop

	mov	rax, r8
	add	rsp, num_children*8
	pop	r8
	pop	rbx
	pop	rcx
	pop	r15
	pop	r14
	mov	rsp, rbp
	pop	rbp
	ret

; main function
main:
	; reserve things on stack
	push	rbp
	mov	rbp, rsp

	call	read_tree

	; Write new line
	mov	rdi, printint
	mov	rsi, rax
	mov	rax, 0
	call	printf

	; Exit
	mov	rax, 0
	mov	rsp, rbp
	pop	rbp
	ret
