6장

8. In the following instruction sequence, show the resulting value of AL where indicated, in
hexadecimal:
mov  al,7Ah
not  al 		; a. -> 
mov  al,3Dh
and  al,74h 	; b. -> 
mov  al,9Bh
or   al,35h 		; c. -> 
mov  al,72h
xor  al,0DCh 	; d. ->
9. In the following instruction sequence, show the values of the Carry, Zero, and Sign flags
where indicated:
mov  al,00001111b
test al,00000010b 		; a. CF=  ZF=   SF= 
mov  al,00000110b
cmp  al,00000101b 		; b. CF=   ZF=  SF= 
mov  al,00000101b
cmp  al,00000111b		; c. CF=   ZF=   SF= 

10. Which conditional jump instruction executes a branch based on the contents of ECX?

11. How are JA and JNBE affected by the Zero and Carry flags?

12. What will be the final value in EDX after this code executes?
    mov  edx,1
    mov  eax,7FFFh
    cmp  eax,8000h
    jl   L1
    mov  edx,0
L1:
14. What will be the final value in EDX after this code executes?
    mov  edx,1
    mov  eax,7FFFh
    cmp  eax,0FFFF8000h
    jl   L2
    mov  edx,0
L2: 
1. Write a single instruction that converts an ASCII digit in AL to its corresponding binary
value. If AL already contains a binary value (00h to 09h), leave it unchanged
-> and al, 0Fh
문자 '5' = 35h (2진수: 0011 0101)
진짜 숫자 5 = 05h (2진수: 0000 0101)
