from openpyxl import Workbook
wb=Workbook()
ws=wb.active

# 作为stream保存,需要使用NamedTemporayFile
'''
from tempfile import NamedTemporaryFile
wb1=Workbook()
with NamedTemporaryFile() as tmp:
    wb1.save(tmp.name)
    tmp.seek(0)
    stream=tmp.read()'''

# You can specify the attribute template=True, to save a workbook as a template:
'''wb.template=True
wb.save('document_template.xltx')'''
# or set this attribute to False (default), to save as a document
'''wb.template=False
wb.save('document.xlsx', as_template=False)'''


# 最简单且安全的保存文件方法是save()方法，此方法保存在Pyhon的根目录下
# 注意：会自动覆盖已经存在文件名的文件，并且毫无提示
wb.save('保存文件及数据.xlsx')
