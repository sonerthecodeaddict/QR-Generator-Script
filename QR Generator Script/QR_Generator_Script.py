import qrcode
import qrcode.image.svg


#Hizli kullanim
qr_image = qrcode.make("github.com/sonerthecodeaddict")
qr_image.save("github.png")


#Gelismis kullanim
qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_H,
                   box_size=15,
                   border=1)

qr.add_data("github.com/sonerthecodeaddict - github.com/soner2160p")
qr.make(fit=True)
qr_image_2 = qr.make_image(fill_color="red", back_color="blue")
qr_image_2.save("github-advenced.png")


"""
renklerin deðiþebilmesi için pillow kütüphanesi yüklü olmalý
"""

#svg
factory = qrcode.image.svg.SvgPathImage
svg_image = qrcode.make("Bu dosya svg formatinda", image_factory=factory)
svg_image.save("svg example.svg")
