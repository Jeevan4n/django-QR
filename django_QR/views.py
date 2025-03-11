from django.shortcuts import render, HttpResponse
from .forms import QRCodeForm
import qrcode
import os
from django.conf import settings

def generate_qr_code(request):
    if request.method == 'POST':
        form = QRCodeForm(request.POST)
        if form.is_valid():
            res_name = form.cleaned_data['restaurant_name']
            url = form.cleaned_data['url']

            # Generate QR code image using qrcode module
            qr = qrcode.make(url)

            # Create a filename based on the restaurant name
            file_name = res_name.replace(" ", "_").lower() + '_menu.png'

            # Define the folder inside static where the QR code will be saved
            qr_folder = os.path.join(settings.BASE_DIR, 'static', 'qr_codes')
            if not os.path.exists(qr_folder):
                os.makedirs(qr_folder)
            
            # Complete file path
            file_path = os.path.join(qr_folder, file_name)

            # Save the QR code image to the file path
            qr.save(file_path)

            # Build the URL to access the QR code image
            qr_code_url = '/static/qr_codes/' + file_name

            # Pass the restaurant name and QR code URL to the template
            context = {
                'res_name': res_name,
                'qr_code_url': qr_code_url,
            }
            return render(request, 'qr_result.html', context)
    else:
        form = QRCodeForm()

    context = {'form': form}
    return render(request, 'generate_qr_code.html', context)
