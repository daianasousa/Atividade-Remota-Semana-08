def main():
    lista = []
    while True:
        n = int(input('Digite um número: '))
        if n == 0:
            break
        lista.append(n)
    valor = int(input('Qual valor deseja pesquisar? '))

    print(lista)
    print(valor)

    quantidade = count(lista, valor)
    print(quantidade)

def count(lista, valor):
    cont = 0
    for n in lista:
        if n == valor:
            cont += 1
    return cont

if __name__ == '__main__':
    main()