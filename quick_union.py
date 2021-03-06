class QuickFindUF():
	def __init__(self,n,lst=None):
		self.n = n
		self.lst = lst
		self.lst = [None]*self.n
		for i in range(self.n):
			self.lst[i]=i

	def connected(self,p,q):
		return p == q

	def root(self,i):
		while(i != self.lst[i]):	
			i = self.lst[i]
		return i

	def union(self,p,q):
		self.lst[self.root(q)] = self.root(p)


def main():
	quf = QuickFindUF(10)
	quf.union(2,5)
	quf.union(1,8)
	quf.union(1,2)
	quf.union(0,8)
	quf.union(6,9)
	quf.union(1,5)
	quf.union(2,6)
	print(quf.lst)

if __name__ == "__main__":
	main()