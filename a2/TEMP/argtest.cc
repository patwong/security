#include <iostream>

int main(int argc, char* argv[]) {
	int c = 1;
	if(argc > 1) {
		std::cout << "number of args: " << argc << std::endl;
		while(c < argc) {
			std::cout << argv[c] << " ";
			c++;
		}
		std::cout << std::endl;
	} else {
		std::cout << "number of args: " << argc << std::endl
				<< "no value passed\n";
	}
/*	std::cout << "number of args: " << argc << std::endl;
	std::cout << argv[0] << std::endl;
	std::cout << argv[1] << std::endl;
*/
	return 0;
}
