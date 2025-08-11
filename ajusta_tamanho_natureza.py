"""
Script para ajustar o tamanho de natureza2.png para o mesmo de natureza1.png.
Salva a nova imagem como natureza2_ajustada.png na pasta images/.
"""
from skimage.io import imread, imsave
from skimage.transform import resize
import os

img_dir = 'images/'
img1_path = os.path.join(img_dir, 'natureza1.png')
img2_path = os.path.join(img_dir, 'natureza2.png')
img2_out = os.path.join(img_dir, 'natureza2_ajustada.png')

# Leitura das imagens
img1 = imread(img1_path)
img2 = imread(img2_path)

# Redimensiona img2 para o shape de img1
img2_resized = resize(img2, img1.shape, anti_aliasing=True, preserve_range=True).astype(img1.dtype)

# Salva imagem ajustada
imsave(img2_out, img2_resized)
print(f'Imagem ajustada salva em: {img2_out}')
