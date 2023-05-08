from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.image("shirtificate.png", 10, 69, 180)
        self.set_font("helvetica", "I", 69)
        self.cell(0, 69, "CS50 Shirtificate", align="C")
        self.ln(2)

def pdfer(name):
    pdf = PDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    pdf.set_font("helvetica", "B", 16)
    pdf.cell(40, 10, f"{name} took CS50", align="C")
    pdf.output("shirtificate.pdf")

def main():
    pdfer(input("Name: "))

if __name__ =="__main__":
    main()
