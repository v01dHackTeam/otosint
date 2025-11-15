import os

GREEN = "\e[1;32m]"
RED = "\e[1;31m]"
RESET = "\e[1;0m]"

print("""
+-+-+-+-+-+-+-+ +-+-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+-+-+-+
|O|T|O|S|I|N|T| |F|R|A|M|E|W|O|R|K| |I|N|S|T|A|L|L|E|R|
+-+-+-+-+-+-+-+ +-+-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+-+-+-+

""")

os.system("apt update -y")

upgrade = input("You Want to Upgrade Y/n: ")
if upgrade == "Y":
	os.system("apt upgrade -y")
	
elif upgrade == "n" or "N":
	print("Ok, we continue...")
	
else:
	os.system("apt upgrade -y")
	
os.system("\n apt install whois dnsutils curl -y ")

os.system("cp otosint.py $PREFIX/bin/")
os.system("mv $PREFIX/bin/otosint.py $PREFIX/bin/otosint")
os.system("chmod +x $PREFIX/bin/otosint")

print(f"""{GREEN}
OSINT FRAMEWORK IS NOW INSTALLED!!!
{RESET}""")