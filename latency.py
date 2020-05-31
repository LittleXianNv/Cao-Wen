import subprocess
import shlex
import os
import sys
import config_latency
import time

def main():
    argv = sys.argv
    distributedGrep(argv)


def distributedGrep(argv):
    ip_list = config_latency.ip_list
    log_file = config_latency.log_file
    # get start time
    start = time.time()
    
    # first call a command to know the ip address of current server
    def get_local_ip():
        command1 = shlex.split("curl http://169.254.169.254/latest/meta-data/public-ipv4")
        process = subprocess.Popen(command1,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)

        stdout, stderr = process.communicate()
        return(stdout)

    local_ip = get_local_ip()


    subprocesses = {}

    num = len(argv)
    
    # we consider two different situations that there are 2 arguments or 3 arguments in total
    # first distingush argument than distingush server client
    # call grep commands
    for ip in ip_list:
        if num == 2:
            half_command = argv[1]+" "+log_file[ip]
        else:
            half_command = argv[1] +" "+ argv[2]+" "+log_file[ip]
        if ip != local_ip:
            command = "ssh -i /home/ec2-user/summer.pem " + "ec2-user@" + ip + " grep " + half_command
        else:
            command = "grep " + half_command
        command = shlex.split(command)
        process = subprocess.Popen(command,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)

        subprocesses[ip] = process
    

    resMap = {}
    sum = 0
    for key in subprocesses:
        stdout, stderr = subprocesses[key].communicate()
        stdout = stdout.splitlines()

        arr = []
        for i in stdout:
            sentence = log_file[key]+":"+i
            arr.append(sentence)

        display = arr
        for line in range(len(display)):
            print(display[line])

        stdout = '\n'.join(arr)
        resMap[key] = stdout
        #get finish time of each server
        end = time.time()
        #the sum of all server ending time and then calculate averages
        sum = sum +(end-start)

    print(sum/4.0)
    return resMap

if __name__ == '__main__':
    main()
