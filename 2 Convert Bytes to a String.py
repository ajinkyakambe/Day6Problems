# 2. Python Program to Convert Bytes to a String

# bytes data 49 20 77 61 6e 74 20 74 6f 20 63 68 65 63 6b 20 62 79 74 65 73

# using the map method we will check bytes

# asic decimal data
bytesdata = [73, 32, 119, 97, 110, 116, 32, 116, 111, 32, 99, 104, 101, 99, 107, 32, 98, 121, 116, 101, 115]

bytetostring = ''.join(map(chr, bytesdata))
print(bytetostring)