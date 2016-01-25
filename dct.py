import numpy as np


class DCT():
	"""docstring for DCT"""
	def __init__(self):
		self.T = []
		self.initT()

	def initT(self):
		tmpT = 0.5*np.ones([8,8])
		tmpT[0,:] *= np.sqrt(2)/2
		 
		for i in xrange(1, 8):
			piArange = np.arange(i,2*i*8,2*i)*np.pi/16
			#print np.cos(piArange)
			tmpT[i, :] *= np.cos(piArange)
		self.T = tmpT
		return self.T

	def dct(self, f):
		self.F = ((self.T).dot(f)).dot(self.T.transpose())
		return self.F

	def idct(self, F):
		self.f_hat = ((self.T.transpose()).dot(self.F)).dot(self.T)
		return self.f_hat

newDCT = DCT()

tmpf = np.random.rand(8, 8)

Fnew = newDCT.dct(tmpf)
fNew = newDCT.idct(Fnew)


print fNew - tmpf