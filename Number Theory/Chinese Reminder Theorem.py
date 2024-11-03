"""
Chinese Reminder Theorem 
without using python in-built functions
"""

## calculate gcd by Euclidean algorithm
def gcd(a,n):
    n1=a if a>n else n
    n2=a if a<n else n
    while(n1%n2!=0):
        rem=n1%n2
        q=n1//n2
        gcdDict[rem]=[n1,n2,q]
        n1=n2
        n2=rem

## find() recursive function to find yi and q values such that Mi.yi+n.q=c ('c' is gcd of 'Mi' and 'ni')
def find(index,i):
    i1=index[0]
    i2=index[1]
    q=-(index[2])
    if i1 in k:
        find(gcdDict[i1],i)
    else:
        if i1==a:
            dict[a]+=i
        else:
            dict[n]+=i
    if i2 in k:
        i=i*q
        find(gcdDict[i2],i)
    else:
        q=q*i
        if i2==a:
            dict[a]+=q
        else:
            dict[n]+=q
    if i1==a and i2==n:
        return     

## if negative congruence, calculate the positive congruence for (mod n)
def posCongruence(con,mod):
    if con>0:
        return con
    else:
        return posCongruence(con+mod,mod)

if __name__ == "__main__":
    ## take input from user
    num=int(input("Enter the number of congruences for Chinese Reinder Theorem: "))
    congruences={}
    for i in range(1,num+1):
        congruences[i]=list(int(num) for num in input("Enter a,n values (space divided input) for 'x congruent to a (mod n)' :").strip().split())

    ## calculate 'm' and 'Mi' values
    m=1
    M=[]
    ni=[]
    ai=[]
    for key,item in congruences.items():
        m*=item[-1]
    print(f"Value of m : {m}")
    for key,item in congruences.items():
        M.append(int(m/item[-1]))
        ni.append(item[-1])
        ai.append(item[0])  

    ## check whether Chinese Reminder Theorem can be applied
    global flag
    flag=1
    l=[]
    for key,item in congruences.items():
        l.append(item[-1])
    index=0
    for i in l[:-1]:
        for j in l[index+1:]:
            gcdDict={} ## dictionary storing reminder as key and dividend,divisor,quotient as values
            gcd(i,j)
            k=list(gcdDict.keys())
            if len(k) == 0:
                print(f"Chinese Reminder theorem not possible since GCD of {i} and {j} is not 1")
                flag=0
                break
        if flag==0:
            break
        index+=1

    ## if Chinese Reminder Theorem is possible
    if flag:
        ## calculate 'yi' values
        y=[]
        for i in range(0,num):
            gcdDict={} ## dictionary storing reminder as key and dividend,divisor,quotient as values
            gcd(M[i],ni[i])
            k=list(gcdDict.keys())
            a=M[i]
            n=ni[i]
            dict={a:0,n:0} ## dictionary holding a,n as keys and x,q as their respective values
            find(gcdDict[k[-1]],1)
            if list(gcdDict.keys())[-1] != 1:
                print("Finding inverse/value of 'b' not possible")
                break
            else:
                y.append(dict[a])
        print(f"Inverse values : {y}\n")


        ## calculate x   
        con=0
        for i in range(0,num):
            con+=(ai[i]*M[i]*y[i])
        if con>0:
            print(f"x is congruent to {con} (mod {m})\n")
        else:
            print(f"x is congruent to {posCongruence(con,m)} (mod {m})\n")
        
        ## Verification
        for i in range(0,num):
            gcdDict={}
            gcd(con,ni[i])
            k=list(gcdDict.keys())
            if k[0]<0:
                print(f"{i+1}. {con} mod {ni[i]} = {gcdDict[k[0]][0]}")
            else:
                print(f"{i+1}. {con} mod {ni[i]} = {k[0]}")