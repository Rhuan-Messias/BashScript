#include <stdio.h>
#include <netdb.h> 
#include <arpa/inet.h>

//man gethostbyname 
//the resolver will get a host dns and make it an ip address
//using this C program, it is 9x faster than host kali-linux's function

int main (int argc, char *argv[]) {

	if (argc <=1) {
		printf("Example: ./DnsResolver www.google.com\n");
		return 0;
	} else {

		struct hostent *target = gethostbyname(argv[1]);
		
		if(target == NULL) {
			printf("Something went wrong !!!\n");
		}else {

			printf("IP: %s\n",inet_ntoa(*((struct in_addr *)target->h_addr)));
			return 0;
		}
	}
}
