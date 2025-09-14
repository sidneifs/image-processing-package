
# image-processing-package

Pacote Python para processamento de imagens, incluindo funções de combinação, transformação, leitura, salvamento e visualização de imagens.

## Funcionalidades

- Comparação de similaridade entre imagens (SSIM)
- Transferência de histograma entre imagens
- Redimensionamento de imagens
- Leitura e salvamento de arquivos de imagem
- Visualização de imagens e histogramas RGB

## Instalação

Recomenda-se utilizar um ambiente virtual. Instale as dependências com:

```bash
pip install -r requirements.txt
```

## Exemplo de Uso

```python
from image_processing.processing.combination import find_difference, transfer_histogram
from image_processing.processing.transformation import resize_image
from image_processing.utils.io import read_image, save_image
from image_processing.utils.plot import plot_image, plot_result, plot_histogram

# Leitura de imagens
img1 = read_image('caminho/para/imagem1.png')
img2 = read_image('caminho/para/imagem2.png')

# Comparação de similaridade
diff = find_difference(img1, img2)
plot_image(diff)

# Transferência de histograma
matched = transfer_histogram(img1, img2)
plot_result(img1, img2, matched)

# Redimensionamento
img_resized = resize_image(img1, 0.5)
plot_image(img_resized)

# Salvar imagem
save_image(img_resized, 'caminho/para/imagem_redimensionada.png')
```

## Estrutura do Projeto

- `image_processing/processing/combination.py`: Funções de comparação e transferência de histograma
- `image_processing/processing/transformation.py`: Função de redimensionamento
- `image_processing/utils/io.py`: Leitura e salvamento de imagens
- `image_processing/utils/plot.py`: Visualização de imagens e histogramas

## Testes com Imagens de Natureza

1. Adicione duas imagens de natureza (paisagens, florestas, etc) no formato PNG na pasta `images/` deste projeto, com os nomes:
   - `images/natureza1.png`
   - `images/natureza2.png`

2. Execute o script de teste:

   ```bash
   python test_natureza.py
   ```

3. O script irá:
   - Comparar as imagens e salvar `natureza_diff.png` (diferença/semelhança)
   - Transferir histograma e salvar `natureza_matched.png`
   - Redimensionar e salvar `natureza_resized.png`

4. Visualize os resultados usando as funções de plot do pacote ou abrindo os arquivos gerados na pasta `images/`.

Se não houver imagens, consulte o arquivo `images/README.txt` para instruções de como obtê-las.

### Sugestão de sites para baixar imagens livres de direitos autorais

- [Unsplash](https://unsplash.com/s/photos/nature)
- [Pixabay](https://pixabay.com/pt/images/search/natureza/)
- [Pexels](https://www.pexels.com/pt-br/procurar/natureza/)

Baixe as imagens desejadas, salve como `natureza1.png` e `natureza2.png` na pasta `images/` e siga os passos acima para rodar os testes.

## Autor

Sidnei Silva ([GitHub](https://github.com/sidneifs)).

## Licença

[MIT](https://choosealicense.com/licenses/mit/)
