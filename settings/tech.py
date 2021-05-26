def save_pdf_page_by_number_to_location(file_path, page_number):
    import PyPDF2
    import os
    reader = PyPDF2.PdfFileReader(file_path)
    # print(reader.documentInfo)
    # print(reader.numPages)
    writer = PyPDF2.PdfFileWriter()
    my_page = reader.getPage(page_number)
    writer.addPage(my_page)

    output_filename = f'saved\{page_number}.pdf'
    with open(output_filename, 'wb') as output:
        writer.write(output)
    os.startfile(output_filename)
    return output_filename

pdf_file = 'part1.pdf'