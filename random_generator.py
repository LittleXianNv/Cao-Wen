import random

arr = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',',','.','\n']
res = ""
c = ""
r = 0

for i in range(0,500):
	num = random.randint(0,9)
	counter = 0
	while num > counter:
		r = random.randint(0,54)
		c = arr[r]
		res += c
		counter += 1
	res += ' '

print(res) 

