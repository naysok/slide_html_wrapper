from pdf2image import convert_from_path


PDF_PATH = '../slide_pdf/slide.pdf'

images = convert_from_path(PDF_PATH)

i = 0

for image in images:
    i += 1
    image.save('../PRESENTATION/slide_images/slide_{}.png'.format(i), 'png')
    print(i)


print("convert all!")