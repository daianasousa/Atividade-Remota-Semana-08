def main():
    lista_a = []
    for a in range(20):
        n = int(input(f'Digite o {a+1}° número: '))
        lista_a.append(n)

    lista_b = []
    for a in range(20):
        n = int(input(f'Digite o {a+1}° número: '))
        lista_b.append(n)


    print(lista_a)
    print(lista_b)
    lista_c = lista_soma(lista_a, lista_b)
    print(lista_c)

def lista_soma(lista_a, lista_b):
    lista_c = []
    posicao = 0

    while True:
        if len(lista_c) >= 20 :
            break
            
        lista_c.append(lista_a[posicao] + lista_b[posicao])

        posicao += 1

    return lista_c


if __name__ == "__main__":
    main()