# chall Name: friend Shop

we are given a binary file
```bash
$ file FriendShipGoal
FriendShipGoal: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=464dc5e59d75ba490b1bde9b6e26007b255fedcf, for GNU/Linux 3.2.0, not stripped
```
when i use strings, i don't get more things.

i exec the prog and see that it is a simple crackme

# reverse the binary. GHIDRA, PWNDBG are my friends

when  i decompile the programe with ghidra, i get this.

```C
// main function    
undefined8 main(void)

{
  bool bVar1;
  undefined7 extraout_var;
  char local_28 [20];
  undefined8 local_14;
  undefined4 local_c;

  local_14 = 0x7552695d745e2176;
  local_c = 0x696463;
  printf("Entrez le mot de passe : ");
  __isoc99_scanf(&DAT_00102022,local_28);
  crypterMotDePasse(local_28);
  bVar1 = verifierMotDePasse((char *)&local_14,local_28);
  if ((int)CONCAT71(extraout_var,bVar1) == 0) {
    puts(&DAT_00102058);
  }
  else {
    puts(&DAT_00102028);
  }
  return 0;
}
// cryptMotDePass function

void crypterMotDePasse(char *param_1)

{
  size_t sVar1;
  int local_14;
  int local_10;
  int local_c;

  for (local_10 = 0; local_10 < 0x2711; local_10 = local_10 + 1) {
    local_c = local_10 % 0x10 + 0x10;
    if (255 < local_10) break;
  }
  sVar1 = strlen(param_1);
  for (local_14 = 0; local_14 < (int)sVar1; local_14 = local_14 + 1) {
    param_1[local_14] = param_1[local_14] ^ (byte)local_c;
  }
  return;
}

//verifyMoDePass function

bool verifierMotDePasse(char *param_1,char *param_2)

{
  int iVar1;

  iVar1 = strcmp(param_1,param_2);
  return iVar1 == 0;
}
```

# easy to understand 
the main function ask for password
encrypt it with encryptMotDePass function
and  verify that the encrypted version of the password i enter is egal to some
string.

we need to understant what encryptMotDePass function do.
after little analyze, i understand that it is a simple xor .

# i write this program to get the xor key. i'm a lazy boy 😄

```C
#include<stdlib.h>
#include<stdio.h>

void cryptmotdepass(void)
{
	int cpt1,cpt2, localc, len;
	for(cpt1 = 0; cpt1 < 1001; cpt1++){
		localc = cpt1 % 16 + 16;
		if(0xff < cpt1){
			printf("cpt1 = %d\n", cpt1);
			printf("xor key = %d\n", localc);
			break;
		}
	}

}

int main()
{
cryptmotdepass();
}
```

this program say that the xor key is: 16. true

# now we have the xor key, what we need is to get the first argument of
verifyMotDePass
pwngdb, breakpoint on strcmp, examine the value of $rdi and everything is ok 

```bash
pwndbg> x/s $rdi
0x7fffffffdaf4: "v!^t]iRucdi"
```

so to get the valid password, we need to xor "v!^t]iRucdi", with 16
```python
>>> from pwn import xor
>>> xor(b"v!^t]iRucdi", 16)
b'f1NdMyBesty'
>>>
```
the valid password is: f1NdMyBesty

# flag: LoveCTF{f1NdMyBesty} 
