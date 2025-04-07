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
    
    def compress(self):
        codes = self.convert_to_code()
        byte = bytearray()
        for c in codes:
            hight_byte = (c>>8) & 0xFF
            low_byte = c & 0xFF
            byte.append(hight_byte)
            byte.append(low_byte)
            self.__size = len(byte)
        return byte
    
    def save(self , file_name):
        byte_data = self.compress()
        with open(file_name , 'wb') as file:
            file.write(byte_data)
            

    
    


o = Encoding('abcab')
o.compress()
