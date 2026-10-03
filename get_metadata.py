import os
import math
from PIL import Image

dir_path = '/home/user/Downloads/6aad421/'

rows = []
for filename in sorted(os.listdir(dir_path)):
    if not filename.lower().endswith(('.jpg', '.jpeg')):
        continue
    path = os.path.join(dir_path, filename)
    size_kb = os.path.getsize(path) / 1024

    with Image.open(path) as im:
        w, h = im.size
        mp = w * h / 1e6
        # Энтропия по яркости — грубая оценка "сложности"
        gray = im.convert('L')
        hist = gray.histogram()
        total = sum(hist)
        entropy = -sum((c/total) * math.log2(c/total) for c in hist if c)
        # Оценка качества JPEG через quantization tables
        q = im.quantization
        # Берём среднее по первой таблице как прокси
        q_avg = sum(q[0]) / len(q[0]) if q else 0

    rows.append((filename, size_kb, w, h, mp, entropy, q_avg))

# Печатаем таблицей
print(f"{'файл':<40} {'КБ':>8} {'WxH':>12} {'Мп':>6} {'энтр':>6} {'q~':>6}")
for r in sorted(rows, key=lambda x: x[1]):
    print(f"{r[0]:<40} {r[1]:8.1f} {r[2]}x{r[3]:<7} {r[4]:6.2f} {r[5]:6.2f} {r[6]:6.1f}")