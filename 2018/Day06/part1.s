extern printf
extern scanf

section .data
	; Scanf/printf stuff
	readcoords: db "%d, %d", 0
	printint: db "%lld", 10, 0
	answer: dq 0

	; Input data
	id: dd 1
	x: dd 1
	y: dd 0

	; Storage

	; Input data storage
	; 4 bytes id
	; 4 bytes x
	; 4 bytes y
	points: times 100*(4+4+4) db 0

	; Grid
	; 1000x1000 large
	; 4 bytes current id (0 if noone has taken it, 255 if two points are equally close)
	; 4 bytes length to the id
	grid: times 1000*1000*(4+4) db 0

	; Edge ids
	; id x is infinite if corresponding place in this array is 0
	candidates: times 256 db 1

	; Best area
	best: dq 0
	bestid: dq 0

section .text
	global main


; Calculate which things have infinite area
; If it managed to reach all the way to the edge, it is infinite
remove_infs:
	push	rbp
	mov	rbp, rsp

	push	rax
	push	rbx
	push	rcx
	push	rdx

	mov	rbx, 0
	mov	r8, 0

	; Upper border
	mov	r8, 0
	lea	rcx, [grid]
	remove_loop:
		mov	ebx, DWORD [rcx]
		lea	ebx, [candidates+ebx]
		mov	BYTE [ebx], 0

		add	rcx, 8
		inc	r8
		cmp	r8, 1000
		jne	remove_loop
	
	; Lower border
	mov	r8, 0
	lea	rcx, [grid+1000*999*8]
	remove_loop2:
		mov	ebx, DWORD [rcx]
		lea	ebx, [candidates+ebx]
		mov	BYTE [ebx], 0

		add	rcx, 8
		inc	r8
		cmp	r8, 1000
		jne	remove_loop2

	; Left side
	mov	r8, 0
	lea	rcx, [grid]
	remove_loop3:
		mov	ebx, DWORD [rcx]
		lea	ebx, [candidates+ebx]
		mov	BYTE [ebx], 0

		add	rcx, 1000*8
		inc	r8
		cmp	r8, 1000
		jne	remove_loop3

	; Right side
	mov	r8, 0
	lea	rcx, [grid+999*8]
	remove_loop4:
		mov	ebx, DWORD [rcx]
		lea	ebx, [candidates+ebx]
		mov	BYTE [ebx], 0

		add	rcx, 1000*8
		inc	r8
		cmp	r8, 1000
		jne	remove_loop4


	pop	rdx
	pop	rcx
	pop 	rbx
	pop	rax

	mov	rsp, rbp
	pop	rbp
	ret

; Count occurences of (non-infinite) candidate
; Candidate in rsi
candidate_count:
	push	rbp
	mov	rbp, rsp
	push	rbx
	push	rcx
	push	rdx
	
	mov	rax, 0
	lea	rbx, [grid]
	mov	rcx, 1000*1000
	candidate_loop:
		mov	edx, DWORD [rbx]
		cmp	edx, esi
		jne	skippy
		inc	rax
		skippy:
		add	rbx, 8
	loop	candidate_loop
	
	pop	rdx
	pop	rcx
	pop	rbx
	mov	rsp, rbp
	pop	rbp
	ret

; Calculate distance between r8 and r9, returns val in ebx
dist:
	push	rbp
	mov	rbp, rsp

		mov	r10, r8
		mov	rbx, r9
		cmp	r10, rbx
		jg	is_greater
		sub	rbx, r10
		jmp	done_dist

		is_greater:
		sub	r10, rbx
		mov	rbx, r10
	
	done_dist:
	mov	rsp, rbp
	pop	rbp
	ret

; Fills the grid from [x] and [y]
fill_grid:
	push	rax
	push	r10
	push	rbx
	push	rcx
	push	rdx
	push	rbp
	mov	rbp, rsp


	mov	rdi, 0 ; y
	outer_loop:
		mov	rsi, 0 ; x
		inner_loop:
			; calculate index into grid (into rax)
			push	rdx
			mov	eax, edi
			mov	r10, 1000	
			mul	r10
			add	eax, esi
			mov	r10, 8
			mul	r10
			lea	ebx, [grid]
			add	eax, ebx
			pop	rdx

			; Calculate manhattan distance (into rcx)
			mov	r8, 0
			mov	r9, 0
			mov	r8d, DWORD [x]
			mov	r9d, esi
			call	dist
			mov	rcx, rbx
			mov	r8d, DWORD [y]
			mov	r9d, edi
			call	dist
			add	rcx, rbx

			; is id a zero?	 then we fill!
			mov	ebx, DWORD [eax]
			cmp	ebx, 0
			jne	not_zero
				; Set id
				mov	ebx, DWORD [id]
				mov	DWORD [eax], ebx
				add	eax, 4
				mov	DWORD [eax], ecx
				jmp	continue

			; not a zero? then check if our length is smaller
			not_zero:
				mov	ebx, DWORD [rax+4]
				cmp	ecx, ebx
				je	equals

				cmp	ecx, ebx
				jg	continue

				mov	edx, DWORD [id]
				mov	DWORD [eax], edx
				mov	DWORD [eax+4], ecx
				jmp	continue

				equals:
				mov	DWORD [rax], 255
				mov	DWORD [rax+4],  ecx
				jmp	continue


		continue:
		inc	rsi
		cmp	rsi, 1000
		jl	inner_loop

	inc	rdi
	cmp	rdi, 1000
	jl	outer_loop


	end_fill_grid:
	mov	rsp, rbp
	pop	rbp
	pop	rdx
	pop	rcx
	pop	rbx
	pop	r10
	pop	rax
	ret

main:
	; reserve things on stack
	push	rbp
	mov	rbp, rsp

	reading_loop:
	; Read coordinates
	mov	rdi, readcoords
	lea	rsi, [x]
	lea	rdx, [y]
	mov	rax, 0
	call	scanf

	; If we did not manage to read digits, exit
	cmp	rax, 2
	jne	end_reading_loop

	; Fill the grid
	mov	rsi, 0
	mov	rdi, 0
	mov	esi, DWORD [x]
	mov	edi, DWORD [y]
	call	fill_grid

	inc	DWORD [id]

	jmp reading_loop
	end_reading_loop:

	; Go through the entire grid and remove the entries which are at the edge
	call	remove_infs

	; Check out the remaining candidates and count their entires
	mov	rcx, 0
	lea	rdx, [candidates]
	counting_loop:
		; Inc
		inc	rdx
		inc	rcx

		; Check
		movzx	rbx, BYTE [rdx]
		cmp	rbx, 0
		je	counting_loop

		; Let's count!
		mov	rsi, rcx
		call	candidate_count

		cmp	rax, QWORD [best]
		jl	skipthing
		mov	QWORD [best], rax
		mov	QWORD [bestid], rcx

		skipthing:
		
	cmp	rcx, 100
	jl	counting_loop
	

	; Write the answer
	mov	rdi, printint
	mov	rsi, [best]
	mov	rax, 0
	call	printf

	; Exit
	mov	rsp, rbp
	pop	rbp
	ret
