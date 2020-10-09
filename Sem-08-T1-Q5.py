def main():
    lista_a = []
    for a in range(25):
        num = int(input(f'Digite o {num+1}° número: '))
        lista_a.append(num)

    lista_b = []
    for b in range(25):
        num = int(input(f'Digite o {num+1}° número: '))
        lista_b.append(num)
    
    print(lista_a)
    print(lista_b)
    
    lista_c = lista_intercalada(lista_a, lista_b)
    print(lista_c)


def lista_intercalada(lista_a, lista_b):
    lista_c = []
    posicao = 0

    while True:
        if len(lista_c) >= 50 :
            break
            
        lista_c.append(lista_a[posicao])
        lista_c.append(lista_b[posicao])

        posicao += 1

    return lista_c


if __name__ == '__main__':
    main()