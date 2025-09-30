from fpdf import FPDF

def main():
    name = input("Name: ")
    
    # Create PDF
    pdf = FPDF()
    pdf.add_page()
    
    # Add header
    pdf.set_font("helvetica", "B", 36)
    pdf.cell(0, 40, "CS50 Shirtificate", ln=True, align="C")
    
    # Add shirt image (centered)
    pdf.image("shirtificate.png", x=10, y=60, w=190)
    
    # Add name on top of the shirt (white text)
    pdf.set_font("helvetica", "B", 24)
    pdf.set_text_color(255, 255, 255)  # White
    pdf.set_xy(0, 120)
    pdf.cell(0, 10, f"{name} took CS50", align="C")
    
    # Save PDF
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()