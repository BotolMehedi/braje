#!system/bin/sh
pkg install root-repo -y
pkg install unstable-repo -y
pkg install x11-repo -y
pkg update && pkg upgrade -y
pkg install git python -y
termux-setup-storage -y
git clone https://github.com/botolmehedi/braje
cd braje
pip install --upgrade pip
pip install -r requirements.txt
clear
python braje.py
