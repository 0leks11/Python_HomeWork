from PIL import Image

def make_grayscale(image):
    # Получаем размеры изображения
    width, height = image.size
    
    # Создаем новое изображение в градациях серого
    grayscale_image = Image.new('L', (width, height))
    original_pixels = image.load()
    grayscale_pixels = grayscale_image.load()
    
    # Проходим по всем пикселям изображения
    for y in range(height):
        for x in range(width):
            # Получаем RGB значения текущего пикселя
            r, g, b = original_pixels[x, y]
            
            # Преобразуем в оттенок серого используя формулу для яркости
            gray = int(0.2989 * r + 0.5870 * g + 0.1140 * b)
            
            # Устанавливаем оттенок серого в новое изображение
            grayscale_pixels[x, y] = gray
    
    return grayscale_image

# Замените 'img.jpg' на путь к вашему изображению
try:
    original_image = Image.open('img.jpg')
except IOError:
    print("Не удается загрузить изображение. Проверьте путь к файлу.")

# Преобразуем изображение и сохраняем результат
gray_image = make_grayscale(original_image)
gray_image.save('grayscale_image.jpg')
gray_image.show()