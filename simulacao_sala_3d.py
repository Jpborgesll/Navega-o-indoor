import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

def desenhar_cubo(ax, origem, tamanho, cor_linha='black'):
    # Função auxiliar para desenhar as linhas de um paralelepípedo (Sala)
    x, y, z = origem
    dx, dy, dz = tamanho
    
    # Definindo os 8 vértices do cubo (sala)
    # Formato: [x, x+dx], [y, y], [z, z] ...
    
    # Chão (z)
    ax.plot([x, x+dx], [y, y], [z, z], color=cor_linha, alpha=0.5)
    ax.plot([x, x+dx], [y+dy, y+dy], [z, z], color=cor_linha, alpha=0.5)
    ax.plot([x, x], [y, y+dy], [z, z], color=cor_linha, alpha=0.5)
    ax.plot([x+dx, x+dx], [y, y+dy], [z, z], color=cor_linha, alpha=0.5)

    # Teto (z + dz)
    ax.plot([x, x+dx], [y, y], [z+dz, z+dz], color=cor_linha, alpha=0.3)
    ax.plot([x, x+dx], [y+dy, y+dy], [z+dz, z+dz], color=cor_linha, alpha=0.3)
    ax.plot([x, x], [y, y+dy], [z+dz, z+dz], color=cor_linha, alpha=0.3)
    ax.plot([x+dx, x+dx], [y, y+dy], [z+dz, z+dz], color=cor_linha, alpha=0.3)

    # Pilares (paredes verticais)
    ax.plot([x, x], [y, y], [z, z+dz], color=cor_linha, alpha=0.3)
    ax.plot([x+dx, x+dx], [y, y], [z, z+dz], color=cor_linha, alpha=0.3)
    ax.plot([x, x], [y+dy, y+dy], [z, z+dz], color=cor_linha, alpha=0.3)
    ax.plot([x+dx, x+dx], [y+dy, y+dy], [z, z+dz], color=cor_linha, alpha=0.3)

# --- CONFIGURAÇÃO DA CENA ---
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.set_title("Navegação Indoor: Sala de Aula UFG (Modelo Volumétrico)", fontsize=12)

# 1. DESENHAR A SALA (8m largura x 10m profundidade x 3m altura)
# Origem (0,0,0), Tamanho (8, 10, 3)
desenhar_cubo(ax, (0,0,0), (8, 10, 3), cor_linha='gray')

# 2. ADICIONAR OBJETOS (Móveis)
# Lousa na parede do fundo (Y=10)
ax.plot([2, 6], [10, 10], [1, 1], color='green', linewidth=4, label='Lousa') # Base da lousa
ax.plot([2, 6], [10, 10], [2.5, 2.5], color='green', linewidth=4) # Topo da lousa
ax.plot([2, 2], [10, 10], [1, 2.5], color='green', linewidth=4) # Esquerda
ax.plot([6, 6], [10, 10], [1, 2.5], color='green', linewidth=4) # Direita

# Carteiras (Simulando pontos de obstáculos)
carteiras_x = [2, 6, 2, 6]
carteiras_y = [3, 3, 7, 7]
ax.scatter(carteiras_x, carteiras_y, 0.5, c='brown', marker='s', s=200, label='Carteiras')

# Porta (Entrada em 0,0)
ax.text(0.5, 0, 1.5, "PORTA", color='black', fontsize=10, fontweight='bold')

# 3. ROTA DE NAVEGAÇÃO (AR)
# O aluno entra (1,0), desvia de uma carteira e vai até a carteira do fundo (6,7)
rota_x = [1, 1, 4, 6]
rota_y = [0, 2, 5, 7]
rota_z = [0, 0, 0, 0] # A rota é no chão (mas poderíamos elevar a seta para o nível dos olhos: 1.5m)

# Desenha a linha da rota
ax.plot(rota_x, rota_y, rota_z, color='red', linewidth=3, label='Caminho AR', linestyle='--')

# Seta final (Onde sentar)
ax.scatter(6, 7, 1, c='red', marker='v', s=100, label='Destino')

# Limites e Etiquetas
ax.set_xlabel('Largura (m)')
ax.set_ylabel('Profundidade (m)')
ax.set_zlabel('Altura (m)')
ax.legend()

print("Gerando Sala 3D...")
plt.show()