import numpy as np
from PIL import ImageGrab
import cv2 as cv
import time
import os
from getkeys import key_check
train = np.load('training_data.npy', allow_pickle=True)

print(train[100])
print(os.path.abspath("."))

# w = [1,0,0,0,0,0,0,0,0]
# s = [0,1,0,0,0,0,0,0,0]
# a = [0,0,1,0,0,0,0,0,0]
# d = [0,0,0,1,0,0,0,0,0]
# wa = [0,0,0,0,1,0,0,0,0]
# wd = [0,0,0,0,0,1,0,0,0]
# sa = [0,0,0,0,0,0,1,0,0]
# sd = [0,0,0,0,0,0,0,1,0]
# nk = [0,0,0,0,0,0,0,0,1]

# def key_to_output(keys):
#     output = [0,0,0,0,0,0,0,0,0]

#     if 'W' in keys:
#         output = w
#     elif 'S' in keys:
#         output = s
#     elif 'A' in keys:
#         output = a
#     elif 'D' in keys:
#         output = d
#     elif 'W' in keys and 'A' in keys:
#         output = wa
#     elif 'W' in keys and 'D' in keys:
#         output = wd
#     elif 'S' in keys and 'A' in keys:
#         output = sa
#     elif 'S' in keys and 'D' in keys:
#         output = sd
#     else: 
#         output = nk
#     return output

# file_name = 'training_data.npy'

# if os.path.isfile(file_name):
#     print('File exist')
#     training_data = list(np.load(file_name))
# else:
#     print('File does not exist')
#     training_data = []

# def main():
#     for i in list(range(4))[::-1]:
#         print(i+1)
#         time.sleep(1)

#     while (True):
#         screen = np.array(ImageGrab.grab(bbox=(0, 0, 1920/2, 540)))
#         screen = cv.cvtColor(screen, cv.COLOR_BGR2GRAY)
#         screen = cv.resize(screen, (80,60))
#         keys = key_check()
#         output = key_to_output(keys)
#         training_data.append([screen, output])

#         if len(training_data) % 500 == 0:
#             print(len(training_data))
#             np.save(file_name, training_data)
#         # cv.imshow('window', cv.cvtColor(screen, cv.COLOR_BGR2RGB))

#         # if cv.waitKey(25) & 0xFF == ord('q'):
#         #     cv.destroyAllWindows()
#         #     break

# main()