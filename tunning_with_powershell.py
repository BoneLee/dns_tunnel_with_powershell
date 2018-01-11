# -*- coding: utf-8 -*-
import subprocess
import binascii
import time
 
def python_call_powershell(lines):
    try:
	args=[r"powershell.exe","-ExecutionPolicy","Unrestricted", r".\trans_trunk.ps1"] + lines
        p=subprocess.Popen(args, stdout=subprocess.PIPE)
        dt=p.stdout.read()
        return dt
    except Exception,e:
        print e
    return False


def pingpong():
    while True:
        number = long(time.time())
        print python_call_powershell(["pingpong-%d" % number])
        time.sleep(2)


def read_bin_file():
    with open("data_to_transfer/office_file_18KB.docx", "rb") as f:
	binary_value = f.read()
	line=binascii.b2a_hex(binary_value) 
	#print binary_value
	#print line
	lines = []
        max_len = 16
	while len(line) > max_len:
	    data = line[:max_len]
	    lines.append('"'+data+'"')
	    line = line[max_len:]
        assert len(line)>=0
	if len(line)>0:
	    lines.append('"'+line+'"')
	max_cnt = 256
	while len(lines) > max_cnt:
	    print lines[:max_cnt]
            print python_call_powershell(lines[:max_cnt])
	    lines = lines[max_cnt:]
	print lines
        print python_call_powershell(lines)


def read_txt_file():
    with open("data_to_transfer/cmd.txt") as f:
	lines = []
        for line in f:
	    #line = line.strip()
	    #print line
	    max_len = 16
	    while len(line) > max_len:
	        data = line[:max_len]
	        lines.append('"'+data+'"')
		line = line[max_len:]
            assert len(line)>=0
	    if len(line)>0:
	        lines.append('"'+line+'"')
	max_cnt = 256
	while len(lines) > max_cnt:
	    print lines[:max_cnt]
            print python_call_powershell(lines[:max_cnt])
	    lines = lines[max_cnt:]
	print lines
        print python_call_powershell(lines)



if __name__=="__main__":
    read_txt_file()
    #read_bin_file()
    #pingpong()
