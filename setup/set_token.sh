#!/bin/dash

skript_pfad=$(realpath $(dirname $0))

. $skript_pfad/src/input.sh

token="$(frage_wert_oder_default "> Access-Token für Telegram-Bot eingeben" "xxx")"

ls $skript_pfad/../.env 2> /dev/null > /dev/null || { echo "ACCESS_TOKEN=${token}" | tee -a > $skript_pfad/../.env; } && sed -i "s/ACCESS_TOKEN.*/ACCESS_TOKEN=${token}/g" $skript_pfad/../.env
