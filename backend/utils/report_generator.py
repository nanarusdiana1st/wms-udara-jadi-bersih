import pandas as pd
from io import BytesIO
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.units import inch
from sqlalchemy.orm import Session
from ..models import Material

def generate_monthly_report_excel(db: Session, year: int, month: int) -> BytesIO:
    materials = db.query(Material).all()
    data = []
    for m in materials:
        data.append({
            'Name': m.name,
            'Code': m.code,
            'Stock': m.stock_quantity,
            'Value': m.stock_quantity * m.price_per_unit
        })
    df = pd.DataFrame(data)
    output = BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, sheet_name='Inventory', index=False)
    output.seek(0)
    return output

def generate_monthly_report_pdf(db: Session, year: int, month: int) -> BytesIO:
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4)
    elements = []

    styles = getSampleStyleSheet()
    title = Paragraph(f"Monthly Report - {year}-{month}", styles['Title'])
    elements.append(title)
    elements.append(Spacer(1, 12))

    materials = db.query(Material).all()
    data = [['Name', 'Code', 'Stock', 'Value']]
    for m in materials:
        data.append([m.name, m.code, m.stock_quantity, f"{m.stock_quantity * m.price_per_unit:.2f}"])
    
    table = Table(data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))

    elements.append(table)
    doc.build(elements)
    buffer.seek(0)
    return buffer