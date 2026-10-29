from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

NAVY = "#102A43"
TEAL = "#1F9D8B"
CREAM = "#F5F7F4"

def font(size, bold=False):
    candidates = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ]
    return ImageFont.truetype(candidates[0], size)

def wrap(draw, text, f, max_width):
    words, lines, line = text.split(), [], ""
    for word in words:
        test = (line + " " + word).strip()
        if draw.textbbox((0,0), test, font=f)[2] <= max_width: line = test
        else: lines.append(line); line = word
    if line: lines.append(line)
    return lines

def make_quote(text, author="[Executive Name]", output="quote_graphic.png"):
    img = Image.new("RGB", (1080,1080), CREAM); d = ImageDraw.Draw(img)
    d.rectangle((0,0,1080,22), fill=TEAL); d.rectangle((0,1058,1080,1080), fill=NAVY)
    qf, af = font(58, True), font(28, False)
    lines = wrap(d, text, qf, 850); y = 300
    for line in lines:
        d.text((115,y), line, font=qf, fill=NAVY); y += 78
    d.text((115, 820), "— " + author, font=af, fill=TEAL)
    d.text((115, 930), "REAL ESTATE / INSIGHT", font=font(22, True), fill=NAVY)
    img.save(output, quality=95)

if __name__ == "__main__":
    make_quote("A property can be attractive over ten years and wrong for a twelve-month mandate.")
