//Script in C 
#include <stdio.h>

int main (void){
	int port;
	char ip[16];

	printf("Messias\n");
	
	printf("Type the IP: ");
	scanf("%s",&ip);

	printf("Type the port number: ");
	scanf("%i",&port);

	printf("Scanning Host: %s on port %i \n", ip, port);

	return 0; 
}
