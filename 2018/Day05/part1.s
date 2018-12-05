extern printf
extern scanf

section .data
	; Printf/scanf stuff
	readstr: db "%s", 0
	printstr: db "%s", 10, 0
	printint: db "%d", 10, 0

	; Data
	str: times 60000 db 0


section .text
	global main

; Goes through the string (pointer in rdi) and modifies it (replaces xX with spaces)
; Returns number of entires modified (in rax)
make_pass:
	push	rbx
	push	rcx
	push	rdx
	push	rbp
	mov	rbp, rsp

	mov	rax, 0		; return value
	mov	rcx, 0x22	; most recent (non-space) character
	mov	rdx, rdi	; pointer to most recent (non-space) character

	loop:
		mov	r12, rdx

		movzx	rbx, BYTE [rdi]	; read current character
		cmp	rbx, 32		; if it's a space, skip it
		je	skip

		mov	r12, rdi	; Store pointer to most recently read

		; Check if current char should be removed
		xor	rbx, rcx	; xor current with last read
		cmp	rbx, 32		; if == 32, they are polar and should be removed
		jne	skip

		; Remove current char & previous char
		mov	BYTE [rdi], 32
		mov	BYTE [rdx], 32
		add	rax, 2

		skip:
		mov	rdx, r12	; Update pointer to "most recent" character
		movzx	rcx, BYTE [rdx]	; Update "most recent" character
		movzx	rbx, BYTE [rdi]
		inc	rdi	

		; If we got a zero, break
		cmp	rbx, 0
		jne	loop

	mov	rsp, rbp
	pop	rbp
	pop	rdx
	pop	rcx
	pop	rbx
	ret

main:
	push	rbp
	mov	rbp, rsp

	; Read a string
	mov	rdi, readstr
	lea	rsi, [str]
	mov	rax, 0
	call	scanf

	; Make passes on the string until no more changes occur
	removing_loop:
		lea	rdi, [str]
		call	make_pass
	cmp	rax, 0
	jne	removing_loop

	; Count number of non-space character
	mov	rax, 0
	lea	rdi, [str]
	counting_loop:
		movzx	rbx, BYTE [rdi]
		inc	rdi
		cmp	rbx, 0
		je	finished_counting

		cmp	rbx, 32
		je	counting_loop
		inc	rax
	jmp	counting_loop


	finished_counting:
	; Print the answer
	mov	rdi, printint
	mov	rsi, rax
	mov	rax, 0
	call	printf

	; Exit
	mov	rsp, rbp
	pop	rbp
	ret

