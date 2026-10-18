# Text to Image using Python
# Pillow: Image, ImageDraw, ImageFont

from PIL import Image, ImageDraw, ImageFont

txt = input("Enter Your Text: ")

# Create Image
image = Image.new("RGB", (800, 300), "white")

# Create Drawing Object
draw = ImageDraw.Draw(image)

# Load Font
font = ImageFont.load_default()

# Set Left and Right Margins
left_margin = 50
right_margin = 50

# Calculate Available Width
available_width = 800 - left_margin - right_margin

# Break Text into Multiple Lines
words = txt.split()
wrapped_lines = []
current_line = ""

for word in words:
    test_line = current_line + " " + word if current_line else word
    text_width = draw.textbbox((0, 0), test_line, font=font)[2]

    if text_width <= available_width:
        current_line = test_line
    else:
        if current_line:
            wrapped_lines.append(current_line)
        current_line = word

if current_line:
    wrapped_lines.append(current_line)

# Draw Text Line by Line
y = 50

for line in wrapped_lines:
    draw.text((left_margin, y), line, fill="red", font=font)
    y += 25

# Save Image
image.save("text_image.png")

print("Image Generated Successfully!")