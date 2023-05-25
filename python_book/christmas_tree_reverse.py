row = 11
t=0
for r in range(0,row,2):
    a=int(row/2-0.5)
    for x in range(t):
        print(' ', end='')
    
    for c in range(row,r,-1):
        print(f'*', end='')
    
    t+=1    
    print('')