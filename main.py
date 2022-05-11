import matplotlib.pyplot as plt


def punto_de_mira(lista_de_coordenadas):
    for coordenadas in lista_de_coordenadas:
        plt.plot(coordenadas[0], coordenadas[1], 'bo')

    plt.plot(0, 0, 'k+')
    plt.ylabel('Y')
    plt.xlabel('X')
    plt.show()


if __name__ == '__main__':
    lista_de_coordenadas = [
        [0, 0],
        [1, 0],
        [-1, 0],
        [0, -1],
        [0, 1]
    ]
    punto_de_mira(lista_de_coordenadas)
