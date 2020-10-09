def main():
    num = []
    multi = 1

    for n in range(10):
        numero = int(input(f"Digite o {n +1}° número: "))
        num.append(numero)
        multi *= numero
    soma = calculo(num)
    print(num)
    print(soma)
    print(multi)

def calculo(num):
    return sum(num)

if __name__ == "__main__":
    main()