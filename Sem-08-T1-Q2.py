def main():
    n = int(input("Digite um número : "))

    lista_a = letra_a(n)
    print(lista_a)
    lista_b = letra_b(n)
    print(lista_b)
    lista_c = letra_c(n)
    print(lista_c)
    lista_d = letra_d(n)
    print(lista_d)

def letra_a(n):
    lista_a = []
    for numero in range(n):
        lista_a.append(0)
    
    return(lista_a)
def letra_b(n):
    lista_b = []
    for numero in range(1, n+1):
        lista_b.append(numero)
    
    return(lista_b)
def letra_c(n):
    lista_c = []
    for numero in range(n):
        num = int(input(f'Digite o {numero+1}° número: '))
        lista_c.append(num)
    
    return(lista_c)
def letra_d(n):
    lista_d = []
    for numero in range(n):
        num = int(input(f'Digite o {numero+1}° número: '))
        lista_d.append(num)

    
    return(lista_d[::-1])
if __name__ == '__main__':
    main()