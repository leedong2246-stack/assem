.386
.model flat, stdcall
.stack 4096

ExitProcess PROTO, dwExitCode:DWORD
MessageBoxA PROTO, hWnd:DWORD, lpText:DWORD, lpCaption:DWORD, uType:DWORD

.data
titleStr BYTE "학생 정보 확인", 0
msgStr   BYTE "이름: 이동환", 13, 10, "학번: 2023664034", 0   ; 13, 10 은 줄바꿈(Enter)

.code
main PROC
    ; 윈도우 팝업창 띄우기
    INVOKE MessageBoxA, 0, ADDR msgStr, ADDR titleStr, 0

    INVOKE ExitProcess, 0
main ENDP

END main
