import re

password = "True" if re.fullmatch(r'\d+[A-Z][a-z]*[A-Z][a-z]*', "2AgboolaAa")else "False"
print(password)
