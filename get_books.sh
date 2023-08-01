#!/bin/bash
pdf_dir="`pwd`/pdfs"
file="book_urls.txt"
while read line; do
    echo "Downloading $line"
    wget -P "$pdf_dir" "$line"
done < "$file"