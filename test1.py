import random_generator.py
import subprocess
import shlex
import os
import sys
import config
import distributed_grep

def test1():
    remoteRes = {}
    argv = ["distributed_grep.py","GNU"]
    remoteRes = distributed_grep.distributedGrep(agrv)
    
