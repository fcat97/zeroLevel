!# /usr/bash

mkdir -p result

for f in ./*.png; do
	convert "$f" -quality 1% -flatten "./result/$f.jpg"
	ls "$f"
done
