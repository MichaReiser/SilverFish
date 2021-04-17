#!/bin/dash

skript_pfad=$(realpath $(dirname $0))

. $skript_pfad/src/input.sh

user=$(whoami)
if [ "$user" != "root" ]
then
	echo "Du brauchst root-Rechte, um weiterzufahren."
	exit 1;
fi

printf "\n> Installiere packages via apt install... " && sleep 2 && apt install -y $(cat $skript_pfad/packages.list) || { echo "Fehler." && exit 1; } && echo "" && echo "Erfolgreich"

printf "\n> Installiere python Pakete via pip3... " && sleep 2 && pip3 install $(cat $skript_pfad/pip.list) || { echo "Fehler." && exit 1; } && echo "" && echo "Erfolgreich"

sh $skript_pfad/set_token.sh

[ "$(frage_ja_nein "> Bot ausführen?")" = "j" ] && { python3 $skript_pfad/../main.py; } || echo "Und off..." 
