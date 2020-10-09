def main():
    nomes_alunos = []
    idades_alunos = []
    alturas_alunos = []

    for c in range(30): 
        nome = str(input('Digite seu nome: '))
        nomes_alunos.append(nome)

        idade = int(input('Digite sua idade: '))
        idades_alunos.append(idade)

        altura = float(input('Digite sua altura: '))
        alturas_alunos.append(altura)

    print('MAIORES DE 13 ANOS COM ALTURA ABAIXO DA MÉDIA')
    resultado = altura_menos_que_media(nomes_alunos, idades_alunos, alturas_alunos)
    for c in range(len(resultado)):
        print(resultado[c])


def media_altura(alturas_alunos):
    soma = 0
    cont = 0

    for num in alturas_alunos:
        soma += num
        cont += 1

    media = soma / cont

    return round(media, 2)


def altura_menos_que_media(nomes_alunos, idades_alunos, alturas_alunos):
    media = media_altura(alturas_alunos)
    resultado = []

    pos = 0
    while pos <= len(alturas_alunos) - 1:
        if alturas_alunos[pos] < media:
            if idades_alunos[pos] > 13:
                resultado.append(nomes_alunos[pos])
        pos += 1

    return resultado


if __name__ == "__main__":
    main()