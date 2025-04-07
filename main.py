import num 


class Encoding:
    def __init__(self , data):
        self.data = data
        self.__size = 0 

    def convert_to_code(self):
        output = []  
        tabel = num.partions
        next_code = num.max_code
        char = ''
        for c in self.data:
            substring = char+c
            if substring in tabel:
                char=substring
            else:
                output.append(tabel[char])
                tabel[substring]=next_code
                next_code+=1
                char=c
        output.append(tabel[substring])
        return output


o = Encoding('abcab')
