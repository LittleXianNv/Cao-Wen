import subprocess
import shlex
import os
import sys

#ip_list = ['18.188.168.68', '3.21.171.93', '18.223.166.10', '18.223.98.92', '3.21.186.8']
ip_list = ['18.188.168.68', '3.21.171.93','18.223.166.10']
log_file = ['1.txt','1.txt','2.txt']
def get_local_ip():
    command1 = shlex.split("curl http://169.254.169.254/latest/meta-data/public-ipv4")
    process = subprocess.Popen(command1,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    
    stdout, stderr = process.communicate()
    return(stdout)

local_ip = get_local_ip()
print(local_ip)
c = 0

subprocesses = []
argv = sys.argv
for ip in ip_list:
    if ip != local_ip:
        command = "ssh -i /home/ec2-user/key/test-key-pair.pem " + "ec2-user@" + ip + " grep " + "-" + argv[1] +" "+ argv[2]+" "+ log_file[c]
    else:
        command = "grep " + "-" + argv[1] +" "+ argv[2]+" "+ log_file[c]
    print(command)
    command = shlex.split(command)
    process = subprocess.Popen(command,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    subprocesses.append(process)
    c += 1

for process in subprocesses:
    stdout, stderr = process.communicate()
    print(stdout)
