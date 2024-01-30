#include <stdio.h>
#include <stdlib.h>

//Basic code showing how to execute commands with C language
//This code will show the open ports in your system
//you can try to open a apache2 server to see if it works :) 

int main (void) {
	printf("Open TCP Ports: ");
	system("netstat -nlpt");
	return 0;
}
