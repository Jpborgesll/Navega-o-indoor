import matplotlib.pyplot as plt

# 1. BANCO DE DADOS (Simulação do JSON que ficaria na nuvem)
# Mapeamos a Quadra 62 da UFG em coordenadas (metros aproximados)
nos = {
    "Entrada Farmácia": (10, 10),     # Perto da rua de baixo
    "Praça SBPC (Convivência)": (40, 50), # Centro da quadra
    "Biblioteca Setorial": (55, 65),  # Acima da praça
    "Fac. Educação": (20, 80),        # Fundo esquerdo
    "Fac. Direito": (70, 80)          # Fundo direito
}

# 2. DEFININDO AS CONEXÕES (Onde é possível andar)
# Isso diz ao sistema: "Existe uma calçada entre A e B"
caminhos = [
    ("Entrada Farmácia", "Praça SBPC (Convivência)"),
    ("Praça SBPC (Convivência)", "Biblioteca Setorial"),
    ("Praça SBPC (Convivência)", "Fac. Educação"),
    ("Praça SBPC (Convivência)", "Fac. Direito")
]

# 3. CONFIGURAÇÃO VISUAL DO GRÁFICO
plt.figure(figsize=(10, 8))
plt.title("Demonstração LOCARE: Mapeamento Digital - UFG (Quadra 62)", fontsize=14)
plt.grid(True, linestyle='--', alpha=0.3)

# Desenha os caminhos (Linhas cinzas representando calçadas)
for ponto_a, ponto_b in caminhos:
    x_values = [nos[ponto_a][0], nos[ponto_b][0]]
    y_values = [nos[ponto_a][1], nos[ponto_b][1]]
    plt.plot(x_values, y_values, 'gray', linestyle='--', linewidth=2, zorder=1)

# Desenha os locais (Pontos azuis)
for nome, coord in nos.items():
    plt.scatter(coord[0], coord[1], color='#004aad', s=150, zorder=2) # Pontos
    plt.text(coord[0] + 2, coord[1], nome, fontsize=10, fontweight='bold') # Nomes

# 4. SIMULAÇÃO DE ROTA (Destaque em VERMELHO)
# Vamos simular um aluno indo da Farmácia para a Biblioteca
rota_exemplo = [("Entrada Farmácia", "Praça SBPC (Convivência)"), 
                ("Praça SBPC (Convivência)", "Biblioteca Setorial")]

for ponto_a, ponto_b in rota_exemplo:
    x_values = [nos[ponto_a][0], nos[ponto_b][0]]
    y_values = [nos[ponto_a][1], nos[ponto_b][1]]
    plt.plot(x_values, y_values, 'red', linewidth=4, alpha=0.7, label='Rota Sugerida (AR)')

# Legendas e Eixos
plt.xlabel("Distância Lateral (Metros)")
plt.ylabel("Profundidade da Quadra (Metros)")
# Adiciona uma legenda única para a rota (truque para não duplicar no gráfico)
plt.legend(["Caminhos Possíveis", "Rota Ativa"], loc='lower right')

print("Gerando mapa da Quadra 62...")
plt.show()