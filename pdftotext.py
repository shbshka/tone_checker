from tika import parser

def extract_text_from_pdf(file):
    return parser.from_file(file)