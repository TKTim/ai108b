def f(x):
    return x*x


dx = 0.001

def diff(f, x):
    df = f(x+dx)-f(x)
    print('df = f({}+{})-f({}) : {}={}-{}'.format(x,dx,x,df,f(x+dx),f(x)))
    return df/dx

print('diff(f,2)=', diff(f, 2))
