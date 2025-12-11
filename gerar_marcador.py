import cv2
import cv2.aruco as aruco
import numpy as np

# 1. Define o dicionário (o "idioma" dos marcadores)
# DICT_4X4_50 significa: quadriculado 4x4, com 50 variações possíveis.
# É leve e rápido para celular.
dicionario_aruco = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)

# 2. Gera a imagem do marcador
# Parâmetros: (Dicionário, ID do marcador, Tamanho em pixels)
# Vamos gerar o ID 0 (que seria o da entrada do hospital)
tamanho_pixels = 400
marcador_img = aruco.generateImageMarker(dicionario_aruco, 0, tamanho_pixels)

# 3. Adiciona uma borda branca para ficar mais fácil de ver
marcador_img = cv2.copyMakeBorder(marcador_img, 20, 20, 20, 20, cv2.BORDER_CONSTANT, value=255)

# 4. Mostra na tela (abre uma janela fora do VS Code)
print("Pressione qualquer tecla na janela da imagem para fechar...")
cv2.imshow("Seu Marcador ArUco (ID 0)", marcador_img)

# Salva o arquivo no seu computador para você imprimir depois
cv2.imwrite("marcador_id0.png", marcador_img)
print("Imagem 'marcador_id0.png' salva na pasta!")

cv2.waitKey(0)
cv2.destroyAllWindows()