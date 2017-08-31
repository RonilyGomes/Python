tabela = []
n1,n2 = 0,1

tabela.append(0)

for _ in range (10000):
    tabela.append(n2)
    n1,n2 = n2,n1+n2 
    
T = int(input())

for _ in range(T):
    n3 = int(input())
    print('Fib(%d) = %d' %(n3, tabela[n3]))