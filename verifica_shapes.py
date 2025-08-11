"""
Script para verificar o shape das imagens de natureza.
"""
from skimage.io import imread
import os

img_dir = 'images/'
img1_path = os.path.join(img_dir, 'natureza1.png')
img2_path = os.path.join(img_dir, 'natureza2.png')
img2_ajustada_path = os.path.join(img_dir, 'natureza2_ajustada.png')

img1 = imread(img1_path)
print(f"natureza1.png shape: {img1.shape}")

if os.path.exists(img2_path):
    img2 = imread(img2_path)
    print(f"natureza2.png shape: {img2.shape}")
else:
    print("natureza2.png não encontrado.")

if os.path.exists(img2_ajustada_path):
    img2a = imread(img2_ajustada_path)
    print(f"natureza2_ajustada.png shape: {img2a.shape}")
else:
    print("natureza2_ajustada.png não encontrado.")
