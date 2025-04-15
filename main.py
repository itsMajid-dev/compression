import num
import time 

class Encoding:
    def __init__(self):
        self.__size = 0 
        self.__start_time = time.time()
        self.__end_time = 0
        self.__control=False
        self.binary = 0
    
    def load(self , file):
        """Reading the data of the file to be compressed"""
        with open(file , mode='r') as file:
            self.data = file.read()

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
            self.__end_time=time.time()
            self.__control = True
            self.binary = byte
        return byte
    
    def save(self , file_name):
        """Save byte data as a file"""
        if self.__control:
            byte_data = self.binary
            with open(file_name , 'wb') as file:
                file.write(byte_data)
            self.__end_time=time.time()
            return
        else:
            raise AttributeError("There is no compressed data to be stored.")

    def compressing_informations(self):
        """Return size and compression percentage information"""
        normal_size = len(self.data)
        compressed_size = self.__size
        compression_percent = (normal_size - compressed_size) / normal_size *100
        return{'normal_size':f'{normal_size} B',
             'compressed_size':f"{compressed_size} B",
             'compression_percent':f"{compression_percent} %",
             'Elapsed_time' : f"{round(self.__end_time - self.__start_time ,3) } s"
        }

class Decoding:
    def __init__(self):
        self.__control = False
        self.data = 0

    def load(self , compress_file):
        """Reading a compressed file"""
        with open(compress_file , mode='rb') as file:
            self.byte_data = file.read()

    def convert_to_code(self):
        """Convert each byte to a number between zero and 255."""
        codes = []
        for i in range(0 , len(self.byte_data) , 2):
            hight = self.byte_data[i]
            low = self.byte_data[i+1]
            code = (hight<<8)+low
            codes.append(code)
        return codes
    
    def decompress(self):
        """Convert each code to its own character from the num.partions dictionary."""
        string = []
        reversed_tabel = {v: k for k, v in num.partions.items()}
        list_of_code = self.convert_to_code()
        init_code = list_of_code[0]
        init_str = reversed_tabel[init_code]
        string.append(init_str)
        nex_code = max(reversed_tabel.keys()) + 1

        for code in list_of_code[1:]:
            if code in reversed_tabel:
                entry = reversed_tabel[code]
            else:
                entry = init_str + init_str[0]
            string.append(entry)
            reversed_tabel[nex_code] = init_str + entry[0]
            nex_code += 1
            init_str = entry
            self.data = ''.join(string)
            self.__control = True

        return ''.join(string)
    
    def save(self , file_name):
        """saveing file. """
        if self.__control:
            data = self.data
            with open(file_name , mode='w') as file:
                file.write(data)
        else:
            raise AttributeError("There is no data to store!")
            



            





    
    
        
