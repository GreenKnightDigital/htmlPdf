# HTML to PDF Converter

This is a simple Python script that converts an HTML file to a PDF using the pdfkit library and wkhtmltopdf tool.

## Requirements

- Python 3.x
- pdfkit library (install using `pip3 install pdfkit`)
- wkhtmltopdf tool (download from https://wkhtmltopdf.org/downloads.html and ensure it's in your system's PATH)

## Usage

1. Clone or download this repository to your computer.

2. Open a terminal or command prompt.

3. `pip3 install -r requirements.txt`

4. Install wkhtmltopdf tool from https://wkhtmltopdf.org/downloads.html for your system. You will need to modify line 18 of htmlPdf.py to fit your system needs. The default is set for Linux.

5. Navigate to the directory where the `htmlPdf.py` script is located.

6. Run the script with the following command:

   ```shell
   python3 htmlPdf.py {Your html doc} {Name you want for the PDF}
