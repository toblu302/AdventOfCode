extern printf
extern scanf

section .data
	buffer:	db '0'
	readstr: db "%s", 0
	printint: db "%d", 10, 0
	printstr: db "%s", 10, 0
	str: times 32 db 0
	letter_counter: times 26 db 0
	two_count: dq 0
	three_count: dq 0

section .text
	global main

main:
	; reserve things on stack
	push	rbp
	mov	rbp, rsp

	loop:
	; Read a string
	mov	rdi, readstr
	lea	rsi, [str]
	mov	rax, 0
	call	scanf

	; If we did not manage to read a string, exit
	cmp	rax, 1
	jne	end

	; Count occurences of every character
	; 1) Set all the counters to 0
	mov	rcx, 26	
	reset_loop:
	dec	rcx
	lea	rax, [letter_counter]
	add	rax, rcx
	mov	BYTE [rax], 0
	cmp	rcx, 0
	jne	reset_loop

	; 2) Count characters
	mov	rcx, 0
	counting_loop:
	lea	rax, [str]
	add	rax, rcx
	movzx	rax, BYTE [rax]	; rax now contains current character
	inc	rcx
	cmp	rax, 97	; Is the character < 97?
	jl	skip	; Then skip it
	cmp	rax, 122; Is the character > 122?
	jg	skip	; Then skip it
	mov	rdx, rax
	sub	rdx, 97 ; rdx now contains character index
	lea	rbx, [letter_counter]
	add	rbx, rdx
	inc	BYTE [rbx]
	skip:
	cmp	rax, 0
	jne	counting_loop

	; 3) Check for character which occurs twice
	mov	rcx, 26
	two_loop:
	dec	rcx
	lea	rax, [letter_counter]
	add	rax, rcx
	movzx	rax, BYTE [rax]
	cmp	rax, 2
	jne	not_two
	inc	QWORD [two_count]
	jmp two_loop_end
	not_two:
	cmp	rcx, 0
	jne two_loop
	two_loop_end:

	; 4) Check for characters which occurs three times
	mov	rcx, 26
	three_loop:
	dec	rcx
	lea	rax, [letter_counter]
	add	rax, rcx
	movzx	rax, BYTE [rax]
	cmp	rax, 3
	jne	not_three
	inc	QWORD [three_count]
	jmp three_loop_end
	not_three:
	cmp	rcx, 0
	jne three_loop
	three_loop_end:

	jmp loop

	end:
	; Write the answer
	mov	rdi, printint
	mov	rsi, [three_count]
	mov	rax, [two_count]
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

