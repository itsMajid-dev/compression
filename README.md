
# Project Title

Data compression with Python and the LZW algorithm


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
x.compressing_informations()
```
The original file size, the compressed file size and the compressed percentage return to the dictionary.
