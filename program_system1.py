import os

if os.name == "nt":
 command = "systeminfo"
else:
 command = "cat /etc/issue"
os.system(command)