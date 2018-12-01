extern printf
extern scanf

section .data
	buffer:	db '0'
	readint: db "%ld", 0
	printint: db "%ld", 10, 0

	current: dq 0

	history: times 200000 dq 0
	num_read: dq 8

	input: times 1200 dq 0
	num_input_read: dq 0
	ci: dq 0

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

	; If we did not manage to read a digit, use the history instead
	cmp	rax, 1
	je	proceed
	lea	rax, [input]
	add	rax, QWORD [ci]
	mov	rax, QWORD [rax]
	lea	rcx, [rsp+8]
	mov	[rcx], rax
	add	QWORD [ci], 8
	mov	rax, QWORD [num_input_read]
	cmp 	rax, QWORD [ci]
	ja	proceed2
	sub	QWORD [ci], rax
	jmp proceed2

	proceed:
	; Update input list
	lea	rax, [input]
	add	rax, QWORD [num_input_read]
	mov	rcx, QWORD [rsp+8]
	mov	QWORD [rax], rcx
	add	QWORD [num_input_read], 8

	proceed2:
	; Update current
	mov	rax, QWORD [current]
	add	rax, QWORD [rsp+8]
	mov	QWORD [current], rax

	; Store the current digit to the history array
	lea	rax, [history]
	add	rax, QWORD [num_read]
	mov	rcx, QWORD [current]
	mov	QWORD [rax], rcx
	add	QWORD [num_read], 8

	; Loop through history and try to find the digit we read last
	mov	rcx, QWORD [num_read]
	sub	rcx, 8
	history_loop:
	sub	rcx, 8
	mov	rax, history
	add	rax, rcx
	mov	rdx, QWORD [rax]
	cmp	rdx, QWORD [current]
	je	end	
	cmp	rcx, 0
	jne	history_loop

	jmp loop

	end:
	; Write the answer
	mov	rdi, printint
	mov	rsi, [current]
	mov	rax, 0
	call	printf

	; Exit
	mov	rsp, rbp
	pop	rbp
	mov	rax, 60 ; exit
	mov	rbx, 0
	syscall   ; exit(0)

