import os
import markdown2
import codecs

doc_path = '/usr/share/nginx/joukkoliikenne/dokumentaatio'

header_file = os.path.join(doc_path,'header.html')
with codecs.open(header_file,'rb','utf-8') as f:
    header = f.read()

footer_file = os.path.join(doc_path,'footer.html')
with codecs.open(footer_file,'rb','utf-8') as f:
    footer = f.read()
for fn in os.listdir(doc_path):
    if not fn.endswith('.md'):
        continue
    docfilepath = os.path.join(doc_path,fn)
    of = codecs.open(os.path.join(doc_path,fn.replace('.md','.html')),'wb','utf-8')
    of.write(header)

    doc_conv = markdown2.markdown_path(docfilepath)
    of.write(doc_conv)
    of.write(footer)
    of.close()
    print fn,'done'
