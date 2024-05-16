import os
import uuid
from faker import Faker
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer,PageBreak
from reportlab.lib.styles import getSampleStyleSheet

def create_random_pdf(file_name, num_pages=3):
    fake = Faker()
    doc = SimpleDocTemplate(file_name, pagesize=letter)
    story = []
    styles = getSampleStyleSheet()
    doc.title = fake.sentence()
    for _ in range(num_pages):
        story.append(Spacer(1, 12))
        story.append(Paragraph(fake.sentence(), styles['Title']))
        story.append(Spacer(1, 12))

        for _ in range(18):
            story.append(Paragraph(fake.sentence(nb_words=50), styles['BodyText']))
        if _ < num_pages - 1:
            story.append(PageBreak())

    doc.build(story)

def generate_pdfs(num_pdfs, output_dir="generated"):
    os.makedirs(output_dir, exist_ok=True)

    for _ in range(num_pdfs):
        # Generate a random file name
        file_name = os.path.join(output_dir, f"{uuid.uuid4()}.pdf")
        create_random_pdf(file_name)

# Generate 5 PDFs
generate_pdfs(3)