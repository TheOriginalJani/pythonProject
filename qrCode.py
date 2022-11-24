import qrcode
from PIL import Image
from pyzbar.pyzbar import decode

path = ''


def encoder():
    try:
        file = open(path, 'r')
        fileData = file.read()
    finally:
        file.close()
    qr = qrcode.QRCode(version=1, box_size=25, border=1)
    qr.add_data(fileData)
    qr.make(fit=True)
    img = qr.make_image(fill_color='#4B0082', back_color='#00FF7F')
    pngName = path[:len(path) - 4] + '.png'
    img.save(pngName)
    return pngName


def decoder():
    decoded = decode(Image.open(path))
    decodedData = decoded[0].data.decode('utf-8')
    txtName = path[:len(path) - 4] + '.txt'
    file = open(txtName, 'w', encoding='utf-8')
    file.write(decodedData)
    file.close()
    return txtName
