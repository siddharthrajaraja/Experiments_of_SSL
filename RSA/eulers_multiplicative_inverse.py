import phi

def mul_inverse(a,n):
    return pow(a,phi.phi(n)-1)%n 
