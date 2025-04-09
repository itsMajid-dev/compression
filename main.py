import num
import time 


class Encoding:
    def __init__(self):
        self.__size = 0 
        self.__start_time = time.time()
        self.__end_time = 0
        self.excepts = []
    
    def load(self , file):
        """Reading the data of the file to be compressed"""
        with open(file , mode='r') as file:
            self.data = file.read()

    def convert_to_code(self):
        """Convert each substring to a number (0 to num.max_code)"""
        # ABCABDAB
        output = []  
        tabel = num.partions
        next_code = num.max_code
        char = ''
        # TABLE      :     {AB : 83 , BC:84 , CA:85 , DAB:86 , DA:87} , 
        # C          :     A  , B , C , A , B , D  , A  , B
        # char       :       '' , A , B , C , A , AB , D  , A , AB
        # substring  :  A  , AB , BC , CA , AB , DAB , DA , AB 
        #output      : [0 , 1 , 2 , 83 ,3 , 83] => [A,B,C,?,D,?]
        for c in self.data:
            substring = char+c
            if substring in tabel:
                char=substring
            else:
                try:
                    output.append(tabel[char])
                except:
                    self.excepts.append(char)
                    
                tabel[substring]=next_code
                next_code+=1
                char=c
        output.append(tabel[substring])
        
        return output
        
        
    def compress(self):
        """Convert any number to a 12 bit number"""
        codes = self.convert_to_code()
        byte = bytearray()
        buffer = 0 
        bit_in_buffer = 0 
        for code in codes:
            buffer = (buffer<<12)| code
            bit_in_buffer+=12
            while bit_in_buffer>=8 :
                bit_in_buffer-=8
                b = (buffer>>bit_in_buffer) & 0xFF
                byte.append(b)
        if bit_in_buffer>0:
            b = (buffer << (8-bit_in_buffer)) & 0xFF
            byte.append(b)
        self.__size = len(byte)
        self.__end_time=time.time()
        return byte
      
        
    def save(self , file_name):
        """Save byte data as a file"""
        byte_data = self.compress()
        with open(file_name , 'wb') as file:
            file.write(byte_data)
        self.__end_time=time.time()

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
    def load(self , compress_file):
        """Reading a compressed file"""
        with open(compress_file , mode='rb') as file:
            self.byte_data = file.read()

    def convert_to_code(self):
        """Convert 12-bit packed bytes back to original codes"""
        codes = []
        buffer = 0
        bits_in_buffer = 0
        
        for byte in self.byte_data:
            buffer = (buffer << 8) | byte
            bits_in_buffer += 8
            
           
            while bits_in_buffer >= 12:
                bits_in_buffer -= 12
                code = (buffer >> bits_in_buffer) & 0xFFF  
                codes.append(code)
        return codes
    
    def decompress(self):
        """Convert each code to its own character from the num.partions dictionary."""
        
        string = [] # [A ,B , C , AB , D ]   # ABCABDABAB
        reversed_tabel = {v: k for k, v in num.partions.items()} # {0:A , 1:B , 2:C , 3:D , 83 : AB , 84:BC ,85:CD }
        list_of_code = self.convert_to_code() # [0 , 1 , 2 , 83 ,3 , 83]
        init_code = list_of_code[0] # 0 
        
        init_str = reversed_tabel[init_code] # A , B  , C 
        string.append(init_str)
        nex_code = max(reversed_tabel.keys()) + 1 # 82 

        for code in list_of_code[1:]: #[ 1 , 2 , 83 ,3 , 83]
            if code in reversed_tabel:
                entry = reversed_tabel[code] # B , C ,AB , D 
            else:  
                entry = init_str + init_str[0]
            string.append(entry)
            reversed_tabel[nex_code] = init_str + entry[0] # AB , BC ,CD 
            nex_code += 1
            init_str = entry

        return ''.join(string)
    
    def save(self , file_name):
        """saveing file. """
        data = self.decompress()
        with open(file_name , mode='w') as file:
            file.write(data)
            



            





    
    
        
