import num 


class Encoding:
    def __init__(self , data):
        self.data = data
        self.__size = 0 

    def convert_to_code(self):
        """Convert each substring to a number (0 to num.max_code)"""
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
        """Convert any number to a number between 0 and 255 then convert to bytes"""
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
        """Save byte data as a file"""
        byte_data = self.compress()
        with open(file_name , 'wb') as file:
            file.write(byte_data)

    def compressing_informations(self):
        """Return size and compression percentage information"""
        normal_size = len(self.data)
        compressed_size = self.__size
        compression_percent = (normal_size - compressed_size) / normal_size *100
        return{'normal_size':f'{normal_size} B',
             'compressed_size':f"{compressed_size} B",
             'compression_percent':f"{compression_percent}%",
        }
    