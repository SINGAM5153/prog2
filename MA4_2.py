#!/usr/bin/env python3
""" 
checked by : 
checked on : 

"""
import matplotlib as plt			
from time import perf_counter as pc
from integer import Integer

	

def compare(n):
	f = Integer(n)
	
	start_cpp = pc()
	fib_cpp = f.fib(n)
	time_cpp = pc()-start_cpp
	
	
	start_py = pc()
	fib_py = f.fib_py(n)
	time_py = pc()-start_py
	
	plt.plot(n,time_cpp,'ro',n,time_py,'b^')

	print(f'Value of {f.get()} fibonacci is {fib_cpp} \t time for C++ fib = {time_cpp} \t time for python = {time_py} \n')
	return [time_cpp,time_py]
	
def main():
	times = []
	xl=[]
	pl=[]
	lt=[]
	for i in range(30,37):
		lt.append(i)
	for i in lt:
		cp=compare(i)
		xl.append(cp[0])
		pl.append(cp[1])
		times.append(cp)

	plt.pyplot(xl,lt)
	plt.pyplot(pl,lt)
	print('end')
	
	plt.savefig('cpp_vs_py.png')



if __name__ == '__main__':
	main()


'''

Value of 30 fibonacci is 832040          time for C++ fib = 0.016971047967672348         time for python = 0.5625622300431132

Value of 31 fibonacci is 1346269         time for C++ fib = 0.024896234972402453         time for python = 0.9051827479852363

Value of 32 fibonacci is 2178309         time for C++ fib = 0.03830707201268524          time for python = 1.458550531999208

Value of 33 fibonacci is 3524578         time for C++ fib = 0.06148823001421988          time for python = 2.350955677917227

Value of 34 fibonacci is 5702887         time for C++ fib = 0.09953848097939044          time for python = 3.8027884350158274

Value of 35 fibonacci is 9227465         time for C++ fib = 0.16246870998293161          time for python = 6.143728667986579

Value of 36 fibonacci is 14930352        time for C++ fib = 0.25748513999860734          time for python = 9.933431852026843

Value of 37 fibonacci is 24157817        time for C++ fib = 3.0900118872523308e-06       time for python = 16.299226878909394

Value of 38 fibonacci is 39088169        time for C++ fib = 3.0420487746596336e-06       time for python = 26.375115173053928
'''
