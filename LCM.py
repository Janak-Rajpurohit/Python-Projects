## finding lcm of two numbers

def findlcm(m,n):
    cf=[]
    if  m==1 or n==1:
        return 1                     #### empty list for common factors then we will take smallest one out of it 
    elif m>n:
        for i in range(2,n):      ## not started from 1 becoz it is divisible with all so answer always be 1 
            if m%i==0 and n%i==0:
                cf.append(i)
        return min(cf)
    elif n>m:
        for i in range(2,m):
            if m%i==0 and n%i==0:
                cf.append(i)
        return min(cf)

if __name__=="__main__":
    m=int(input("Enter 1st number >>> "))
    n=int(input("Enter 2nd wnumber >>> "))
    print(f"LCM --> {findlcm(m,n)}")
