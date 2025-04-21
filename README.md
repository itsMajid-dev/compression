
# Project Title

Data compression with Python and the LZW algorithm  
With the help of this code, you can reduce the size of html and xml text files by up to **90%** !

## About the LZW algorithm : 

[WikiPedia](https://en.wikipedia.org/wiki/Lempel%E2%80%93Ziv%E2%80%93Welch)


## Usage/Compression:

```python
import main 

x= main.Encoding()
x.load('a.txt')
x.compress()
x.save('ac')

```

## Usage/Decompress:

```python
import main 

x= main.Decoding()
x.load('ac')
x.decompress()
x.save('a.txt')

```



## Compression information:

```python
x = main.Encoding()
i = x.compressing_informations()
```
The original file size, the compressed file size and the compressed percentage return to the dictionary.



## File validation:

```python
x = main.Decoding()
v = x.valid("a.txt" , 'ac')

```
Returns True if the compressed file is equal to the original file.




## GUI version : 
<p align="center">
  <img src="https://raw.githubusercontent.com/itsMajid-dev/compression/refs/heads/main/screenshots/Screenshot%20(668).png" alt="compressing" />
</p>

> The installation file and images are in this repository. This file is a **beta** version that will eventually compress 1.2 MB text files.
