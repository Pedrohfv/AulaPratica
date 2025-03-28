import pytest
from src.projeto_final.jogo import Bola, RAIO_BOLA, LARGURA_TELA, ALTURA_TELA

def test_movimento_bola():
    """Testa se a bola se move corretamente sem colisão"""
    bola = Bola(x=100, y=100, vel_x=5, vel_y=3)
    bola.mover()
    assert bola.x == 105
    assert bola.y == 103

def test_bola_quica_nas_bordas_horizontais():
    """Testa colisão na borda esquerda com correção de posição"""
    bola = Bola(x=RAIO_BOLA, y=100, vel_x=-5, vel_y=0)
    bola.mover()
    assert bola.vel_x == 5  # Deve inverter direção
    assert bola.x == RAIO_BOLA  # Deve ficar exatamente na borda

def test_bola_quica_nas_bordas_verticais():
    """Testa colisão no topo com correção de posição"""
    bola = Bola(x=100, y=RAIO_BOLA, vel_x=0, vel_y=-5)
    bola.mover()
    assert bola.vel_y == 5  # Deve inverter direção
    assert bola.y == RAIO_BOLA  # Deve ficar exatamente na borda

def test_bola_nao_sai_da_tela():
    """Testa colisão na borda direita e inferior"""
    # Teste borda direita
    bola = Bola(x=LARGURA_TELA - RAIO_BOLA, y=300, vel_x=10, vel_y=0)
    bola.mover()
    assert bola.x == LARGURA_TELA - RAIO_BOLA
    assert bola.vel_x == -10
    
    # Teste borda inferior
    bola = Bola(x=400, y=ALTURA_TELA - RAIO_BOLA, vel_x=0, vel_y=10)
    bola.mover()
    assert bola.y == ALTURA_TELA - RAIO_BOLA
    assert bola.vel_y == -10

def test_criacao_bola_aleatoria():
    """Testa se a bola é criada dentro dos limites da tela"""
    bola = criar_bola_aleatoria()
    assert RAIO_BOLA <= bola.x <= LARGURA_TELA - RAIO_BOLA
    assert RAIO_BOLA <= bola.y <= ALTURA_TELA - RAIO_BOLA
    assert isinstance(bola, Bola)