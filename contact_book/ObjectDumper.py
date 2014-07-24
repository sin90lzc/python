import pickle as cp


class ObjectDumper():
	__fileName=""

	def __init__(self,fileName):
		self.__fileName=fileName

	def read(self):
		f = file(self.__fileName,"r")
		o=cp.load(f)
		f.close()
		return o

	def write(self,o):
		f = file(self.__fileName,"w")
		cp.dump(o,f)
		f.close()
