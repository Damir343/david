from PIL import Image
# Ввод пути до изображения
img_path = input('Введите путь до изображения: ')
# Открываем изображение в формате PNG
img = Image.open(img_path)
# Сохраняем изображение в формате ICO
img.save('output.ico')