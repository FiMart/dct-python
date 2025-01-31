import cv2
import matplotlib.pyplot as plt
import numpy as np

# โหลดภาพต้นฉบับ (เปลี่ยน 'tintin.jpg' เป็นชื่อไฟล์ภาพของคุณ)
image_path = 'd:/image/tintin.jpg'
original_image = cv2.imread(image_path)
original_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)  # แปลงเป็น RGB

# ระดับคุณภาพที่ต้องการบีบอัด 
quality_levels = [10, 30, 50, 70, 90] #quality ใส่ได้ Max สุดคือ <= 6 ค่า มากกว่านี้จะ Error แต่รูปที่บีบอัดตั้งแต่ 10-90 ก็จะบันทึกเป็น .jpg
compressed_images = []

# ทำการบีบอัดและบันทึกภาพที่แตกต่างกัน
for quality in quality_levels:
    output_path = f'compressed_{quality}.jpg'
    cv2.imwrite(output_path, cv2.cvtColor(original_image, cv2.COLOR_RGB2BGR), [int(cv2.IMWRITE_JPEG_QUALITY), quality])
    compressed_image = cv2.imread(output_path)
    compressed_image = cv2.cvtColor(compressed_image, cv2.COLOR_BGR2RGB)  # แปลงเป็น RGB
    compressed_images.append((quality, compressed_image))

# แสดงภาพต้นฉบับและภาพที่บีบอัดแล้ว
plt.figure(figsize=(15, 8))
plt.subplot(2, 3, 1)
plt.imshow(original_image)
plt.title("Original Image")
plt.axis("off")

for i, (quality, img) in enumerate(compressed_images):
    plt.subplot(2, 3, i + 2)
    plt.imshow(img)
    plt.title(f"Quality {quality}")
    plt.axis("off")

plt.tight_layout()
plt.show()