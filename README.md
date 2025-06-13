# ID Card Generator

## Overview
This project generates a PDF file containing custom ID cards for employees. Each ID card includes the employee's photo and name, overlaid on a pre-defined ID template.

## Prerequisites
- Python 3
- Pillow (PIL Fork)
- ReportLab

To install the required Python packages, run:
```
pip install pillow reportlab
```

## Inputs
1. `template.png`: A pre-defined ID template image (PNG format).
2. `employee_data.csv`: A CSV file containing employee details with the columns: `name` and `photo`.
3. `photos/`: A folder containing all employee ID photos referenced in the CSV file.


## Usage
1. Place the following in the same directory:
   - `template.png`
   - `employee_data.csv`
   - `photos/` folder with all employee images
   - `generate_id_cards.py` script

2. Run the script with:
```
python generate_id_cards.py
```

3. The script will generate a PDF named `employee_id_cards.pdf` in the current directory, with one ID card per employee listed in the CSV file.

## Customization
- You can modify the font size and font path by editing the `setFont()` line and `font_path` variable in the script.
- The positions for the photo and name placement can also be adjusted using the `photo_x`, `photo_y`, and `drawCentredString()` parameters.

## Output
- The output PDF will have the size of a standard credit card (85.6mm × 54mm), with each page containing one ID card.

