#!/usr/bin/python
#pip install paramiko
import paramiko
ssh = paramiko.SSHClient()
ssh.connect("172.16.1.5", username='root', password='root')

stdin, stdout, stderr = ssh.exec_command('id') #here you can type the commands you want to execute
print(stdout)
ssh.close()
