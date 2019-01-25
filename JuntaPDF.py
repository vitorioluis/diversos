
try:
    from PyPDF2 import PdfFileWriter, PdfFileReader
except:
    from pip._internal import main
    main(['install','--user', 'PyPDF2'])
    from PyPDF2 import PdfFileWriter, PdfFileReader
import os


DicArq = {}
Caminho = u'diretorio'
Novo = Caminho+'/Consolidado.pdf'
for path, subdirs, files in os.walk(Caminho):
    for name in files:        
        arquivo = str(os.path.join(path, name))                       
        DicArq[arquivo] = (arquivo.replace('\\','/'))

output = PdfFileWriter()
for arquivo in sorted(DicArq):
    arq = DicArq[arquivo]
    input1 = PdfFileReader(open(arq, "rb"))
    pageCount = input1.getNumPages()   
    for pg in range(0, pageCount):
        output.addPage(input1.getPage(pg))
output.addMetadata({u'/Title': Novo})
        
outputStream = open(Novo, "wb")
output.write(outputStream)
outputStream.close()
    

