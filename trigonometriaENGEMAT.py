import math #sen e cos
import matplotlib as plt #criar, alterar e configurar gráficos ++matplotlib.pyplot

#%matplotlib inline

def plotUnitCircle(x, y):
    eixos = plt.subplot() #produz figura em vários plots (áreas) diferentes, retorna os eixos x e y
    eixos.grid(True) #grade para visualizar as posições

    #CÍRCULO TRIGONOMÉTRICO
    circulo = plt.Circle((0,0), radius=1.0, edgecolor = "black", facecolor = "none")
    eixos.add_artist(circulo)

    #PLANO CARTESIANO
    eixos.axhline(y=0.0, color="black") #insere linha horizontal que define o eixo x
    eixos.axvline(x=0.0, color="black") #define o eixo y

    plt.xlim(-1.0, 1.0) #define o limite de x no plot
    plt.ylim(-1.0, 1.0) #define o limite de x no plot

    #TRIANGULO
    eixos.plot([0,x],[0,0], color ="blue", label="cateto adjacente") #define a posicao x e y da linha, inicial e final
    eixos.plot([x,x],[0,y], color ="green", label="cateto oposto")
    eixos.plot([0,x],[0,y], color ="red", label="hipotenusa")

    #EXIBIÇÃO
    plt.legend() #mostra os rótulos escritos (ex: cat op, cat adj, hipotenusa)
    plt.title("Nome do Gráfico")
    plt.show()

#CÓDIGO FORA FUNÇÃO
angulo = float(input("Digite um valor para o ângulo em graus: "))
angulo = math.radians(angulo)

#cos t = x (base, adjacente)-----cos t = adj/hipo
x= math.cos(angulo)

# sen t = y (altura do triangulo, oposto)----sen t = op/hipo
y= math.sin(angulo)

print("Cosseno do ângulo (x) =", round(x, 2),"\nSeno do ângulo (y) =", round(y, 2))

plotUnitCircle(x, y)