# Contacts App
# James Skon, Kenyon College 2022

all:	PutHTML 

PutHTML:
	cp contactApp.html ./var/www/html/contactPy/
	cp contactApp.js ./var/www/html/contactPy/
	cp contactApp.css ./var/www/html/contactPy/


	echo "Current contents of your HTML directory: "
	ls -l ./var/www/html/contactPy