import pikepdf
from termcolor import colored

pdf_file = input("enter the name of pdf : ")
file = open("wordlist.txt")


for password in file:
	try:
		with pikepdf.open(pdf_file,password.strip()) as pdf:
			print(colored("password found: {}".format(password), 'green'))
			break
	except:
		print(colored("Trying password: {}".format(password),'red'))
		continue
