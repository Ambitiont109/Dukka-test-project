from celery import shared_task
from django.template.loader import render_to_string
from xhtml2pdf import pisa
import time


@shared_task(bind=True)
def generate_receipt_pdf(self, receipt_data=None):
    """
        Generate the 10 different pdfs from receipt data.        
    """
    task_id = self.request.id
    for i in range(10):
        html = render_to_string("receipt_template.html", receipt_data)
        file = open(f"generated_receipt_pdfs/{task_id}_{i + 1}.pdf", "w+b")
        pisa.CreatePDF(
            html,
            dest=file)
        file.close()
        time.sleep(1)
        self.update_state(state="PROGRESS", meta={'current': i + 1, 'total': 10})
