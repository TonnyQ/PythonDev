#!/usr/bin/env python3

age = 20
if age >= 18:
	print("You age is ",age)
	print("adult")
else:
	print("teenager")

age = 3
if age >= 18:
	print("adult")
elif age >= 6:
	print("teenager")
else:
	print("kid")

x = 7
if x: #x是非零、非空字符串、非空list等，判断为true，否则为false
	print("True")

birth = input("bitrh : ")
birth = int(birth)
if birth < 2000:
	print("00 forward")
else:
	print("00 last")

