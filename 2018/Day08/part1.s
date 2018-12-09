extern printf
extern scanf

section .data
	; Scanf/printf stuff
	readint: db "%lld", 0
	printint: db "%lld", 10, 0

	; Data
	input: dq 0
	answer: dq 0
	

section .text
	global main

read_tree:
	push	rbp
	mov	rbp, rsp

	push	r14	; number of child nodes
	push	r15	; number of metadata entries
	push	rcx	; loop counter
	push	rbx	; read items

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
	mov	rcx, r14
	cmp	rcx, 0
	je	child_loop_skip
	child_loop:
		call	read_tree
	loop	child_loop
	child_loop_skip:

	; Read each metadata entry
	mov	rcx, r15
	metadata_loop:
		push	rcx
		; Read digit
		mov	rdi, readint
		lea	rsi, [input]
		mov	rax, 0
		call	scanf
		mov	rbx, QWORD [answer]
		add	rbx, QWORD [input]
		mov	QWORD [answer], rbx
		pop	rcx
	loop	metadata_loop

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
	mov	rsi, QWORD [answer]
	mov	rax, 0
	call	printf

	; Exit
	mov	rax, 0
	mov	rsp, rbp
	pop	rbp
	ret
