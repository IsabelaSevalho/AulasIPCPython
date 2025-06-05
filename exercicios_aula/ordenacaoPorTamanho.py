def ordena(lista):

    #tenta colocar no lugar certo à esquerda
    for i in range(1, len(lista)):
        atual = lista[i] #palavra atual que quer posicionar corretamente (vai do primeiro até o penultimo)
        anterior = i - 1 #palavra anterior, compara à esquerda
        while anterior>=0 and len(lista[anterior]) < len(atual): #enquanto o tamanho da esquerda for menor que a atual
            lista[anterior + 1] = lista[anterior] #a menor vai mais para a direita
            anterior -= 1 #anda mais uma posicao à esquerda
        lista[anterior + 1] = atual #posição correta para inserir a palavra atual
    return lista


#cod
n = int(input())

for i in range(n):
    texto = input()

    #divide as palavras
    lista_palavras = texto.split(" ")
    #recebe e junta em uma string
    texto_ordenado_lista = ordena(lista_palavras)

    texto_ordenado=' '.join(texto_ordenado_lista)

    print(texto_ordenado.strip())