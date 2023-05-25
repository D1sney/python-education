row = 11
t=0
for r in range(0,row,2):
    a=int(row/2)
    for x in range((row-t-1)-a):
        print(' ', end='')
    
    for c in range(r+1):
        print(f'*', end='')
    
    t+=1    
    print('')