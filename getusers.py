# log into freeshell.org
#!/usr/pkg/bin/python
# source https://www.cyberciti.biz/faq/python-execute-unix-linux-command-examples/
import os
users = os.popen("who | awk '{print $1}'")

for n in users:
        print (n, len(n))
