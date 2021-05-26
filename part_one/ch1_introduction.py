from settings.tech import save_pdf_page_by_number_to_location, pdf_file


if __name__ == '__main__':

     path = save_pdf_page_by_number_to_location(pdf_file,41)
     print(path)