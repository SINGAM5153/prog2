#!/usr/bin/env python3

from integer import Integer

def main():
	f = Integer(30)
	lt=[i for i in range(30,38)]
	for i in lt:
		print(f.get())
		f.set(i)
		r=f.fib()
		print(f.get())


if __name__ == '__main__':
	main()