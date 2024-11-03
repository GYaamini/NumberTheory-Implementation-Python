"""
Factorization of Nth Order Degree Equation
without using python in-built functions
"""

## function to return factorisation values
def factorise(x,n,lval):
    return x-(n*lval)

## function getVal to return root
def getVal(lval):
    global val
    val=[]
    for n in range(1,10):
        val=[1,0]
        for x in lval:
            val.append(factorise(x,n,val[-1])) ## positive values
        if val[-1]==0:
            return n
        else:
            val=[1,0]
            for x in lval:
                val.append(factorise(x,-n,val[-1])) ## negative values
            if val[-1]==0:
                return -n

if __name__ == "__main__":      
    ## take input from user
    l=list(int(num) for num in input("Enter cubic equation coefficients with constant :").strip().split())
    print(l)

    ## code block to generate tupled factorised values
    factorised=[] ##list to contain all the factorised tuple values
    lval=l
    while len(lval)!=1:
        t=[1,0]
        t[1]=getVal(lval)## create tuple
        if t[1]==None:
            factorised.append(tuple(lval))
            break
        else:
            t=tuple(t)
            lval.clear()
            factorised.append(t) ## add tuples to a list
            for ele in val[2:-1]:
                lval.append(ele) ##new set of coefficients to be factorised

    print("Factorised value is : ")
    for ele in factorised: print(ele,end="")