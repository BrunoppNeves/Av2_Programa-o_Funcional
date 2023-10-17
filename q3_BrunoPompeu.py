from PIL import Image

image_path = '/home/brunopequeno/Documents/faculdade/6semestre/funcional/AV2/AV2_BrunoPompeu/foto.jpg'
image = Image.open(image_path)
width, height = image.size
brightness_increase = int(input('Enter the value to increase brightness: '))

increase_channel = lambda channel: min(255, channel + brightness_increase)
image_info = [[image.getpixel((x, y)) for y in range(height)] for x in range(width)]
modified_image = [[tuple(map(lambda c: increase_channel(c), image_info[x][y])) for y in range(height)] for x in range(width)]
new_image = Image.new('RGB', (width, height))
[new_image.putpixel((x, y), modified_image[x][y]) for x in range(width) for y in range(height)]
new_image.save('new_image.jpg')
print('Image generated successfully!')
