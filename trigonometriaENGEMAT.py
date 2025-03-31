import math #sen e cos
import matplotlib as plt #criar, alterar e configurar gráficos ++matplotlib.pyplot

#%matplotlib inline

def plotUnitCircle(x_cosseno, y_seno, tangente):
    eixos = plt.subplot() #produz figura em vários plots (áreas) diferentes, retorna os eixos x e y
    eixos.grid(True) #grade para visualizar as posições

    #CÍRCULO TRIGONOMÉTRICO
    circulo = plt.Circle((0,0), radius=1.0, edgecolor = "black", facecolor = "none")
    eixos.add_artist(circulo)


    #PLANO CARTESIANO
    eixos.axhline(y=0.0, color="black") #insere linha horizontal que define o eixo x
    eixos.axvline(x=0.0, color="black") #define o eixo y

    max_limit = max(abs(tangente), 1.0) + 0.2  # Limite baseado na tangente ou 1.0
    plt.xlim(-max_limit, max_limit) #define o limite de x no plot
    plt.ylim(-max_limit, max_limit) #define o limite de y no plot


    #TRIANGULO
    eixos.plot([0.0,x_cosseno],[0.0,0.0], color ="blue", label="cateto adjacente") #define a posicao x e y da linha, inicial e final
    eixos.plot([x_cosseno,x_cosseno],[0.0,y_seno], color ="green", label="cateto oposto")
    eixos.plot([0.0,x_cosseno],[0.0,y_seno], color ="red", label="hipotenusa")

    if x_cosseno<0.0:
      tangente = -tangente
      eixos.plot([-1.0, -1.0], [0.0, tangente], color="orange", label="tangente")
      eixos.plot([x_cosseno, -1.0],[y_seno, tangente], linestyle='dashed', color ="grey") #reta TRACEJADA para indicar a extensão para o encontro da tangente

    elif x_cosseno>0.0:
      eixos.plot([1.0, 1.0], [0.0, tangente], color="orange", label="tangente")
      eixos.plot([x_cosseno, 1.0],[y_seno, tangente], linestyle='dashed', color ="grey") #reta TRACEJADA para indicar a extensão para o encontro da tangente

    #caso cosseno igual a 0, tangente não existe, pois tangente = seno/cosseno, tangente= oposto/adjacente

    eixos.plot([x_cosseno,x_cosseno], [y_seno, y_seno], "o", color="purple") #ponto único, "o" define que vai ter formato de ponto

    #EXIBIÇÃO
    plt.legend() #mostra os rótulos escritos (ex: cat op, cat adj, hipotenusa)
    plt.title("Trigonometria com Python")
    plt.show()

#FORA FUNÇÃO
angulo = float(input("Digite um valor para o ângulo em graus: "))
angulo_r = math.radians(angulo)

#cos t = x (base, adjacente)-----cos t = adj/hipo
x_cosseno= math.cos(angulo_r)

# sen t = y (altura do triangulo, oposto)----sen t = op/hipo
y_seno= math.sin(angulo_r)

tangente = math.tan(angulo_r)

print("Cosseno do ângulo (x) =", round(x_cosseno, 2),"\nSeno do ângulo (y) =", round(y_seno, 2), "\nTangente do ângulo =", round(tangente, 2))

plotUnitCircle(x_cosseno, y_seno, tangente)