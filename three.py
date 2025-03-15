#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import random


par = int(input())
print(par)
name = input("Insert Name:")
print(name)
measure = input("insert measure")
sred = 0
numb = 0

list = []

for i in range(60):
	ran =random.randint(0,par)
	list.append(ran)
	#time.sleep(1)
	sred += ran
	numb+=1


print(sred/numb)
