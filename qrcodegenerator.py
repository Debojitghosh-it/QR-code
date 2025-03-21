import qrcode

qr = qrcode.make('Hello World')

qr.save('hello.png')

print('QR Code generated successfully')