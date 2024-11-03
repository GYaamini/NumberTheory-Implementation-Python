"""
Factorization of Cubic Equation
without using python in-built fuctions
"""

## function to return factorisation values
def factorise(x,n,lval):
    return x-(n*lval)

## function to return root
def getVal():
    global val
    val=[]
    for n in range(1,10):
        val=[1,0]
        for x in l:
            val.append(factorise(x,n,val[-1])) ## positive values
        if val[-1]==0:
            return n
        else:
            val=[1,0]
            for x in l:
                val.append(factorise(x,-n,val[-1])) ## negative values
            if val[-1]==0:
                return -n
            
if __name__ == "__main__":
    ## take input from user
    l=list(int(num) for num in input("Enter cubic equation coefficients with constant :").strip().split())
    print(l)

    val[1]=getVal()

    if val[1] is None:
        print("Can't be factorised")
    else:
        print(f"Factorised value is : \n{val[0],val[1]}{val[2],val[3],val[4]}")