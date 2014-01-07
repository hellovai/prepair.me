# lists=[[4, 10, 15, 24, 26],[0, 9, 12, 20],[5, 18, 22, 30]]
import sys
class MyIterator:
	data=[]
	pointersMin=[]
	def __init__(self,lists):
		self.data=lists
		for i in xrange(len(lists)):
			self.pointersMin+=[0]
	def nextMin(self):
		mlist,mvalue=-1,sys.maxint
		for i in xrange(len(self.data)):
			if(self.pointersMin[i]==len(self.data[i])):
				continue
			if(self.data[i][self.pointersMin[i]]<mvalue):
				mlist=i
				mvalue=self.data[i][self.pointersMin[i]]
		self.pointersMin[mlist]+=1
		if(mlist==-1):
			return None,None
		return mvalue,mlist

if __name__ == "__main__":
    lists = []
    x = int(raw_input())
    for i in xrange(0,x):
        y = raw_input().split(' ')
        tempList = [0] * int(y[0])
        for j in xrange(0,len(tempList)):
            tempList[j] = int(y[1+j])
        lists.append(tempList)
    # print lists
    it=MyIterator(lists)
    val=[]
    lids=[]
    m,lid=it.nextMin()
    while(m!=None):
        # print m,lid
        lids+=[lid]
        val+=[m]
        m,lid=it.nextMin()
    
    seqsize=len(lists)
    res=(-sys.maxint,sys.maxint)
    while(res[0]==(-sys.maxint)):
        for i in xrange(len(lids)-seqsize+1):
            seq=lids[i:(i+seqsize)]
            mval=val[i:(i+seqsize)]
            if(len(set(seq))==len(lists)):
                if((mval[-1]-mval[0])<(res[1]-res[0])):
                    res=(mval[0],mval[-1])
        seqsize+=1
    print res[0], res[1]