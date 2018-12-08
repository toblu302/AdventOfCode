extern printf
extern scanf

section .data
	; Scanf/printf stuff
	readcoords: db "%d, %d", 0
	printint: db "%lld", 10, 0
	printchar: db "%c", 0
	scanformat: db "Step %c must be finished before step %c can begin.", 10, 0
	answer: dq 0

	; Input data
	ch1: db 0
	ch2: db 0

	; Dependencies
	; Every node has a list of the stuff it depends on
	; For each entry: 1 byte for "printed" (0) and "unprinted" (1)
	; For each entry: 26 bytes for "depends on" (1) and "does not depend on" (0)
	deps: times 26*27 db 0

section .text
	global main


; Add dependency "x depends on y", x in rsi, y in rdi
add_deps:
	push	rbp
	mov	rbp, rsp
	push	rax

	; mark x as "unprinted"
	mov	rax, rsi
	sub	rax, 65
	mov	r8, 27
	mul	r8
	lea	rax, [deps+rax]
	mov	BYTE [rax], 1

	; mark dependency
	sub	rdi, 64
	add	rax, rdi
	mov	BYTE [rax], 1

	; mark y as "unprinted"
	dec	rdi
	mov	r8, 27
	mov	rax, rdi
	mul	r8
	lea	rax, [deps+rax]
	mov	BYTE [rax], 1

	pop	rax
	mov	rsp, rbp
	pop	rbp
	ret

; Check if the character which rsi points to is allowed to be printed
; rax=1 if allowed to be printed, rax=0 otherwise
check_dependencies:
	push	rbp
	mov	rbp, rsp
	push	rcx
	push	rbx

	mov	r8, 1 ; return value

	inc	rsi
	mov	rcx, 0
	dep_check_loop:
		movzx	rbx, BYTE [rsi]
		cmp	rbx, 0
		je	no_dep

		; If we have a dependency, check if we've already printed it
		mov	rax, rcx
		mov	r9, 27
		mul	r9
		lea	rbx, [deps+rax]
		movzx	rbx, BYTE [rbx]
		cmp	rbx, 0
		je	no_dep
		mov	r8, 0
		jmp	done_checking

		no_dep:
	inc	rsi
	inc	rcx
	cmp	rcx, 27
	jne	dep_check_loop

	done_checking:
	mov	rax, r8
	pop	rbx
	pop	rcx
	mov	rsp, rbp
	pop	rbp
	ret

; finds and prints one allowed character. Returns 1 if successful, 0 otherwise
print_one:
	push	rbp
	mov	rbp, rsp
	push	rbx
	push	rcx

	mov	r8, 0

	; Loop through all the characters
	lea	rbx, [deps]
	mov	rcx, 0
	find_char_loop:
		; Is it a zero? Skip it.
		movzx	rdx, BYTE [rbx]
		cmp	rdx, 0
		je	skip

		; Not a zero? Check if dependencies has been printed.
		mov	rsi, rbx
		call	check_dependencies

		; If we are allowed to print character, print it
		cmp	rax, 0
		je	skip

		; Write the character
		mov	rdi, printchar
		mov	rsi, rcx
		add	rsi, 65
		mov	rax, 0
		call	printf

		; Mark character as printed
		mov	BYTE [rbx], 0
		mov	r8, 1

		jmp	done_printing

	skip:
	add	rbx, 27
	inc	rcx
	cmp	rcx, 26
	jne	find_char_loop

	done_printing:
	mov	rax, r8
	pop	rcx
	pop	rbx
	mov	rsp, rbp
	pop	rbp
	ret


; main function
main:
	; reserve things on stack
	push	rbp
	mov	rbp, rsp

	reading_loop:
	; Read the two characters
	mov	rdi, scanformat
	lea	rsi, [ch1]
	lea	rdx, [ch2]
	mov	rax, 0
	call	scanf

	; If we did not manage to read characters, exit
	cmp	rax, 2
	jne	end_reading_loop

	; Add dependency
	movzx	rdi, BYTE [ch1]
	movzx	rsi, BYTE [ch2]
	call	add_deps


	jmp reading_loop
	end_reading_loop:

	; Print characters in order
	print_dep_loop:
		call	print_one
		cmp	rax, 1
		je	print_dep_loop

	; Write new line
	mov	rdi, printchar
	mov	rsi, 10
	mov	rax, 0
	call	printf

	; Exit
	mov	rax, 0
	mov	rsp, rbp
	pop	rbp
	ret
