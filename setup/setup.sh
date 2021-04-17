#!/bin/dash

skript_pfad=$(realpath $(dirname $0))

frage_ja_nein() {
	local retval
	while [ "$retval" != "j" -a "$retval" != "n" ]; do read -p "$1 (j/n) " retval; done
	echo "$retval"
}

frage_wert_oder_default() {
	local retval
	read -p "$1 (Standard: $2) " retval;
	if [ "$retval" = "" ]; then retval="$2"; fi
	echo "$retval"
}

user=$(whoami)
if [ "$user" != "root" ]
then
	echo "Du brauchst root-Rechte, um weiterzufahren."
	exit 1;
fi

#printf "\n> Installiere packages via apt install... " && sleep 2 && apt install -y $(cat packages.list) || { echo "Fehler." && exit 1; } && echo "" && echo "Erfolgreich"

#printf "\n> Installiere python Pakete via pip3... " && sleep 2 && pip3 install $(cat pip.list) || { echo "Fehler." && exit 1; } && echo "" && echo "Erfolgreich"

token="$(frage_wert_oder_default "> Access-Token für Telegram-Bot eingeben" "xxx")"

ls $skript_pfad/../.env 2> /dev/null > /dev/null || { echo "ACCESS_TOKEN=${token}" | tee -a > $skript_pfad/../.env; } && sed -i "s/ACCESS_TOKEN.*/ACCESS_TOKEN=${token}/g" $skript_pfad/../.env

[ "$(frage_ja_nein "> Bot ausführen?")" = "j" ] && { python3 $skript_pfad/../main.py; } || echo "Und off..." 
