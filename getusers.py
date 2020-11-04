#!/usr/pkg/bin/python
# log into freeshell.org
# source https://www.cyberciti.biz/faq/python-execute-unix-linux-command-examples/
# remote off linux mint
import os
users = os.popen("who | awk '{print $1}'")

for n in users:
        print (n, len(n))
