from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

def generate_pdf(request):
    template = get_template('pdf_template.html')
    html = template.render({'title': 'My PDF', 'message': 'Hello from Django PDF,A PDF, or Portable Document Format, '
    'is a file format used to present and exchange documents reliably, '
    'regardless of the software, hardware, or operating system used. '
    'PDFs can contain text, fonts, images, interactive elements like buttons and form fields,'
    ' and even audio and video. They are widely used because they preserve document formatting and layout,'
    ' ensuring a consistent appearance across different devices and platforms.  '})
    
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="report.pdf"'

    pisa_status = pisa.CreatePDF(html, dest=response)
    
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

from django.shortcuts import render
def home(request):
    return render(request, 'home.html')
