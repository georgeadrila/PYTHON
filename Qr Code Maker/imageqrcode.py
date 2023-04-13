import qrcode

def generate_qr_code(text, output_path):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(output_path)

# Generate QR code with text
text = "wa.me/256757591879"
output_path = "qr_code.png"
generate_qr_code(text, output_path)
