from huffman import HuffmanCoding
import sys
import time 

path = "sample.txt"
time_start = time.time()

h = HuffmanCoding(path)
output_path = h.compress()
decom_path = h.decompress(output_path)

time_end = time.time()
print(time_end-time_start)