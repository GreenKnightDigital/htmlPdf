#!/usr/bin/python3
import pdfkit
import sys

if len(sys.argv) == 2 and sys.argv[1] == 'help':
    print("Usage: htmlPdf.py input_html output_pdf")
    print("Converts an HTML file to a PDF using pdfkit and wkhtmltopdf.")
    sys.exit()

if len(sys.argv) != 3:
    print("Error: Incorrect number of arguments. Use 'htmlPdf.py help' for usage instructions.")
    sys.exit(1)

inputHtml = sys.argv[1]
outputPdf = sys.argv[2]

# Path to the wkhtmltopdf executable the defaut for this is set for Linux distro
wkhtmltopdf_path = '/usr/local/bin/wkhtmltopdf'

# Path to your HTML file
html_file_path = inputHtml

# Path to the output PDF file
pdf_file_path = outputPdf

# Configure PDF options
options = {
    'quiet': '',
}

# Convert HTML to PDF
pdfkit.from_file(html_file_path, pdf_file_path, configuration=pdfkit.configuration(wkhtmltopdf=wkhtmltopdf_path), options=options)

print(f'Conversion complete. PDF saved to {pdf_file_path}')
