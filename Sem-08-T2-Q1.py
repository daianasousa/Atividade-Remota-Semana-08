def main():
    lista = []

    while True:
        a = int(input(f'Digite o primeiro número: '))
        if a == 0:
            break
        lista.append(a)

    print(lista)

    lista_a = comprimento(lista)
    print(lista_a)

    lista_b = inverter(lista)
    print(lista_b)

    lista_c = minimo(lista)
    print(lista_c)

    lista_d = maxino(lista)
    print(lista_d)

    lista_e = soma(lista)
    print(lista_e)

def comprimento(lista):
    cont = 0
    for compri in lista:
        cont += 1
    return cont


def inverter(lista):
    lista_b = lista[::-1]
    return lista_b

def minimo(lista):
    menor = lista[0]
    for a in lista:
        if a < menor:
            menor = a
    
    return menor

def maxino(lista):
    maior = lista[0]
    for a in lista:
        if a > maior:
            maior = a

    return maior

def soma(lista):
    s = 0
    for elementos in lista:
        s += elementos
    return s



if __name__ == '__main__':
    main()