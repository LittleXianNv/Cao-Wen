import subprocess
import shlex
import os
from threading import Timer
import sys
import config


def main():
    argv = sys.argv
    distributedGrep(argv)

def distributedGrep(argv):
    ip_list = config.ip_list
    log_file = config.log_file

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
            #subprocesses[ip].returncode

    resMap = {}
    for key in subprocesses:
        timer = Timer(5, process.kill)
        try:
            timer.start()
            stdout, stderr = subprocesses[key].communicate()
        finally:
            timer.cancel()
        returncode = subprocesses[key].returncode
        if returncode == 0:
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
        else:
            stderr = stderr.splitlines()
            print(stderr)
            continue



    return resMap

if __name__ == '__main__':
    main()


