from PIL import Image

input_img_path = "input_img.png"
input_img = Image.open(input_img_path)

img_to_hide_path = "image_to_hide.png"
img_to_hide = Image.open(img_to_hide_path)

# forçar o tamanho da segunda imagem para ser igual ao da primeira
img_to_hide = img_to_hide.resize(input_img.size)

width, height = input_img.size

output_img = Image.new("RGB", (width, height))

# Iterar sobre todos os pixels e ocultar informações da segunda imagem na primeira
for y in range(height):
    for x in range(width):
        # Obter os valores de R, G, B para ambas as imagens
        input_r, input_g, input_b = input_img.getpixel((x, y))
        to_hide_r, to_hide_g, to_hide_b = img_to_hide.getpixel((x, y))

        # Utilizar os 4 bits menos significativos da input_img para 
        # armazenar os bits mais significativos da img_to_hide
        # Máscara 0xF0 = 11110000 utilizamos o AND para zerar os 4 bits menos significativos
        # e depois utilizamos o OR para armazenar os 4 bits mais significativos da segunda imagem
        # >> é utilizado para deslocar os bits mais significativos da segunda iamgem para 
        # o local dos bits menos significativos
        output_r = (input_r & 0xF0) | ((to_hide_r & 0xF0) >> 4)
        output_g = (input_g & 0xF0) | ((to_hide_g & 0xF0) >> 4)
        output_b = (input_b & 0xF0) | ((to_hide_b & 0xF0) >> 4)

        # Criar a imagem de saída
        output_img.putpixel((x, y), (output_r, output_g, output_b))

output_img.save("output_img.png", "png")

input_img.close()
img_to_hide.close()
