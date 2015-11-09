#include <stdio.h>

int main() {
	int i ;
	printf ("foobar%n\n", (int *) &i);
	printf ("i = %d\n", i);

	return 0;
}
