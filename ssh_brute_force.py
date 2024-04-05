#!/usr/bin/python
#pip install paramiko
#ssh root@172.16.1.5 --> add the host to known_hosts file with the kali function
import paramiko
ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) # Auto Add the key to the known_hosts file

try:
  ssh.connect("172.16.1.5", username='root', password='root')
except paramiko.ssh_exception.AuthenticationException:
  print("Access failed")
else:
  print("Connected")
  stdin, stdout, stderr = ssh.exec_command('ls') #here you can type the commands you want to execute, this will bring the stdout in list format
  for line in stdout.readlines():
    print(line).strip() # strip() will remove the line breaks


ssh.close()
