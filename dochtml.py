"""program to convert doc to html"""
import mammoth
import webbrowser
with open("Article.docx", "rb") as docx_file:
    result = mammoth.convert_to_html(docx_file)
    html = result.value # The generated HTML
with open("output.html","w") as f:
    f.write(html)
webbrowser.open("file://d:/python36/output.html",new=2)

