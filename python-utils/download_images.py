import requests

for i in range(140, 150):
    image_url = f'http://lib.kaznau.kz/Res/ebook_29/Pages/{i}.jpg'
    img_data = requests.get(image_url).content
    with open(f'images/{i}.jpg', 'wb') as handler:
        handler.write(img_data)
