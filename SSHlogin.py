#!/usr/bin/python3
import pexpect

PROMPT=['# ','>>> ','> ','\$ ']

def send_command(argchild,execute):
	argchild.sendline(execute)
	argchild.expect(PROMPT)
	print(argchild.before)

def connect(host,user,password):
	question="Are you sure you want to continue connecting"
	command='ssh '+user+'@'+host
	child=pexpect.spawn(command)
	ret=child.expect([pexpect.TIMEOUT,question,'[P|p]assword: '])
	if ret==0:
		print("[-]Error Connecting!")
		return
	else:
		child.sendline('yes')
		ret=child.expect([pexpect.TIMEOUT,'[P|p]assword: '])
		if ret==0:
			print("[-]Error Connecting!")
			return	
	child.sendline(password)
	child.expect(PROMPT)
	return child

def main():
	host=input("Enter host ip-address: ")
	user=input("Enter SSH username: ")
	password=input("Enter SSH login password: ")
	child=connect(host,user,password)
	send_command(child,'cat etc/shadow | grep root;ps')


main()
