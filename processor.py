import re
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import LETTER
from reportlab.lib import colors

#validate_data
def validate_data(name, email, phone):
    if len(name.strip()) < 2:
        return False, "Name is too short."
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return False, "Invalid email format."
    if len(re.sub(r'\D', '', phone)) < 10:
        return False, "Phone number must be at least 10 digits."
    return True, "Success"


# COMMON SECTION WRITER 
def draw_section(c, title, content, y):
    c.setFont("Helvetica-Bold", 11)
    c.drawString(50, y, title)
    y -= 15
    c.setFont("Helvetica", 10)

    for line in content.split("\n"):
        c.drawString(60, y, line)
        y -= 14
    return y - 10


#  ATS STANDARD TEMPLATE 
def draw_ats_standard(data, filename):
    c = canvas.Canvas(filename, pagesize=LETTER)
    width, height = LETTER

    y = height - 50  # starting point

    # Header
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, y, data["name"])
    y -= 20

    c.setFont("Helvetica", 10)
    c.drawString(50, y, f"{data['email']} | {data['phone']}")
    y -= 30

    # Section helper
    def section(title, content):
        nonlocal y
        c.setFont("Helvetica-Bold", 12)
        c.drawString(50, y, title)
        y -= 15

        c.setFont("Helvetica", 10)
        text = c.beginText(50, y)
        for line in content.split("\n"):
            text.textLine(line)
            y -= 12
        c.drawText(text)
        y -= 10

    section("EDUCATION", data["edu"])
    section("EXPERIENCE", data["exp"])
    section("SKILLS", data["skills"])
    section("PROJECTS", data["project"])
    section("CERTIFICATIONS", data["certificate"])

    c.save()


# MODERN SIDEBAR TEMPLATE
def draw_modern_sidebar(data, filename):
    c = canvas.Canvas(filename, pagesize=LETTER)
    width, height = LETTER

    # Sidebar
    c.setFillColor(colors.lightgrey)
    c.rect(0, 0, 170, height, fill=1)
    c.setFillColor(colors.black)

    y = height - 50

    # Sidebar content
    c.setFont("Helvetica-Bold", 14)
    c.drawString(20, y, data["name"])
    y -= 20

    c.setFont("Helvetica", 9)
    c.drawString(20, y, data["email"])
    y -= 12
    c.drawString(20, y, data["phone"])
    y -= 20

    c.setFont("Helvetica-Bold", 11)
    c.drawString(20, y, "SKILLS")
    y -= 15

    text = c.beginText(20, y)
    for skill in data["skills"].split(","):
        text.textLine(f"- {skill.strip()}")
        y -= 12
    c.drawText(text)

    # Main content
    y = height - 50
    x = 190

    def main_section(title, content):
        nonlocal y
        c.setFont("Helvetica-Bold", 12)
        c.drawString(x, y, title)
        y -= 15

        c.setFont("Helvetica", 10)
        text = c.beginText(x, y)
        for line in content.split("\n"):
            text.textLine(line)
            y -= 12
        c.drawText(text)
        y -= 10

    main_section("EDUCATION", data["edu"])
    main_section("EXPERIENCE", data["exp"])
    main_section("PROJECTS", data["project"])

    c.save()

#  CREATIVE TEMPLATE 
def draw_creative(data, filename):
    c = canvas.Canvas(filename, pagesize=LETTER)
    width, height = LETTER

    # ===== HEADER =====
    c.setFillColor(colors.HexColor("#1f4fd8"))  # blue header
    c.rect(0, height - 90, width, 90, fill=1)

    c.setFillColor(colors.white)
    c.setFont("Helvetica-Bold", 20)
    c.drawString(40, height - 50, data["name"])

    c.setFont("Helvetica", 10)
    c.drawString(40, height - 70, f"{data['email']} | {data['phone']}")

    #  BODY 
    y = height - 120
    x = 40

    def section(title, content):
        nonlocal y
        c.setFillColor(colors.black)
        c.setFont("Helvetica-Bold", 13)
        c.drawString(x, y, title)
        y -= 8

        c.setLineWidth(1)
        c.setStrokeColor(colors.HexColor("#1f4fd8"))
        c.line(x, y, x + 200, y)
        y -= 15

        c.setFont("Helvetica", 10)
        text = c.beginText(x, y)
        for line in content.split("\n"):
            text.textLine(line)
            y -= 12
        c.drawText(text)
        y -= 10

    # SECTIONS 
    section("EDUCATION", data["edu"])
    section("EXPERIENCE", data["exp"])
    section("PROJECTS", data["project"])
    section("CERTIFICATIONS", data["certificate"])
    section("SKILLS", data["skills"].replace(",", " | "))

    c.save()
