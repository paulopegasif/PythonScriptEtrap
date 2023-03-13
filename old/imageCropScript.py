import cv2

path = "/home/telmo/Desktop/fotos_pulgoes_placa_amarela/"
path_image = "afideo2_campo_05_01_2023_608_608"
path_extension = ".png"
meio = 608 / 2



#carrega a imagem.
image = cv2.imread(path + path_image + path_extension)

print('Imagem carregada: ' + path + path_image + path_extension)

print(image.shape)

height,width,c = image.shape

centro_w = width / 2
centro_h = height / 2

print('height:' + str(centro_h))
print('width:' + str(centro_w))

image_croped = image[(int)(centro_h - meio):(int) (centro_h + meio), (int)(centro_w - meio): (int) (centro_w + 304)]

cv2.imwrite(path +  path_image  + "_croped" + path_extension,image_croped)