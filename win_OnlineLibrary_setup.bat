@echo off
pip install -r requirements.txt
cd root
pyinstaller --add-data "books.txt;." --add-data "requests.txt;." --add-data "gitupdate.py;." --add-data "bg.jpg;." --windowed --icon="icon1.ico" -n "Online Library" --distpath %~dp0 --onefile gui.py
