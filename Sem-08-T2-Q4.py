def main():
    nomes_jogadores = []
    alturas_jogadores = []

    for c in range(12):
        nome = str(input('Digite seu nome: '))
        nomes_jogadores.append(nome)

        altura = float(input('Digite sua altura: '))
        alturas_jogadores.append(altura)

    alto, nome_alto = mais_alto(alturas_jogadores, nomes_jogadores)
    print('JOGADOR MAIS ALTO DO TIME') 
    print(nome_alto)
    print('{:.2f}'.format(alto))

    media = media_altura(alturas_jogadores)
    print('ALTURA MÉDIA DO TIME') 
    print('{:.2f}'.format(media))

    mais_que_media = mais_alto_media(alturas_jogadores, nomes_jogadores)
    print('JOGADORES MAIS ALTOS QUE A MÉDIA DO TIME') 
    pos = 0
    for n in mais_que_media:
        if pos % 2 == 0:
            print(mais_que_media[pos])
        else:
            print('{:.2f}'.format(mais_que_media[pos]))
        pos += 1


def mais_alto(alturas_jogadores, nomes_jogadores):
    alto = alturas_jogadores[0]
    nome_alto = nomes_jogadores[0]
    pos = 0

    for a in alturas_jogadores:
        if a > alto:
            alto = a
            nome_alto = nomes_jogadores[pos]
        
        pos += 1
    
    return alto, nome_alto


def media_altura(alturas_jogadores):
    soma = 0
    cont = 0
    for num in alturas_jogadores:
        soma += num
        cont += 1

    media = soma / cont

    return media


def mais_alto_media(alturas_jogadores, nomes_jogadores):
    media = media_altura(alturas_jogadores)
    pos = 0

    mais_que_media = []

    for a in alturas_jogadores:
        if a > media:
            mais_que_media.append(nomes_jogadores[pos])
            mais_que_media.append(a)
        
        pos += 1
    
    return mais_que_media


if __name__ == "__main__":
    main()