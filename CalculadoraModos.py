from operator import truediv

def DecimalToBase(n,p):
    if n == 0:
        return [0,0,0]
    nums = []
    while n:
        n, r = divmod(n,p)
        nums.append(r)
    while len(nums)<3:
        nums.append(0)
    return list(reversed(nums))
# print(DecimalToBase(3,4))

def calculadora_modos():
    c=340
    n=100
    p=3
    # lx=int(input('Ingrese largo'))
    # ly=int(input('Ingrese ancho'))
    # lz=int(input('Ingrese alto'))
    lx = 5
    ly = 5
    lz = 5
    l=[lx,ly,lz]
    
    # T=float(input('Ingrese tiempo de reverberación'))
    T=0.5
    V=lx*ly*lz
    fsch=2000*(T/V)**(1/2)
    
    valores=[]
    for i in range(n):
        valores.append(list(DecimalToBase(i,p)))
    Q1=[]
    for i in range(n):
        Q1.append(list(map(truediv,valores[i],l)))
    modos=[]
    for i in range(len(Q1)):
        frec = (c/2)*(((Q1[i][0])**2+(Q1[i][1])**2+(Q1[i][2])**2)**(1/2))
        if frec<fsch:
            modos.append(round(frec,1))
    return modos

print(calculadora_modos())
