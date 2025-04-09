import string 


lower_chr = string.ascii_lowercase
uper_chr = string.ascii_uppercase
number_chr = string.digits
symbol_chr = '\n\t :;.,/\()<>?!&"_-=\'$@#{}+[]'

partions = {}

n = 0
# Add any character and number to the dictionary
for i in lower_chr:
    partions[i]=n
    n+=1
for i in uper_chr:
    partions[i]=n
    n+=1
for i in number_chr:
    partions[i]=n
    n+=1
for i in symbol_chr:
    partions[i]=n
    n+=1


max_code = len(partions)
