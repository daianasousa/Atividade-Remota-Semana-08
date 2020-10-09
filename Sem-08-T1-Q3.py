def main():
    n = int(input("Digite um número: "))
    
    lista_a = inverso(n)
    print(lista_a)

    lista_b, media = media_soma(n)
    if n == 0:
        print(lista_b)
        print('SEM NOTAS')
        print(media)
    else:
        print(lista_b)
        print('{:.1f}'.format(media))

    vogal, cons = letras(n)
    if n != 0:
        print(vogal)
    print(cons)

def inverso(n):
    lista_a = []
    for a in range(n):
        cal = float(input(f"Digite o {a+1}° número: "))
        lista_a.append(cal)
    lista = lista_a[::-1]
    return lista

def media_soma(n):
    lista_b = []
    soma = 0
    for b in range(n):
        nota = float(input(f"Digite sua {b+1}° nota: "))
        lista_b.append(nota)
        soma+= nota

    if n == 0:
        media = 0
    else:
        media = soma / n
    
    return lista_b, media

def letras(n):
    lista_c = []
    for c in range(n):
        letra = input("Digite uma letra: ")[0]
        lista_c.append(letra)
        

    vogal = 0
    cons = []

    for letra in lista_c:
        if letra in 'AaEeIiOoUu':
            vogal+= 1

        elif letra in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
            cons.append(letra)
    return vogal, cons
    

if __name__ == '__main__':
    main()








