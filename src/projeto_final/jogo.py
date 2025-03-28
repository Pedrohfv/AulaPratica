""" Módulo do jogo: Bola Maluca """

import random
import pygame

__all__ = [
    'Bola',
    'RAIO_BOLA',
    'LARGURA_TELA',
    'ALTURA_TELA',
    'criar_bola_aleatoria'
]

# Configurações
LARGURA_TELA = 800
ALTURA_TELA = 600
RAIO_BOLA = 30
AZUL = (30, 144, 255)
BRANCO = (255, 255, 255)


class Bola:
    """ Representa a bola do jogo, que se move e colide com as bordas. """

    def __init__(self, x: int, y: int, vel_x: int, vel_y: int) -> None:
        """ Inicializa a bola com posição (x, y) e velocidade """
        self.x = x
        self.y = y
        self.vel_x = vel_x
        self.vel_y = vel_y

    def mover(self) -> None:
        """ Move a bola e inverte a direção ao colidir com as bordas. """
        new_x = self.x + self.vel_x
        new_y = self.y + self.vel_y

        if new_x - RAIO_BOLA <= 0:
            new_x = RAIO_BOLA
            self.vel_x *= -1
        elif new_x + RAIO_BOLA >= LARGURA_TELA:
            new_x = LARGURA_TELA - RAIO_BOLA
            self.vel_x *= -1

        if new_y - RAIO_BOLA <= 0:
            new_y = RAIO_BOLA
            self.vel_y *= -1
        elif new_y + RAIO_BOLA >= ALTURA_TELA:
            new_y = ALTURA_TELA - RAIO_BOLA
            self.vel_y *= -1

        self.x = new_x
        self.y = new_y

    def desenhar(self, tela: pygame.Surface) -> None:
        """ Desenha a bola na tela. """
        pygame.draw.circle(tela, AZUL, (self.x, self.y), RAIO_BOLA)


def criar_bola_aleatoria() -> Bola:
    """ Cria uma bola em posição aleatória com velocidade fixa. """
    x = random.randint(RAIO_BOLA, LARGURA_TELA - RAIO_BOLA)
    y = random.randint(RAIO_BOLA, ALTURA_TELA - RAIO_BOLA)
    vel_x = random.choice([-4, 4])
    vel_y = random.choice([-4, 4])
    return Bola(x, y, vel_x, vel_y)


def main():
    """ Função principal do jogo. Inicia o pygame e executa o loop do jogo. """
    pygame.init()  # pylint: disable=no-member
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption(
        "🏀 Bola Maluca!"
    )  # Dividindo a linha para ficar abaixo de 79 caracteres

    bola = criar_bola_aleatoria()
    relogio = pygame.time.Clock()

    rodando = True
    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # pylint: disable=no-member
                rodando = False

        bola.mover()
        tela.fill(BRANCO)
        bola.desenhar(tela)
        pygame.display.flip()
        relogio.tick(60)

    pygame.quit()  # pylint: disable=no-member


if __name__ == "__main__":
    main()
