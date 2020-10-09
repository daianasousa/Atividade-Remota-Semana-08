def main():
    numero = []
    for num in range(20):
        n = int(input(f'Digite o {num+1}° número: '))
        numero.append(n)
    print(numero)

    par, impar = par_impar(numero)
    print(par)
    print(impar)

def par_impar(numero):
    par = []
    impar = []
    for n in numero:
        if n % 2 == 0:
            par.append(n)
        else:
            impar.append(n)

    return par, impar

if __name__ == '__main__':
    main()
