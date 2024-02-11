from llmsherpa.readers import LayoutPDFReader

llmsherpa_api_url = "http://localhost:5001/api/parseDocument?renderFormat=all"
pdf_url = "1910.13461.pdf" # also allowed is a file path e.g. /home/downloads/xyz.pdf
pdf_reader = LayoutPDFReader(llmsherpa_api_url)
doc = pdf_reader.read_pdf(pdf_url)