import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D # Importa a ferramenta 3D

# 1. BANCO DE DADOS COM ALTURA (X, Y, Z)
# Z = 0 (Térreo) | Z = 4 (1º Andar)
nos = {
    "Entrada Farmácia": (10, 10, 0),     # Térreo
    "Praça SBPC": (40, 50, 0),           # Térreo (Meio do caminho)
    "Escada/Elevador": (50, 60, 0),      # Ponto de acesso ao andar de cima
    "Hall Biblioteca": (50, 60, 4),      # 1º Andar (mesma posição X,Y da escada, mas Z=4)
    "Balcão Biblioteca": (55, 65, 4)     # 1º Andar (dentro da biblioteca)
}

# 2. CAMINHOS (Conectando os pontos)
rota_simulada = [
    ("Entrada Farmácia", "Praça SBPC"),
    ("Praça SBPC", "Escada/Elevador"),
    ("Escada/Elevador", "Hall Biblioteca"), # AQUI ACONTECE A SUBIDA (Linha vertical)
    ("Hall Biblioteca", "Balcão Biblioteca")
]

# 3. CONFIGURAÇÃO DO GRÁFICO 3D
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d') # Cria o ambiente 3D

ax.set_title("LOCARE 3D: Navegação Multi-nível (Térreo -> 1º Andar)", fontsize=12)

# Desenha os pontos e nomes
for nome, coord in nos.items():
    x, y, z = coord
    # Diferencia cores por andar
    cor = 'blue' if z == 0 else 'orange' 
    ax.scatter(x, y, z, c=cor, s=100) 
    ax.text(x, y, z+0.5, nome, fontsize=8)

# Desenha as linhas da rota
for ponto_a, ponto_b in rota_simulada:
    xa, ya, za = nos[ponto_a]
    xb, yb, zb = nos[ponto_b]
    
    # Plota a linha vermelha conectando A e B
    ax.plot([xa, xb], [ya, yb], [za, zb], c='red', linewidth=3, alpha=0.8)

# Configurações dos Eixos
ax.set_xlabel('Eixo X (Lateral)')
ax.set_ylabel('Eixo Y (Profundidade)')
ax.set_zlabel('Eixo Z (Altura/Andares)')

# Define o chão (limites) para ficar bonito
ax.set_zlim(0, 10) 

print("Gerando visualização 3D... (Use o mouse para girar o gráfico!)")
plt.show()