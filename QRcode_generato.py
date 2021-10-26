import qrcode

# Link for website
input_data = "https://pasqualebuonocore.wixsite.com/pasq"

# Creating an instance of qrcode
# version:
#       - It defines size of the QR Code generated within a range of [1-40]. 
#       - The higher this value, bigger the dimension of the generated QR Code image.
# box_size: 
#       - This parameter defines the size of each box in pixels.
# border: 
#       - The border defines the thickness of the border.
qr = qrcode.QRCode(version=1, box_size=10, border=1)

qr.add_data(input_data)
qr.make(fit=True)
img = qr.make_image(fill='black', back_color='white')
img.save('output/WebSite_qrcode.png')