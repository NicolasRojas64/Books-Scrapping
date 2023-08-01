#!/bin/bash
#pdf_dir="`pwd`/pdfs/"
pdf_dir="/home/kali/Documents/Electiva3/pdfs/"
file="book_urls.txt"

while read url; do
	firefox -incognito &
	sleep 2
	xdotool key Ctrl+t
	sleep 2
	xdotool type "$url"
	xdotool key KP_Enter
	sleep 2
	xdotool key Home
	sleep 2
	xdotool type "$pdf_dir"
	sleep 5
	xdotool key KP_Enter
	xdotool key Ctrl+w
	xdotool key Ctrl+w 
done < $file