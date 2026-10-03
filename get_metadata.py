from PIL import Image, ExifTags

# Открываем изображение
image = Image.open('/home/user/Downloads/6aad421e60ac3bd3a3f2f42d.jpeg')

# Получаем EXIF-данные
exif_data = image.getexif()

if not exif_data:
    print("В этом файле нет EXIF-данных.")
else:
    # ExifTags.TAGS преобразует числовые ключи в читаемые имена
    for tag_id, value in exif_data.items():
        tag_name = ExifTags.TAGS.get(tag_id, tag_id)
        print(f"{tag_name}: {value}")