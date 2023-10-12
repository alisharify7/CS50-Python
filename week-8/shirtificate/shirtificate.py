from fpdf import FPDF

class ShirtificatePDF(FPDF):
    """
    Cs50 ShirtificatePDF class
    """
    def __init__(self):
        super().__init__()
        self.image("./shirtificate.png", w=self.epw) #  15, 80, 180
        self.set_font("helvetica", "B", size=52)
        self.cell(0, 58, "CS50 Shirtificate", align="C")
        self.ln(20)
    
    def get_name_on_shirt(self, name:str):
        name = input("Name: ")
        self.name = name

    def make_shirt(self):
        self.add_page(orientation="portrait", format="A4")
        text = f"{self.name} took CS50"
        self.set_text_color(r=255,g=255,b=255)
        self.set_font("helvetica", size=24)
        self.cell(0, 213, text, align="C")
        self.output("shirtificate.pdf")

def main():
    pdf = ShirtificatePDF()
    pdf.get_name_on_shirt()
    pdf.make_shirt()

if __name__ == "__main__":
    main()