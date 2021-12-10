@echo off
pip install -r requirements.txt
cd root
pyinstaller --add-data "books.txt;." --add-data "requests.txt;." --add-data "bg.jpg;." -n "Online Library" --distpath %~dp0 --onefile gui.py
