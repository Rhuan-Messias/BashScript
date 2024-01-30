#include <stdio.h> 
#include <sys/socket.h>
#include <netdb.h>

int main(void) {
	
	int mysocket;
	int conect;

	struct sockaddr_in target;

	mysocket = socket(AF_INET,SOCK_STREAM,0);
	target.sin_family = AF_INET;
	target.sin_port = htons(80);
	target.sin_addr.s_addr = inet_addr("192.168.1.1");

	conect = connect(mysocket, (struct sockaddr *)&alvo, sizeoff alvo);

	if(conect == 0){
		printf("Port is open! \n");
		close(mysocket);
		close(conect);
	} else {
		printf("Port is closed! \n")
	}
}
