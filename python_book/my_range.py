import math
def my_range(a,b=math.pi,c=1):
    if b == math.pi:
        b=a
        a=0
        return bange(a,b)
    else:
        return bange(a,b,c)


def bange(a,b,c=1):
    i=[a]
    x=a
    if a//1 != a/1 or b//1 != b/1 or c/1 != c//1:
        print('error')
        return
    if a==b:
        i = []
        return  i
    elif a>b and c<0:
        while i[-1]+c>b:
            x+=c
            i.append(x)
        return i
    elif a > b or c==0:
        print('error')
        return 
    elif a<b and c<0: 
        print('error')
        return
    while i[-1]+c < b:
    #while len(i)<b-a:
        
        x+=c
        i.append(x)
    return i

if __name__ =='__main__':
    print(my_range(5))  
    i = list(my_range(7))
    print(i)
    v = list(range(7))
    print(v)  
    