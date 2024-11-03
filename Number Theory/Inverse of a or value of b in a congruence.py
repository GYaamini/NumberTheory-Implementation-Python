"""
Inverse of a or value of b in the form of : ab congruent to m (mod m)
without using python in-built functions
"""

## calculate gcd by Euclidean algorithm
def gcd(a,n):
    n1=a if a>n else n
    n2=a if a<n else n
    gcdDict={} ## dictionary storing reminder as key and dividend,divisor,quotient as values
    while(n1%n2!=0):
        rem=n1%n2
        q=n1//n2
        gcdDict[rem]=[n1,n2,q]
        n1=n2
        n2=rem
    return gcdDict
## find() recursive function to find x and q values such that ax+nq=m ('m' is gcd of 'a' and 'n')
def find(index,i,dict):
    i1=index[0]
    i2=index[1]
    q=-(index[2])
    if i1 in k:
        find(gcdDict[i1],i,dict)
    else:
        if i1==a:
            dict[a]+=i
        else:
            dict[n]+=i
    if i2 in k:
        i=i*q
        find(gcdDict[i2],i,dict)
    else:
        q=q*i
        if i2==a:
            dict[a]+=q
        else:
            dict[n]+=q
    if i1==a and i2==n:
        return dict
    return dict
        
if __name__ == "__main__":
    ## take input from user
    a,n,m=(int(num) for num in input("Enter a,n,m values (space divided input) for 'a*b congruent to m (mod n)' :").strip().split())
    
    ## invoke gcd function and display dictionary values as {reminder :[dividend,divisor,quotient]}
    gcdDict=gcd(a,n)
    print(gcdDict)
    
    k=list(gcdDict.keys())
    dict=find(gcdDict[k[-1]],1,dict={a:0,n:0})       ## dictionary holding a,n as keys and x,q as their respective values

    ## check whether a and n has m as gcd and print value of b/inverse of a suct that a*b congrunet to m for (mod n)
    if list(gcdDict.keys())[-1]!=m:
        print("Finding inverse/value of 'b' not possible")
    else:
        print(f"{m}=({a})({dict[a]})+({n})({dict[n]})")
        print(f"Value of b/inverse of a is : {dict[a]}")

    