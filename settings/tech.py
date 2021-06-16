def save_pdf_page_by_number_to_location(file_path, text,page_number):
    import PyPDF2
    import os
    reader = PyPDF2.PdfFileReader(file_path)
    # print(reader.documentInfo)
    print(reader.numPages)
    writer = PyPDF2.PdfFileWriter()
    my_page = reader.getPage(page_number)
    writer.addPage(my_page)
    print(my_page)

    output_filename = f"C:\\Users\\Anastasia Siedykh\\Documents\\Backup\\python_projects\\lutz\\part_one\\saved_2\\{page_number}_{text}.pdf"
    with open(output_filename, 'wb') as output:
        writer.write(output)
    #os.startfile(output_filename)
    return output_filename

