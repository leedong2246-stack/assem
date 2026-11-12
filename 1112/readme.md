문자 : 1 + 2 = '12'은 그냥 문자 <br>
숫자는 : 1은 1 + 2 = 3<br>
comppare, scan 둘다 비교하는데 조금 다름. <br>
AL, Ax or EAX -> accumualator di를 메모리 주소에 넣는것? <br>
String 기본적인 명령어 mov, cmp, scans <br>
메모리에 있는걸 cpu로 가져오는거 laod (DI에 있는 내용을) -> [ESI]의 메모리 값과 [EDI]의 메모리 값을 직접 비교. <br>
cpu에 있는걸 메모리로 가져가는거 Store (DI에 있는 내용을) <br>
B = Byte, W = Word, DW = doubleWord <br>
디렉션 플래그 스트링 명령어 실행 시 ESI, EDI 주소를 앞으로 이동시킬지(증가), 뒤로 이동시킬지(감소) 방향 결정 <br>
위치 : EFLAGS 레지스터의 10번째 비트 (Bit 10) <br>
.data <br>
source DWORD 20 DUP(0FFFFFFFFh) -> 초기화  ; 4바이트(DWORD) 20개 배열 선언 <br>
target DWORD 20 DUP(?) -> 초기화(x)        ; 4바이트(DWORD) 20개 빈 배열 선언 <br>

.code <br>
cld                             ; 복사 방향을 순방향(앞->뒤)으로 설정 <br>
mov ecx, LENGTHOF source        ; 반복 횟수(20)를 ECX에 저장 <br>
mov esi, OFFSET source          ; source의 시작 주소를 ESI에 저장 <br>
mov edi, OFFSET target          ; target의 시작 주소를 EDI에 저장 <br>
rep movsd                       ; ESI 주소에서 EDI 주소로 4바이트씩 20번 복사 <br>

Reapeat prefix -> REP (계속적으로 반복한다.) <br>
REPZ, REPE -> REPE / REPZ	ECX > 0 AND ZF = 1	서로 다른 값이 나오는 순간 (ZF = 0)	두 문자열이 같은지 비교할 때 (CMPS) <>br
REPNZ, REPNE -> REPNE / REPNZ	ECX > 0 AND ZF = 0	서로 같은 값이 나오는 순간 (ZF = 1)	문자열에서 특정 문자를 찾을 때 (SCAS) <br>

Direction Flag <br>
CLD → DF = 0 → 주소 증가 (앞에서 뒤로) <br>
STD → DF = 1 → 주소 감소 (뒤에서 앞으로) <br>
CL은 clear <br>
ST는 set <br>

si, di는 주소를 가지고있다  
