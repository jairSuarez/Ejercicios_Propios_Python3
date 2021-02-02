def esPrimo(num):
    prim = False
    divs = 0
    for i in range(1,num+1):
        if(num%i==0): divs+=1
    if(divs==2): prim = True
    return prim

for x in range(100):
    if(esPrimo(x)==True): print(x)



    
        
    




