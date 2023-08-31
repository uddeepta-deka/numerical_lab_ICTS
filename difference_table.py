#this program makes a difference table from given entries of evenly spaced data

def diff_table(xlist, ylist):     
    n=len(ylist)
    h=xlist[1]-xlist[0]               #here h is the spacing of the entries
    f = [[0 for i in range(n)] 
        for j in range(n)]; 
    for i in range(n):
        f[i][0]=ylist[i]
    for i in range (1,n):
        for j in range (n-i):
            f[j][i]=((f[j+1][i-1]-f[j][i-1]))/(i*h)
            
    # Displaying the forward difference table 
    for i in range(n): 
        print(xlist[i], end = "\t"); 
        for j in range(n - i): 
            print(f[i][j], end = "\t"); 
        print(""); 
    return f

