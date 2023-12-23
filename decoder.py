from PIL import Image

input_img_path = "output_img.png"
input_img = Image.open(input_img_path)

width, height = input_img.size

output_img = Image.new("RGB", (width, height))

# Iterar sobre todos os pixels e ocultar informações da segunda imagem na primeira
for y in range(height):
    for x in range(width):

        # Limpando os bits mais significativos usando a mascara 0x0F = 00001111
        # junto com o operador AND e posteriormente deslocando 4 bits para a esquerda
        # tornando os bits menos significativos em mais significativos
        input_r, input_g, input_b = input_img.getpixel((x, y))
        output_r = (input_r & 0x0F) << 4
        output_g = (input_g & 0x0F) << 4
        output_b = (input_b & 0x0F) << 4



        # Criar a imagem de saída
        output_img.putpixel((x, y), (output_r, output_g, output_b))

output_img.save("decoded.png", "png")
input_img.close()
