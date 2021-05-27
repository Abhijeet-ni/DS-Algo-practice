import  pyqrcode

s = "https://www.youtube.com/watch?v=pTFZFxd4hOI"
qr = pyqrcode.create(s,error= 'L', version=25, mode='binary')
qr.svg("docker_tutorial.svg", scale=8)

