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
