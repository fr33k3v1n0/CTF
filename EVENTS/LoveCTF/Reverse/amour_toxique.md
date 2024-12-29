# chall name : "amour Toxique"

we are given a ELF 64-bit LSB filel

```bash
file amourToxique
amourToxique: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=a8b67c3d872a23f3a651007f8c5781fe44ebe269, for GNU/Linux 3.2.0, not stripped
```
```bash
$ strings  amourToxique
/lib64/ld-linux-x86-64.so.2
__libc_start_main
__cxa_finalize
printf
libc.so.6
GLIBC_2.2.5
GLIBC_2.34
_ITM_deregisterTMCloneTable
__gmon_start__
_ITM_registerTMCloneTable
PTE1
u+UH
TG92ZUNUH
RntsM3RfH
dXNxxxddH
dfdzFdsuH
ffdXfdsfH
3sddpdGhH
fcGFzczEH
wMG5ufQ=H
RXXMZKDKH
RDHW3BTOH
RPXK427OH
4YW4X3XNH
F2GQX3QMH
FXGMJQGBH
QGBNGXG4H
7NGqsI=
9Q,)c6W?H
O%Ch@*kAH
%Ch@*kARH
B%c@:su
<rv{VG]nH
FLo7WVB'H
Lo7WVB'CH
Sk;P|e}
JRXXMZKDH
KRDHW3BTH
ORPXK427H
O4YW4X3XH
NF2GQX3QH
MFZXGMJQH
GBXG47I
$T9O/E1NH
8/+8UVD9H
D9ECV CUH
.C5ECZ2
4c 6f 76H
 65 43 5H
4 46 7b H
6c 66 61H
 6b 65 5H
f 66 6c H
 66 6c 6H
1 67 7d
{@G6r%uLH
=72<607=H
f3d05ba5H
9c21c490H
f9ca1907H
9ff22ecfH
13617fa8H
72f0cbcfH
dec897d0H
86c3dadeH
f5b08014H
7b5101b8H
8813ac5aH
4c04a57eH
Ilsb@QCxH
ic^hb\ciH
The flag is: %s
```
in this output, we have some base64 encoded string and some hexadecimal string.
let analyze the hexa string
```bash
$ python3
Python 3.11.7 (main, Dec  8 2023, 14:22:46) [GCC 13.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> text = """4c 6f 76H
...  65 43 5H
... 4 46 7b H
... 6c 66 61H
...  6b 65 5H
... f 66 6c H
...  66 6c 6H
... 1 67 7d
... """
>>> text.replace("\n",'')
'4c 6f 76H 65 43 5H4 46 7b H6c 66 61H 6b 65 5Hf 66 6c H 66 6c 6H1 67 7d'
>>> text.replace("\n",'').replace("H", '')
'4c 6f 76 65 43 54 46 7b 6c 66 61 6b 65 5f 66 6c  66 6c 61 67 7d'
>>> text.replace("\n",'').replace("H", '').replace(" ", '')
'4c6f76654354467b6c66616b655f666c666c61677d'
>>> hexstring = text.replace("\n",'').replace("H", '').replace(" ", '')
>>> bytes.fromhex(hexstring)
b'LoveCTF{lfake_flflag}'
```
ahh fake flag.😲
# ok why not dig more by debugging the program 
# gdb-pwndbg is my Friend 

```bash
pwndbg> file amourToxique
Reading symbols from amourToxique...
(No debugging symbols found in amourToxique)
pwndbg> info functions
All defined functions:

Non-debugging symbols:
0x0000000000001000  _init
0x0000000000001030  printf@plt
0x0000000000001040  __cxa_finalize@plt
0x0000000000001050  _start
0x0000000000001080  deregister_tm_clones
0x00000000000010b0  register_tm_clones
0x00000000000010f0  __do_global_dtors_aux
0x0000000000001130  frame_dummy
0x0000000000001139  main
0x0000000000001504  _fini
pwndbg> 
```
the only intersting function is main.
I  disassembled the main function and see that the file deal with more string
than what is output when whe execute the program
```bash
pwndbg> disassemble main
Dump of assembler code for function main:
   0x0000000000001139 <+0>:     push   rbp
   0x000000000000113a <+1>:     mov    rbp,rsp
   0x000000000000113d <+4>:     sub    rsp,0x200
   0x0000000000001144 <+11>:    lea    rax,[rbp-0x200]
   0x000000000000114b <+18>:    movabs rdx,0x554e555a32394754
   0x0000000000001155 <+28>:    movabs rcx,0x6652334d73746e52
   0x000000000000115f <+38>:    mov    QWORD PTR [rax],rdx
   0x0000000000001162 <+41>:    mov    QWORD PTR [rax+0x8],rcx
   0x0000000000001166 <+45>:    movabs rsi,0x64647878784e5864
   0x0000000000001170 <+55>:    movabs rdi,0x757364467a646664
   0x000000000000117a <+65>:    mov    QWORD PTR [rax+0x10],rsi
   0x000000000000117e <+69>:    mov    QWORD PTR [rax+0x18],rdi
   0x0000000000001182 <+73>:    movabs rdx,0x6673646658646666
   0x000000000000118c <+83>:    movabs rcx,0x6847647064647333
   0x0000000000001196 <+93>:    mov    QWORD PTR [rax+0x20],rdx
   0x000000000000119a <+97>:    mov    QWORD PTR [rax+0x28],rcx
   0x000000000000119e <+101>:   movabs rsi,0x457a637a46476366
   0x00000000000011a8 <+111>:   movabs rdi,0x3d51667535474d77
   0x00000000000011b2 <+121>:   mov    QWORD PTR [rax+0x30],rsi
   0x00000000000011b6 <+125>:   mov    QWORD PTR [rax+0x38],rdi
   0x00000000000011ba <+129>:   mov    WORD PTR [rax+0x40],0x3d

```
we can see that the local variable stored at rbp-0x200 is a buffer(array or
char pointer) in which some string are coped.
0x3d is "=" ascii code and we now that '=' or '==' are used as padding for
base64 encoded string. so the 0x3d will be the end of some encoded string.
# this two line script give us the first string which is stor at rbp-0x200
```python
hexstring =["0x554e555a32394754","0x6652334d73746e52","0x64647878784e5864","0x757364467a646664","0x6673646658646666","0x6847647064647333","0x457a637a46476366","0x3d51667535474d77","0x3d"] 
print(b''.join(bytes.fromhex( l[2:])[::-1] for l in hexstring).decode())

```
```bash
python3 get_string.py
TG92ZUNURntsM3RfdXNxxxdddfdzFdsuffdXfdsf3sddpdGhfcGFzczEwMG5ufQ==

```
we get this base64 encoded string:
TG92ZUNURntsM3RfdXNxxxdddfdzFdsuffdXfdsf3sddpdGhfcGFzczEwMG5ufQ
```bash
┌──(top0n3㉿top0n3)-[/media/…/trainning/ctf/loveCTf/reverse]
└─$ echo "TG92ZUNURntsM3RfdXNxxxdddfdzFdsuffdXfdsf3sddpdGhfcGFzczEwMG5ufQ==" | base64 -d 
LoveCTF{l3t_usq�]u�s�.}�W}���]�ѡ}����������base64: invalid input

```
what? but this look like a flag !!!. 😰
#  don't forget the description of this chall told us thas the scret message is  scrambed whit something.  the encoded chaine is corromptud by adding some char. we need to repair it

#o we need to remove some char from this base64 encoded chaine.
- First i see xxxddd, that is very bad. let remoce it.
the string become: TG92ZUNURntsM3RfdXNfdzFdsuffdXfdsf3sddpdGhfcGFzczEwMG5ufQ==

```bash
$ echo "TG92ZUNURntsM3RfdXNfdzFdsuffdXfdsf3sddpdGhfcGFzczEwMG5ufQ==" | base64 -d
LoveCTF{l3t_us_w1]���uwݱ��u�]▒�▒\��L
                                    �base64: invalid input
```
still invalid

i dig more and finaly, i know that the valide string is: TG92ZUNURntsM3RfdXNfdzFuX3dpdGhfcGFzczEwMG5ufQo=
```bash
(top0n3㉿top0n3)-[/media/…/trainning/ctf/loveCTf/reverse]
└─$ echo "TG92ZUNURntsM3RfdXNfdzFuX3dpdGhfcGFzczEwMG5ufQo=" | base64 -d
LoveCTF{l3t_us_w1n_with_pass100nn}
```

# So we get the flag 🏁

