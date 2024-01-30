#include <stdio.h> 
#include <sys/socket.h>
#include <netdb.h>
#include <arpa/inet.h>
#include <unistd.h>

int main(int argc, char *argv[]) {
	
	int mysocket;
	int conect;

	int port;
	int start = 0;
	int end = 65535;
	char *dst;
	dst = argv[1];

	struct sockaddr_in target;

	for(port=start; port<=end; port++){

		//printf("Port in testing: %d",port);

		mysocket = socket(AF_INET,SOCK_STREAM,0);
		target.sin_family = AF_INET;
		//target.sin_port = htons(port);
		target.sin_port = htons(21);
		target.sin_addr.s_addr = inet_addr(dst);

		conect = connect(mysocket, (struct sockaddr *)&target, sizeof target);

		if(conect == 0){
			printf(":) YOU ARE UNDER ATTACK :) YOU ARE UNDER ATTACK :) YOU ARE UNDER ATTACK:) \n" );
			//printf("Port %d - status [OPEN] \n",port);
			//close(mysocket);
			//close(conect);
		} else {
			//close(mysocket);
			//close(conect);
		}
	}
}
