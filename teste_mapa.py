import matplotlib.pyplot as plt

# Simulação: Imagine que o Admin andou e clicou "Salvar Ponto" nessas coordenadas
# (X, Z) em metros. O Y (altura) geralmente ignoramos em mapas 2D.
pontos_x = [0, 0, 2, 2, 5, 5]  # Coordenada lateral
pontos_z = [0, 3, 3, 6, 6, 10] # Coordenada de profundidade (frente)
nomes = ["Entrada (ArUco)", "Corredor A", "Curva 1", "Corredor B", "Curva 2", "Raio-X"]

# Configura o gráfico
plt.figure(figsize=(8, 6))
plt.grid(True, linestyle='--', alpha=0.6)

# 1. Desenha a linha do caminho (O trajeto)
plt.plot(pontos_x, pontos_z, color='blue', linewidth=2, label='Rota Caminhável')

# 2. Desenha os pontos (Os nós/waypoints)
plt.scatter(pontos_x, pontos_z, color='red', s=100, zorder=5)

# 3. Coloca os nomes nos pontos
for i, nome in enumerate(nomes):
    plt.text(pontos_x[i] + 0.2, pontos_z[i], f"{i}. {nome}", fontsize=9)

# Detalhes visuais
plt.title("Simulação do Mapeamento (Modo Admin)")
plt.xlabel("Eixo X (Metros - Lateral)")
plt.ylabel("Eixo Z (Metros - Profundidade)")
plt.legend()
plt.axvline(0, color='black', linewidth=0.5) # Linha de centro
plt.axhline(0, color='black', linewidth=0.5) # Linha de centro

# Mostra o gráfico
print("Abrindo visualização do mapa...")
plt.show()