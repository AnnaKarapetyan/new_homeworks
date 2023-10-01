import pprint
import sims_def 

a=[[2,3,1],[1,2,3]]

l=3
arr=[]
for i in range(l):
    m=[]
    for j in range(l):
        if i!=j:
            m.append(' ')
        else:
            m.append('e')
    arr.append(m)
answer=sims_def.sims(arr,a)
for i in answer:
    print(i)

