import string 

#کاراکتر ها
lower_chr = string.ascii_lowercase
uper_chr = string.ascii_uppercase
number_chr = string.digits
symbol_chr = '\n\t :;.,/\()<>?!&"_-=\'$@#{}+'

# دیکشنری کاراکتر و عدد اختصاصی هر کاراکتر
partions = {}

n = 0
# افزودن کاراکتر و عدد اختصاصی به دیکشنری
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

# تعداد کاراکتر ها 
max_code = len(partions)
# for i,j in partions.items():
#     print(i,j,sep='   :   ')