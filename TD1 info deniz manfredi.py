def solve1(n):
    nombre=2**n
    res=sum([int(c) for c in str(nombre)]
    return res

assert solve1(15)==26
print (solve1(1000))

def solve2():
    fichier=open('p022_names.text','r')
    texte=fichier.read()
    liste=texte.split(",")
    l=sorted(liste)
    #print(l)
    for i in range(len(l)):
        somme=0
        for x in l[i][1:,-1]:
            somme+=ord(x)-64
        l[i]=somme*(i+1)
    return sum(l)

print(solve2())

def inv(n):
    miroir=int(str(n)[::-1])
    return miroir

assert inv(432)==234



def solve3(n):
    i=0
    j=1
    k=0
    while k<=n:
        while j<=50:
            if inv(k)+k==inv(k+inv(k)):
                i+=1
                k+=1
            else:
                j+=1
                k+=inv(k)
    return i
                
print(solve3(100000))     
#Euler m'indique que mon résultat est faux    