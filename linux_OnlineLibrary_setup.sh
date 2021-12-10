#/bin/bash
pip install -r requirements.txt
cd root
pyinstaller --add-data "books.txt;." --add-data "requests.txt;." --add-data "bg.jpg;." -n "Online Library" --distpath output --onefile gui.py
cd output
chmod +x ./Online\ Library
cp ./Online\ Library /usr/local/bin/Online\ Library

