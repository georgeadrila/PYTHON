import qrcode

def generate_qr_code(text, file_name):
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 10,
        border = 4,
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="white", back_color="black")
    img.save(file_name)

text = "https://www.adygadgets.com#products"
file_name = "adygadgets.png"
generate_qr_code(text, file_name)
print(f"QR Code for {text} is saved as {file_name}")
