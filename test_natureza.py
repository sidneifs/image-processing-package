"""
Script de teste para o pacote image-processing-package usando imagens de natureza.
Coloque duas imagens PNG em 'images/natureza1.png' e 'images/natureza2.png'.
"""
from image_processing.processing.combination import find_difference, transfer_histogram
from image_processing.processing.transformation import resize_image
from image_processing.utils.io import read_image, save_image
from image_processing.utils.plot import plot_image, plot_result


# Caminhos das imagens de teste
import os
dir_img = 'images/'
img1_path = os.path.join(dir_img, 'natureza1.png')
img2_path = os.path.join(dir_img, 'natureza2_ajustada.png') if os.path.exists(os.path.join(dir_img, 'natureza2_ajustada.png')) else os.path.join(dir_img, 'natureza2.png')


# Leitura das imagens
i1 = read_image(img1_path)
i2 = read_image(img2_path)
# Remove dimensão extra se necessário
if len(i1.shape) == 4 and i1.shape[0] == 1:
	i1 = i1[0]
if len(i2.shape) == 4 and i2.shape[0] == 1:
	i2 = i2[0]

# Teste 1: Comparação de similaridade
print('Teste: Similaridade')
diff = find_difference(i1, i2)
plot_image(diff)
save_image(diff, f"{dir_img}natureza_diff.png")

# Teste 2: Transferência de histograma
print('Teste: Transferência de histograma')
matched = transfer_histogram(i1, i2)
plot_result(i1, i2, matched)
save_image(matched, f"{dir_img}natureza_matched.png")

# Teste 3: Redimensionamento
print('Teste: Redimensionamento')
resized = resize_image(i1, 0.5)
plot_image(resized)
save_image(resized, f"{dir_img}natureza_resized.png")

print('Imagens geradas em:', dir_img)
