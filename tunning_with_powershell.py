# -*- coding: utf-8 -*-
import subprocess
 
def python_call_powershell(lines):
    try:
	args=[r"powershell.exe","-ExecutionPolicy","Unrestricted", r".\trans_trunk.ps1"] + lines
        p=subprocess.Popen(args, stdout=subprocess.PIPE)
        dt=p.stdout.read()
        return dt
    except Exception,e:
        print e
    return False


if __name__=="__main__":
    with open("data.txt") as f:
	lines = []
        for line in f:
	    lines.append('"'+line.strip()+'"')
	print lines
        print python_call_powershell(lines)
