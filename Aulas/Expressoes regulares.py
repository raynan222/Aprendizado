import re #import regular expressions (regex)
"""

    REGEX101.COM

"""

strings = "o rato roeu a roupa do rei de roma"


patern = re.findall(r"[\w\.-]+@[\w\.-]+\.[\w\.-]+","joao.scar@dsaijds.com") # r -> RAW STRING \w caractere word "." caractere generico
if patern:
    print(patern)
else:
    print("padrao nao encontrado")