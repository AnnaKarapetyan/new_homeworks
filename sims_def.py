def full(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i][j]==' ':
                return False
    return True
def mult(a,b):
    c=[]
    for i in range(len(a)):
        c.append(b[a[i]-1])
    return c
def riv(a):
    b=[]
    for i in range(1,len(a)+1):
        b.append(a.index(i)+1)
    return b
def cascade(a,arr):
    i=0
    l=len(a)
    while i!=l:
        if a[i]==i+1:
            i+=1
        else:
            if arr[i][a[i]-1]==' ':
                if(i<a[i]-1):
                    arr[i][a[i]-1]=a
                break
            else:
                a=mult(riv(arr[i][a[i]-1]),a)
                i+=1
    return arr
def couple(l):
    newl=[]
    for i in range(len(l)):
        for j in range(i,len(l)):
            if mult(l[i],l[j]) not in l:
                newl.append(mult(l[i],l[j]))
            if mult(l[j],l[i]) not in l:
                newl.append(mult(l[j],l[i]))
    return newl
def sims(arr,bazm):
    for i in range(len(bazm)):
        arr=cascade(bazm[i],arr)
    while True:
        if full(arr):
            break
        tw=couple(bazm)
        if len(tw)==0:
            break
        for i in tw:
            arr=cascade(i,arr)
            bazm.append(i)
    return arr