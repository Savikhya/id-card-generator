import csv
from PIL import Image, ImageOps
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.lib.utils import ImageReader
import os

TEMPLATE_PATH = 'template.png'
CSV_PATH = 'employee_data.csv'
PHOTO_DIR = 'photos'
OUTPUT_PDF = 'employee_id_cards.pdf'

PAGE_WIDTH, PAGE_HEIGHT = 85.6 * mm, 54 * mm

def draw_id_card(c, name, photo_path):
    
    c.drawImage(TEMPLATE_PATH, 0, 0, width=PAGE_WIDTH, height=PAGE_HEIGHT)
    photo_x = 48 * mm
    photo_y = 19.5 * mm
    photo_w = 28 * mm
    photo_h = 30 * mm
    if os.path.exists(photo_path):
        img = Image.open(photo_path)
        px_w = int((photo_w / mm) / 25.4 * 300)
        px_h = int((photo_h / mm) / 25.4 * 300)
        img = ImageOps.fit(img, (px_w, px_h), method=Image.LANCZOS)
        img_reader = ImageReader(img)
        c.drawImage(img_reader, photo_x, photo_y, width=photo_w, height=photo_h, mask='auto')
    else:
        print(f"Photo not found: {photo_path}")
    c.setFont("Helvetica-Bold", 12)
    c.setFillColorRGB(1, 1, 1)
    c.drawCentredString(PAGE_WIDTH / 2,8* mm, name)

c = canvas.Canvas(OUTPUT_PDF)

with open(CSV_PATH, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    reader.fieldnames = [field.strip() for field in reader.fieldnames] 

    for row in reader:
        name = row['name'].strip()
        photo = row['photo'].strip()
        title = row.get('title', '').strip()
        location = row.get('location', '').strip()
        photo_path = os.path.join(PHOTO_DIR, photo)

        c.setPageSize((PAGE_WIDTH, PAGE_HEIGHT))
        draw_id_card(c, name, photo_path)
        c.showPage()

c.save()
print(f" All ID cards saved to {OUTPUT_PDF}")
