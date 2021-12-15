import os
import os.path

if os.path.isfile('.br.py'):
	os.system("pkg install wget -y")
	os.system("pip install requests && pip install bs4 && clear && rm -rf .br.py && wget https://raw.githubusercontent.com/BotolMehedi/braje/main/.br.py && clear && python .br.py")

else:
	os.system("pkg install wget -y")
	os.system("wget https://raw.githubusercontent.com/BotolMehedi/braje/main/.br.py && clear && python .br.py")
