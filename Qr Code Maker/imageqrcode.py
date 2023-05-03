import qrcode

def generate_qr_code(name, phone, email, website, whatsapp, twitter, instagram, output_path):
    # Create the vCard string
    vcard = f"BEGIN:VCARD\nVERSION:3.0\nFN:{name}\nTEL:{phone}\nEMAIL:{email}\nURL:{website}\n"
    if whatsapp:
        vcard += f"X-SOCIALPROFILE;TYPE=WhatsApp:{whatsapp}\n"
    if twitter:
        vcard += f"X-SOCIALPROFILE;TYPE=Twitter:{twitter}\n"
    if instagram:
        vcard += f"X-SOCIALPROFILE;TYPE=Instagram:{instagram}\n"
    vcard += "END:VCARD"

    # Generate the QR code with the vCard string as the data
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(vcard)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(output_path)

# Generate QR code with name, phone, email, website, WhatsApp, twitter, and Instagram as vCard
name = "George Adrian"
phone = "+256757591879"
email = "info@adygadgets.com"
website = "https://www.adygadgets.com"
whatsapp = "+256757591879"
twitter = "https://www.twitter.com/adygadgets"
instagram = "https://www.instagram.com/ady__gadgets"
output_path = "qr_code.png"
generate_qr_code(name, phone, email, website, whatsapp, twitter, instagram, output_path)
