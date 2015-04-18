#!/bin/bash

function request() {
    curl -X $1 "http://coffee.camsctf.com/" -b "PHPSESSID=09u7imkuo315bo0s3o1h98a433" --header "Content-Type: application/coffee-pot-command;" -d "23"
}

request BREW
request WHEN
request PROPFIND
request GET

