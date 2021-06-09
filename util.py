from PIL import Image, ImageFilter

# img = Image.open('./Pokedex/pikachu.jpg')
# blurred_image = img.filter(ImageFilter.BLUR)
# blurred_image.save('pikachu_blurred.png','png')

# converted_gray = img.convert('L').rotate(180).resize((150,150))
# converted_gray.save('gray_pikachu.png','png')

# cropped = img.crop((60, 20, 400, 200))
# cropped.save('cropped.png',quality=10)

# img = Image.open('./astro.jpg')

# to avoid images squished

# img.thumbnail((400,400))
# img.save('thumbnail_astro.jpg')

# print(img.size)

img = Image.open('./pprint-scrape.png')
converted_gray = img.resize((432,243))
converted_gray.save('pprint-scrape-resized.png','png')