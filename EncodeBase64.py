import base64
import sys

with open("C:\\img\\eiffel.jpg", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read())
print(encoded_string)

for i in range(0,10,2):
  print(i)

line = "62 29 64 63 31 64 63 34 64 65 30 60 66 27 59 63 31 62 61 31 62 63 30 61 63 30 59 64 31 58 64 30 61 61 30 58 65 30 56 64 32 59 61 31 59 62 30 60 63 30 62 65 32 64 65 32 61 64 29 58 61 29 57 64 30 56 65 29 58 64 30 61 66 30 61 71 31 66 67 33 67 65 33 63 64 35 62 62 32 62 68 31 64 68 35 66 70 31 65 70 31 63 71 33 65 70 34 68 68 33 67 74 37 69 74 37 69 70 36 69 70 36 70 71 37 67 71 36 67 72 34 69 74 35 70 70 34 70 69 34 67 70 35 65 67 34 63 67 32 65 67 33 66 69 37 67 69 36 66 66 35 63 67 35 64 67 32 64 71 32 66 70 35 66 69 35 65 67 32 65 68 34 65 71 36 66 69 35 65 70 37 68 71 36 69 71 34 67 71 36 66 70 38 68 67 37 68 68 32 63 67 30 64 60 28 64 57 28 58 56 24 56 51 21 53 46 22 47 45 22 49 51 24 54 54 25 51 54 25 55 55 27 57 58 30 59 54 32 56 54 30 52 57 29 51 58 29 54 60 30 58 60 29 58 58 28 58 59 27 56 57 29 56 60 30 60 63 31 61 67 31 66 70 34 71 69 37 70 70 36 68 70 38 67 69 38 67 71 36 71 70 35 67 67 36 70 68 37 69 69 36 66 66 32 63 67 30 57 68 31 58 66 33 61 67 32 62 64 34 65 63 35 66 65 35 62 66 34 58 66 35 64 65 36 68 62 33 66 62 32 65 66 33 66 66 33 65 64 32 64 63 35 64 64 35 67 62 31 63 65 32 60 67 33 64 61 32 65 64 32 66 64 33 65 65 32 65 65 30 64 62 30 63 61 33 62 65 33 63 68 32 64 67 32 65 65 36 68 70 36 69 70 35 72 65 34 70 66 32 65 68 33 65 68 37 69 67 37 69 70 37 67 70 36 66 72 38 67 70 37 64 70 36 63 70 35 64 68 36 66 70 39 68 71 39 65 71 37 66 71 39 71 68 38 67 71 37 70 73 36 71 71 37 67 69 38 67 70 39 71 72 37 69 74 38 73 75 38 73 76 39 71 76 41 74 74 42 73 75 42 74 76 41 74 76 42 74 80 44 78 79 42 76 76 40 75 73 39 72 74 40 70 72 36 69 73 36 69 69 35 68 63 34 63 63 36 62 62 33 61 62 32 60 62 30 59 62 30 57 59 30 56 59 29 58 57 32 62 57 31 61 62 30 57 66 32 60 64 32 63 64 32 66 65 34 66 63 34 63 68 34 65 70 35 67 68 36 69 69 35 70 74 36 69 73 35 67 70 36 67 67 37 66 70 36 68 71 35 68 72 36 68 70 36 70 70 39 68 69 39 67 68 38 67 68 37 68 73 40 71 74 39 70 72 38 69 73 37 68 74 38 71 72 38 71 68 38 66 68 35 64 67 36 68 66 37 70 70 39 72 66 37 67 66 37 68 71 37 69 69 38 67 67 38 67 64 36 66 65 36 67 69 37 69 72 38 69 69 38 71 69 38 72 73 38 70 73 40 71 74 37 68 76 38 70 72 38 67 69 35 64 71 34 68 70 33 68 72 37 67 71 37 63 71 38 67 70 38 69 70 35 67 69 35 65 68 37 66 68 36 65 69 36 64 68 36 64 65 38 67"
print(len(line.split(' ')))
