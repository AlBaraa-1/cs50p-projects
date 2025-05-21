from fpdf import FPDF
import csv

def main():
    name = input("Name: ")
    pdf = FPDF(unit="mm", format="A4")
    pdf.add_page()

    # Title
    pdf.set_font("Arial", size=50)
    pdf.cell(0, 30, "CS50 Shirtificate", ln=True, align="C")
    pdf.ln(10)

    # Shirt
    pdf.image("shirtificate.png", x=5, y=50, w=200, h=220)

    # Overlay name in white
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(10, 50 + (130//2))
    pdf.set_font("Arial", size=30)
    pdf.cell(0, 10, f"{name} took CS50", align="C")
    # Save
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
