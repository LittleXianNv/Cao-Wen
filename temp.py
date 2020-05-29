import subprocess
import shlex
import os
import sys

#ip_list = ['52.60.77.126', '35.182.255.151', '35.183.208.52', '35.183.29.42', '35.183.30.234','99.79.10.67']
ip_list = ['52.60.77.126', '35.182.255.151','35.183.208.52']
log_file = {'52.60.77.126':'machine_1_log.txt','35.182.255.151':'machine_2_log.txt','35.183.208.52':'machine_3_log.txt'}
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

subprocesses = {}
argv = sys.argv
num = len(argv)

for ip in ip_list:
    if num == 2:
        half_command = argv[1]+" "+log_file[ip]
    else:
        half_command = argv[1] +" "+ argv[2]+" "+log_file[ip]
    if ip != local_ip:
        command = "ssh -i /home/ec2-user/summer.pem " + "ec2-user@" + ip + " grep " + half_command
    else:
        command = "grep " + half_command
    print(command)
    command = shlex.split(command)
    process = subprocess.Popen(command,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    subprocesses[ip] = process
    c += 1

for key in subprocesses:
    stdout, stderr = subprocesses[key].communicate()
    result = stdout.rstrip()
    print("Server ip: "+key +" Log file: "+log_file[key]+"\n" + result+'\n')

