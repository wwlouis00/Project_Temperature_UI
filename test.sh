#!/bin/expect
set timeout 30
spawn ssh -l pi 192.168.50.238
expect "password:"
send "123\r"
interact

