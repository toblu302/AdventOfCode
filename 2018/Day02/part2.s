extern printf
extern scanf

section .data
	buffer:	db '0'
	readstr: db "%s", 0
	printint: db "%d", 10, 0
	printstr: db "%s", 10, 0
	printchr: db "%c", 0
	current_index: dq 0
	history: times 32*300 db 0
	diff_counter: db 0
	diff_spot: dq 0
	shit: dq 0

section .text
	global main

main:
	; reserve things on stack
	push	rbp
	mov	rbp, rsp

	; Set current_index to first value
	lea	rax, [history]
	mov	QWORD [current_index], rax

	loop:
		; Read a string
		mov	rdi, readstr
		mov	rsi, QWORD [current_index]
		mov	rax, 0
		call	scanf

		; If we did not manage to read a string, exit
		cmp	rax, 1
		jne	end

		; Move through all the previous strings
		mov	rcx, QWORD [current_index]	; rcx = most recently read string start
		mov	rdx, QWORD [current_index]	; rdx = current string start
		outer_loop:
			cmp	rdx, history
			je break_outer_loop

			sub	rdx, 32
			mov	rbx, 32			; rbx = string index
			mov	BYTE [diff_counter], 0	; reset difference counter
			inner_loop:
				dec	rbx
				mov	rax, rcx	; rax = start of string a
				add	rax, rbx	; rax = string a index j
				movzx	rax, BYTE [rax]	; al = character at pos j
				mov	r8, rdx		; r8 = start of string b
				add	r8, rbx		; r8 = string b index j
				movzx	r8, BYTE [r8]
				cmp	rax, r8
				je	no_diff
					inc	BYTE [diff_counter]
					mov	BYTE [diff_spot], bl
				no_diff:
			cmp	rbx, 0
			jne inner_loop

		cmp	BYTE [diff_counter], 1	; Did we only find one difference?
		je 	end			; Then jump to the end
		jmp	outer_loop
		break_outer_loop:
		
		; Move current_index pointer to next correct position
		mov	rax, QWORD [current_index]
		add	rax, 32
		mov	QWORD [current_index], rax


	jmp loop

	end:
	; Write the answer
	mov	rbx, 0
	write_loop:
		mov	rdi, printchr
		movzx	rsi, BYTE[rdx]
		cmp	rsi, 0
		je	write_loop_end
		mov	rax, 0
		push 	rdx	; printf destroys rdx for some reason
		call	printf
		pop	rdx
		add	rdx, 1
		inc	rbx
	cmp	rbx, QWORD [diff_spot]
	jne	write_loop
	add	rdx, 1
	mov	QWORD [diff_spot], 32
	jmp	write_loop
	write_loop_end:

	mov	rdi, printchr
	mov	rsi, 0xa
	mov	rax, 0
	call	printf

	; Exit
	mov	rsp, rbp
	pop	rbp
	mov	rax, 60 ; exit
	mov	rbx, 0
	syscall   ; exit(0)

