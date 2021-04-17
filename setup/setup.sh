#!/bin/dash

frage_ja_nein() {
	local retval
	while [ "$retval" != "j" -a "$retval" != "n" ]; do read -p "$1 (j/n) " retval; done
	echo "$retval"
} 

user=$(whoami)
if [ "$user" != "root" ]
then
	echo "Du brauchst root-Rechte, um weiterzufahren."
	exit 1;
fi

printf "\n> Installiere packages via apt install... " && sleep 2 && apt install -y $(cat packages.list) || { echo "Fehler." && exit 1; } && echo "" && echo "Erfolgreich"

printf "\n> Installiere python Pakete via pip3... " && sleep 2 && pip3 install $(cat pip.list) || { echo "Fehler." && exit 1; } && echo "" && echo "Erfolgreich"

[ "$(frage_ja_nein "> Bot ausführen?")" = "j" ] && { python3 ../main.py; } || echo "Und off..." 
