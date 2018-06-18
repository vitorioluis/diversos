# -*- coding: utf-8 -*-
import base64

try:
    import qrcode
except ImportError:
    from pip._internal import main
    main(['install','--user', 'qrcode'])
    import qrcode

try:
    import PIL
except ImportError:
    from pip._internal import main
    main(['install','--user','pillow'])
    import PIL
    


class GerarQRCode:
    def __init__(self, msg, CaminhoImg="D:/filename.png"):
        self._img=CaminhoImg
        self._msg=msg

    def versao_curta(self):
        img = make(self._msg)
        img.save(self._img)


    def versao_full(self):
        qr = QRCode(version=20, error_correction=ERROR_CORRECT_L)
        qr.add_data(self._msg)
        qr.make()
        im = qr.make_image()
        im.save(self._img)

    def img_to_string(self):
        """Transforma uma imagem em string."""
        with open(self._img,"rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())

        #f = open("d:/jpg1_b64.txt", "wb")
        #f.write(encoded_string)
        #f.close()

        return encoded_string

    def string_to_img(self,string,imagem='d:/qrcode.png'):
        """Converte string em Imagem."""
        img = base64.b64decode(string)
        saida = open(imagem,"wb")
        saida.write(img)
        saida.close()

if __name__  == '__main__':
    app=GerarQRCode(msg='https://play.google.com/store/apps/details?id=br.com.oparoquiano.app')
    app.versao_curta()
    app.versao_full()
    
    
