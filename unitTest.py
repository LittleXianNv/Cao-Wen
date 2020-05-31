
import subprocess
import shlex
import os
import sys
import config
import distributed_grep
import unittest
import ast

class testGrep(unittest.TestCase):
    # test 1 with grep command grep "GNU"
    def test1(self):
        remoteRes = {}
        argument = []
        argument = ["distributed_grep.py","GNU"] #mimic command line arguments
        remoteRes = distributed_grep.distributedGrep(argument) #get remot results from server
        f = open("test/test1.txt", "r")
        groundTruth = f.read() #get ground truth from our test files in test folder
        groundTruth =  ast.literal_eval(groundTruth)
        f.close()
        for key in config.ip_list:
            self.assertEqual(groundTruth[key],remoteRes[key])

    # test 2 with grep command grep -i "license"
    def test2(self):
        remoteRes = {}
        argument = []
        argument = ["distributed_grep.py","-i","license"]
        remoteRes = distributed_grep.distributedGrep(argument)
        f = open("test/test2.txt", "r")
        groundTruth = f.read()
        groundTruth =  ast.literal_eval(groundTruth)
        f.close()
        for key in config.ip_list:
            self.assertEqual(groundTruth[key],remoteRes[key])

    # test 3 with grep command grep -c "that"
    def test3(self):
        remoteRes = {}
        argument = []
        argument = ["distributed_grep.py","-c","that"]
        remoteRes = distributed_grep.distributedGrep(argument)
        f = open("test/test3.txt", "r")
        groundTruth = f.read()
        groundTruth =  ast.literal_eval(groundTruth)
        f.close()
        for key in config.ip_list:
            self.assertEqual(groundTruth[key],remoteRes[key])

    # test 4 with grep command grep -w "License"
    def test4(self):
        remoteRes = {}
        argument = []
        argument = ["distributed_grep.py","-w","License"]
        remoteRes = distributed_grep.distributedGrep(argument)
        f = open("test/test4.txt", "r")
        groundTruth = f.read()
        groundTruth =  ast.literal_eval(groundTruth)
        f.close()
        for key in config.ip_list:
            self.assertEqual(groundTruth[key],remoteRes[key])

    # test 5 with grep command grep -o "General"
    def test5(self):
        remoteRes = {}
        argument = []
        argument = ["distributed_grep.py","-o","General"]
        remoteRes = distributed_grep.distributedGrep(argument)
        f = open("test/test5.txt", "r")
        groundTruth = f.read()
        groundTruth =  ast.literal_eval(groundTruth)
        f.close()
        for key in config.ip_list:
            self.assertEqual(groundTruth[key],remoteRes[key])

    # test 6 with grep command grep "^GNU"
    def test6(self):
        remoteRes = {}
        argument = []
        argument = ["distributed_grep.py","^GNU"]
        remoteRes = distributed_grep.distributedGrep(argument)
        f = open("test/test6.txt", "r")
        groundTruth = f.read()
        groundTruth =  ast.literal_eval(groundTruth)
        f.close()
        for key in config.ip_list:
            self.assertEqual(groundTruth[key],remoteRes[key])

    # test 7 with grep command grep "and$"
    def test7(self):
        remoteRes = {}
        argument = []
        argument = ["distributed_grep.py","and$"]
        remoteRes = distributed_grep.distributedGrep(argument)
        f = open("test/test7.txt", "r")
        groundTruth = f.read()
        groundTruth =  ast.literal_eval(groundTruth)
        f.close()
        for key in config.ip_list:
            self.assertEqual(groundTruth[key],remoteRes[key])

    # test 8 with grep command grep "..cept"
    def test8(self):
        remoteRes = {}
        argument = []
        argument = ["distributed_grep.py","..cept"]
        remoteRes = distributed_grep.distributedGrep(argument)
        f = open("test/test8.txt", "r")
        groundTruth = f.read()
        groundTruth =  ast.literal_eval(groundTruth)
        f.close()
        for key in config.ip_list:
            self.assertEqual(groundTruth[key],remoteRes[key])

    # test9 with grep command grep "t[wo]o"
    def test9(self):
        remoteRes = {}
        argument = []
        argument = ["distributed_grep.py","t[wo]o"]
        remoteRes = distributed_grep.distributedGrep(argument)
        f = open("test/test9.txt", "r")
        groundTruth = f.read()
        groundTruth =  ast.literal_eval(groundTruth)
        f.close()
        for key in config.ip_list:
            self.assertEqual(groundTruth[key],remoteRes[key])

    def test10(self):
        # manuually change the last ip of config file to a invalid address and corresponds to invalid log file

        remoteRes = {}
        argument = []
        argument = ["distributed_grep.py","^GNU"]
        
        remoteRes = distributed_grep.distributedGrep(argument)
        f = open("test/test10.txt", "r")
        groundTruth = f.read()
        groundTruth =  ast.literal_eval(groundTruth)
        f.close()
        
        for key in config.ip_list:
            if key in groundTruth.keys():
                self.assertEqual(groundTruth[key],remoteRes[key])
            else:
                continue



if __name__ == '__main__':
    unittest.main()


