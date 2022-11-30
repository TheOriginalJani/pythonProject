import qrcode
from PIL import Image
from pyzbar.pyzbar import decode

path = ''


# Szöveges fálból QR-kódot hoz létre
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


# QR-kódból szöveges fájlt hoz létre
def decoder():
    decoded = decode(Image.open(path))
    decodedData = decoded[0].data.decode('utf-8')

    # legelegánsabb megoldás
    decodedData = decodedData.replace('Ã¡', 'á')
    decodedData = decodedData.replace('Ã©', 'é')
    decodedData = decodedData.replace('Ã­', 'í')
    decodedData = decodedData.replace('Ã³', 'ó')
    decodedData = decodedData.replace('Ã¶', 'ö')
    decodedData = decodedData.replace('Å‘', 'ő')
    decodedData = decodedData.replace('Ãº', 'ú')
    decodedData = decodedData.replace('Ã¼', 'ü')
    decodedData = decodedData.replace('Å±', 'ű')

    txtName = path[:len(path) - 4] + '.txt'
    file = open(txtName, 'w', encoding='utf-8')
    file.write(decodedData)
    file.close()
    return txtName
