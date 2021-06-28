#sudo apt-get libzbar0
#pip install pyzbar
#pip install pyzbar[scripts]
#pip install qrcode[pil]
##################################################
#import
import cv2
import matplotlib.pyplot as plt
import sys
from PIL import Image
from pyzbar.pyzbar import decode
import qrcode
##################################################
#image_read_1922_qrcode
img_bgr = cv2.imread('qrcode.jpg')
print(img_bgr.shape)
img_bgr=img_bgr[500:1400,250:1200,:]
plt.imshow(img_bgr)

#decode_qrcode
decode_data = decode(img_bgr)
print(decode_data)
print(type(decode_data))
#get_UTF-8
#UTF-82chinese
#SMSTO:1922:場所代碼：OOOO OOOO OOOO OOO \n本簡訊是簡訊實聯制發送，限防疫目的使用。
##################################################
#cread_new_qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

#new_qrcode_add_text
qr.add_data("SMSTO:1922:場所代碼：OOOO OOOO OOOO OOO \n本簡訊是簡訊實聯制發送，限防疫目的使用。\n\nXXXX店\n電話 ooxxxoooo\n手機 xxxxoooooo\n住址：OOOOOOOOOOOOOO")
qr.make(fit=True)

#save_new_qrcode
img = qr.make_image(fill_color="black", back_color="white")
print(img.size)
img.save("qrcode.png")
##################################################
#image_read_new_qrcode
#new_qrcode_add_alpha_channel
img = cv2.imread('qrcode.png')
print(img.shape)
img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
print(img.shape)
plt.imshow(img)
[m,n,o]=img.shape

#image_read_logo
logo_size = 250
logo = cv2.imread('logo.png',cv2.IMREAD_UNCHANGED)
plt.imshow(logo)
print(logo.shape)
plt.imshow(logo[:,:,3])

#cal_image_center
xmin=ymin=int((m/2)-(logo_size/2))
xmax=ymax=int((m/2)+(logo_size/2))

#logo_resize
#put_logo_into_new_qrcode
logo = cv2.resize(logo, (xmax-xmin, ymax-ymin), interpolation=cv2.INTER_AREA)
img_logo=img[xmin:xmax,ymin:ymax,:]
logo = Image.fromarray(logo)
img_logo = Image.fromarray(img_logo)
img_logo = Image.alpha_composite(img_logo, logo)
plt.imshow(img_logo)
img_logo = np.asarray(img_logo)
img[xmin:xmax,ymin:ymax,:]=img_logo

#save_new_qrcode_with_logo
im = Image.fromarray(img)
im.save("qrcode_logo.png")
