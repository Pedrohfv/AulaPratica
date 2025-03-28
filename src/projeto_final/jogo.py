import pygame
import random

# Constantes exportáveis
__all__ = ['Bola', 'RAIO_BOLA', 'LARGURA_TELA', 'ALTURA_TELA', 'criar_bola_aleatoria']

# Configurações do jogo
LARGURA_TELA = 800
ALTURA_TELA = 600
RAIO_BOLA = 30
AZUL = (30, 144, 255)
BRANCO = (255, 255, 255)

class Bola:
    def __init__(self, x: int, y: int, vel_x: int, vel_y: int) -> None:
        self.x = x
        self.y = y
        self.vel_x = vel_x
        self.vel_y = vel_y

    def mover(self) -> None:
        new_x = self.x + self.vel_x
        new_y = self.y + self.vel_y

        # Colisão com bordas
        if new_x - RAIO_BOLA <= 0 or new_x + RAIO_BOLA >= LARGURA_TELA:
            self.vel_x *= -1
        if new_y - RAIO_BOLA <= 0 or new_y + RAIO_BOLA >= ALTURA_TELA:
            self.vel_y *= -1

        self.x = new_x
        self.y = new_y

    def desenhar(self, tela: pygame.Surface) -> None:
        pygame.draw.circle(tela, AZUL, (self.x, self.y), RAIO_BOLA)

def criar_bola_aleatoria() -> Bola:
    x = random.randint(RAIO_BOLA, LARGURA_TELA - RAIO_BOLA)
    y = random.randint(RAIO_BOLA, ALTURA_TELA - RAIO_BOLA)
    vel_x = random.choice([-4, 4])
    vel_y = random.choice([-4, 4])
    return Bola(x, y, vel_x, vel_y)

def main():
    pygame.init()
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption("🏀 Bola Maluca!")
    
    bola = criar_bola_aleatoria()
    relogio = pygame.time.Clock()
    
    rodando = True
    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
        
        bola.mover()
        tela.fill(BRANCO)
        bola.desenhar(tela)
        pygame.display.flip()
        relogio.tick(60)
    
    pygame.quit()

if __name__ == "__main__":
    main()