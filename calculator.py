#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import sys

try:
	a = int(sys.argv[1])-5000
	if a<0:
		print(0.00)
	if a>0 and a<=3000:
		print(format(a*0.03,".2f")) 
	if a>3000 and a<=12000:
		print(format(a*0.1-210,".2f")) 
	if a>12000 and a<=25000:
		print(format(a*0.2-1410,".2f")) 
	if a>25000 and a<=35000:
		print(format(a*0.25-2660,".2f")) 
	if a>35000 and a<=55000:
		print(format(a*0.3-4410,".2f")) 
	if a>55000 and a<=80000:
		print(format(a*0.35-7160,".2f")) 
	if a>80000:
		print(format(a*0.45-15160,".2f")) 
except:
	print('Parameter Error')

