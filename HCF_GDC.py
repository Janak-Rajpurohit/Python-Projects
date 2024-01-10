# hcf/ gdc of two numbers

def findhcf(m,n):
    cf=[]
    if m%n==0:                      ## hcf can be itself too
        print(f"HCF --> {n}") 
    elif n%m==0:
        print(f"HCF --> {m}")
    else:
        if m>n:
            for i in range(1,n):
                if m%i==0 and n%i==0:
                    cf.append(i)
            return max(cf)
        elif n>m:
            for i in range(1,m):
                if m%i==0 and n%i==0:
                    cf.append(i)
            return max(cf)

if __name__=="__main__":
    m=int(input("Enter 1st number >>> "))
    n=int(input("Enter 2nd number >>> "))
    print(f"HCF --> {findhcf(m,n)}")
    