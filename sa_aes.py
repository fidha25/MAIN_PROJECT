from PIL import Image
from Crypto.Cipher import AES

filename = "a.bmp"
filename_out = "tux_encrypted"
format = "BMP"
key = "aaaabbbbccccdddd"
key_bytes = key.encode('utf-8')
import pyaes
def pad(data):
    return data + b"\x00" * (16 - len(data) % 16)

def convert_to_RGB(data):
    r, g, b = tuple(map(lambda d: [data[i] for i in range(0, len(data)) if i % 3 == d], [0, 1, 2]))
    pixels = tuple(zip(r, g, b))
    return pixels

def process_image(filename,outfilename):
    # Opens image and converts it to RGB format for PIL
    im = Image.open(filename)
    data = im.convert("RGB").tobytes()
    original = len(data)
    mn=aes_ecb_encrypt(key_bytes, pad(data))[:original]
    print("okkkkkkkkkkkkkkkkkkk")
    new = convert_to_RGB(mn)
    im2 = Image.new("RGBA", im.size)
    im2.putdata(new)
    im2.save(outfilename, format)

# def process_image(filename,outfilename,rr):
#     # Opens image and converts it to RGB format for PIL
#     im = Image.open(filename)
#     data = im.convert("RGB").tobytes()
#     original = len(data)
#     # mn=aes_ecb_encrypt(key, pad(data))[:original]
#     aes = pyaes.AESModeOfOperationCTR(key)
#     ciphertext = aes.encrypt(data)
#     print("okkkkkkkkkkkkkkkkkkk")
#     new = convert_to_RGB(mn)
#     im2 = Image.new("RGBA", im.size)
#     im2.putdata(new)
#     im2.save(outfilename, format)




def dec_process_image(filename,filedec):
    # Opens image and converts it to RGB format for PIL
    im = Image.open(filename)
    data = im.convert("RGB").tobytes()
    original = len(data)
    mn=aes_ecb_decrypt(key,pad(data))[:len(data)]
    print(mn)
    new = convert_to_RGB(mn)
    im2 = Image.new(im.mode, im.size)
    im2.putdata(new)
    im2.save(filedec, format)



# ECB
def aes_ecb_encrypt(key, data, mode=AES.MODE_ECB):
    aes = AES.new(key, mode)
    new_data = aes.encrypt(data)
    return new_data

def aes_ecb_decrypt(key, data, mode=AES.MODE_ECB):
    aes = AES.new(key, mode)
    new_data = aes.decrypt(data)
    return new_data



# process_image("i","o")
# dec_process_image("in.BMP","savepath")




# def aes_cbc_encrypt(key, data, mode=AES.MODE_CBC):
#     IV = "A" * 16  # We'll manually set the initialization vector to simplify things
#     aes = AES.new(key, mode, IV)
#     new_data = aes.encrypt(data)
#     return new_data
#
# def aes_cbc_decrypt(key, data, mode=AES.MODE_CBC):
#     IV = "A" * 16  # We'll manually set the initialization vector to simplify things
#     aes = AES.new(key, mode, IV)
#     new_data = aes.decrypt(data)
#     return new_data
