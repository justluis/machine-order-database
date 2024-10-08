from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate,Table, TableStyle,Image, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def create_pdf(inventory):
    pdf_filename='Hoist_Order.pdf'
    pdf= SimpleDocTemplate(pdf_filename)