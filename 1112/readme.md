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

si, di는 주소를 가지고있다  <br>

.data <br> 
source DWORD 1234h   ;4바이트(DWORD) 크기의 source 변수를 선언하고 16진수 1234h (00001234h)를 저장 <br>
target DWORD 5678h   ;4바이트(DWORD) 크기의 target 변수를 선언하고 16진수 5678h (00005678h)를 저장 <br>
.code <br>
mov esi,OFFSET source   ;urce 변수의 메모리 시작 주소를 ESI 레지스터에 넣는다 <br>
mov edi,OFFSET target   ;target 변수의 메모리 시작 주소를 EDI 레지스터에 넣는다 <br>
cmpsd <br>
ja L1 <br>  ;비교하는 값은 1234h vs 5678h<br>

LODS = 메모리([ESI])에서 데이터를 읽어 CPU 레지스터(EAX)로 가져오고, ESI 주소를 자동으로 이동시키는 명령어 <br>
.data <br>
myString BYTE "HELLO", 0 <br>

.code <br>
cld                     ; Direction Flag = 0 (순방향, ESI 주소 증가) <br>
mov esi, OFFSET myString; ESI에 문자열 시작 주소 보관 <br>

lodsb                   ; 1. [ESI]에서 'H'를 읽어 AL에 저장 <br>
                        ; 2. ESI 주소가 자동으로 +1 증가함 (다음 글자 'E' 위치) <br>

lodsb                   ; 1. [ESI]에서 'E'를 읽어 AL에 저장 <br>
                        ; 2. ESI 주소가 자동으로 +1 증가함 (다음 글자 'L' 위치) <br>

MUL = ax와 dx를 거쳐서 값을 넣는다 <br>
INVOKE Str_compare, ADDR STring1, ADDR String2 -> String1과 String2를 비교함 <br>
String1 < String2 : Carry Flag = 1 , Zero Flag = 0, Branch If True = JB <br>
String1 = String2 : Carry Flag = 0 , Zero Flag = 1, Branch If True = JE <br>
String1 > String2 : Carry Flag = 0 , Zero Flag = 0, Branch If True = JA <br>

Base-Index -> 두 개의 레지스터(기준점 + 위치)를 합쳐서 메모리 주소를 찾아내는 방식<br>
Word일 때 <br>
mov esi, 0 → WORD 배열의 0번째 요소 (array[0])를 가리킴 <br>
mov esi, 2 → WORD 배열의 1번째 요소 (array[1])를 가리킴 (2바이트 건너뜀) <br>

Sorting하면 searching이 나옴
