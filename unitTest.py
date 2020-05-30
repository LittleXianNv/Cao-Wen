
import subprocess
import shlex
import os
import sys
import config
import distributed_grep
import unittest
import ast

class testGrep(unittest.TestCase):
    def test1(self):
        remoteRes = {}
        argument = []
        argument = ["distributed_grep.py","GNU"]
        remoteRes = distributed_grep.distributedGrep(argument)
        f = open("test/test1.txt", "r")
        groundTruth = f.read()
        groundTruth =  ast.literal_eval(groundTruth)
        f.close()
        for key in config.ip_list:
            self.assertEqual(groundTruth[key],remoteRes[key])

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


if __name__ == '__main__':
    unittest.main()


