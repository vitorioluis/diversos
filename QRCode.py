# -*- coding: utf-8 -*-
import base64

try:
    from qrcode import QRCode, make, image, ERROR_CORRECT_L
except ImportError:
    from pip._internal import main

    main(['install', '--user', 'qrcode'])
    from qrcode import QRCode, make, image, ERROR_CORRECT_L

try:
    import PIL
except ImportError:
    from pip._internal import main

    main(['install', '--user', 'pillow'])
    import PIL


class GerarQrCode:
    def __init__(self, msg, CaminhoImg="D:/"):
        self.__caminho_img = CaminhoImg
        self.__msg = msg

    def versao_curta(self, nome_img='qr_simples'):
        nome_img += '.png'
        img = make(self.__msg)
        img.save(self.__caminho_img + nome_img)

    def versao_full(self, nome_img='qr_complexo'):
        nome_img += '.png'
        qr = QRCode(version=20, error_correction=ERROR_CORRECT_L)
        qr.add_data(self.__msg)
        qr.make()
        im = qr.make_image()
        im.save(self.__caminho_img + nome_img)

    def img_to_string(self):
        """Transforma uma imagem em string."""
        with open(self.__caminho_img, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())

        # f = open("d:/jpg1_b64.txt", "wb")
        # f.write(encoded_string)
        # f.close()

        return encoded_string

    def string_to_img(self, string, imagem='d:/qrcode.png'):
        """Converte string em Imagem."""
        img = base64.b64decode(string)
        saida = open(imagem, "wb")
        saida.write(img)
        saida.close()


if __name__ == '__main__':
    app = GerarQrCode(msg='www.meusite.com.br')
    app.versao_curta()
    app.versao_full()
