extern printf
extern scanf

section .data
	buffer:	db '0'
	readint: db "%d", 0
	printint: db "%d", 10, 0
	answer: dq 0

section .text
	global main

main:
	; reserve things on stack
	; answer: esp+8
	push	rbp
	mov	rbp, rsp
	sub	rsp, 8


	loop:
	; Read a digit
	mov	rdi, readint
	lea	rsi, [rsp+8]
	mov	rax, 0
	call	scanf

	; If we did not manage to read a digit, exit
	cmp	rax, 1
	jne	end

	; Update answer
	mov	rax, [answer]
	add	rax, [rsp+8]
	mov	[answer], rax

	jmp loop

	end:
	; Write the answer
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

