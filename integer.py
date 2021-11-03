""" Python interface to the C++ Integer class """ 
"""
Student:SIVA SAI NAVEEN SINGAM
Mail:singamnaveen23@gmail.com
Reviewed by:sven-erik
Date reviewed:03/11/2021
"""
import ctypes
lib = ctypes.cdll.LoadLibrary('./libinteger.so')

class Integer(object):
	def __init__(self, val):
		lib.Integer_new.argtypes = [ctypes.c_int]
		lib.Integer_new.restype = ctypes.c_void_p
		lib.Integer_get.argtypes = [ctypes.c_void_p]
		lib.Integer_get.restype = ctypes.c_int
		lib.Integer_set.argtypes = [ctypes.c_void_p,ctypes.c_int]
		lib.Integer_delete.argtypes = [ctypes.c_void_p]

		lib.Integer_fib.argtypes = [ctypes.c_void_p,ctypes.c_int]
		lib.Integer_fib.restype = ctypes.c_int
		self.obj = lib.Integer_new(val)
		

	def get(self):
		return lib.Integer_get(self.obj)

	def set(self, val):
		lib.Integer_set(self.obj, val)
        
	def __del__(self):
		return lib.Integer_delete(self.obj)

	def fib(self,val):
		return lib.Integer_fib(self.obj,val)
	
	def fib_py(self,val):
		n = val
		if n<=1:
			return n
		else:
			return self.fib_py(n-1)+self.fib_py(n-2)

	
