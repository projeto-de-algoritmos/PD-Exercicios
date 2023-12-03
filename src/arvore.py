def knapsack(W, wt, val, n):
    K = [[0 for w in range(W + 1)]
            for i in range(n + 1)]
                
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
    
    return K[n][W]

G = int(input())  # Quantidade de testes

for i in range(G):
    print ("Galho %d:" % (i+1))
    P = int(input())  # Quantidade de itens
    W = int(input())  # Capacidade da mochila
    E = []  # Inicializando a lista E
    PC = []  # Inicializando a lista PC
    for _ in range(P):
        e, pc = map(int, input().split())  # Lendo o peso e o valor de cada item
        E.append(e)
        PC.append(pc)

        # Chamar a função knapsack
    result = knapsack(W, PC, E, P)
    print("Numero total de enfeites: %d\n" % result)
