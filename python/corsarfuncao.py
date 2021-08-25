def funcao(n):

    if n == 1:
        return n
    else: 
        return n*funcao(n-1)

print(funcao(19))