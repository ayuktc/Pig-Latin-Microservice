#!/bin/bash

help() {
    echo " pglatin.sh -w <word> "
    echo " -w word to be converted to piglatin"
    exit 1
}

send_request() {
local lword="$1"
    url=\'http://localhost:8080/translation/piglatin/json\'
    command="curl  --location --request POST ${url} --form 'words'=\"$lword\""
#    url --location --request POST 'http://127.0.0.1:8080/translation/piglatin' \
#--form 'words="abcd"'
    echo "Executing following command to get message: " "$command"
    /bin/sh -c "$command"
}



if [[ $# -le 0 || $# -gt 2 ]]; then
    help
    exit
fi


IFS=$'\t'
while [[ $# -gt 0 ]]; do
    key="$1"
    case $key in
        -w|--word)
        WORD="$2"
        if [[ -z $WORD ]]; then
            help
        fi
        send_request $WORD
        shift # shifts pass argument
        shift # shifts pass value
        exit 0
        ;;
     esac
done

