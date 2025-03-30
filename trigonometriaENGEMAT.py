import math #sen e cos
import matplotlib as plt #criar, alterar e configurar gráficos ++matplotlib.pyplot

#%matplotlib inline

def plotUnitCircle(x_cosseno, y_seno, tangente):
    eixos = plt.subplot()  # produz figura em vários plots (áreas) diferentes, retorna os eixos x e y
    eixos.grid(True)  # grade para visualizar as posições

    # CÍRCULO TRIGONOMÉTRICO
    circulo = plt.Circle((0, 0), radius=1.0, edgecolor="black", facecolor="none")
    eixos.add_artist(circulo)

    # PLANO CARTESIANO
    eixos.axhline(y=0.0, color="black")  # insere linha horizontal que define o eixo x
    eixos.axvline(x=0.0, color="black")  # define o eixo y

    # verificação para que não corte a tangente ao MONTAR O PLANO CARTESIANO
    if tangente <= 1:
        plt.ylim(-1.0, 1.0)  # define o limite de y no plot
        plt.xlim(-1.0, 1.0)  # define o limite de x no plot

    else:
        plt.ylim(-(round(tangente, 0) + 0.5), (round(tangente, 0) + 0.5))  # limite de y
        plt.xlim(-(round(tangente, 0) + 0.5), (round(tangente, 0) + 0.5))  # limite de y

    # TRIANGULO
    eixos.plot([0, x_cosseno], [0, 0], color="blue",
               label="cateto adjacente")  # define a posicao x e y da linha, inicial e final
    eixos.plot([x_cosseno, x_cosseno], [0, y_seno], color="green", label="cateto oposto")
    eixos.plot([0, x_cosseno], [0, y_seno], color="red", label="hipotenusa")

    if x_cosseno > 0:
        eixos.plot([1.0, 1.0], [0, tangente], color="yellow", label="tangente")
    elif x_cosseno < 0:
        eixos.plot([-1.0, -1.0], [0, tangente], color="yellow", label="tangente")
        # caso cosseno igual a 0, tangente não existe, pois tangente = seno/cosseno

    # EXIBIÇÃO
    plt.legend()  # mostra os rótulos escritos (ex: cat op, cat adj, hipotenusa)
    plt.title("Nome do Gráfico")
    plt.show()

#CÓDIGO FORA FUNÇÃO
angulo = float(input("Digite um valor para o ângulo em graus: "))
angulo = math.radians(angulo)

#cos t = x (base, adjacente)-----cos t = adj/hipo
x_cosseno= math.cos(angulo)

# sen t = y (altura do triangulo, oposto)----sen t = op/hipo
y_seno= math.sin(angulo)

tangente = math.tan(angulo)

print("Cosseno do ângulo (x) =", round(x_cosseno, 2),"\nSeno do ângulo (y) =", round(y_seno, 2), "\nTangente do ângulo =", round(tangente, 2))

plotUnitCircle(x_cosseno, y_seno, tangente)