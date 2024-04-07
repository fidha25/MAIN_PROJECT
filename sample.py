
from flask import Flask, render_template, request, send_file
from scipy import  misc
from panorama import Panaroma
import imutils
import cv2
from database import *
import random
path=r"C:\Users\hp\OneDrive\Desktop\proj\ezyzip (2)\ezyzip\static\\"

path1=r"C:\Users\hp\OneDrive\Desktop\proj\ezyzip (2)\ezyzip\static\CHECK\\"
from flask import request
import time
import os
import imageio
from sa_aes import process_image

from flask import request
import time
import os
import imageio
from sa_aes import process_image

def filepost(uploaded_file_path,id,original_filename,ext):
    # files = request.files["file"]

    # # Save the uploaded file
    # original_filename, file_extension = os.path.splitext(files.filename)
    # upload_timestamp = time.strftime("%Y%m%d-%H%M%S")
    # uploaded_file_path = f"{original_filename}_{upload_timestamp}{file_extension}"
    # files.save(path + uploaded_file_path)

    # Read the image
    img = imageio.imread(path + uploaded_file_path)
    height, width, k = img.shape

    # Cut the image in half
    slize = width // 4
    s1 = img[:, :slize + (slize // 2)]
    s2 = img[:, slize: (2 * slize) + (slize // 2)]
    s3 = img[:, (2 * slize): (3 * slize) + (slize // 2)]
    s4 = img[:, (3 * slize):]
    
  
    

    # Save each half with the same name as the original file
    face1_path = path + f"{original_filename}_face1.bmp"
    face2_path = path + f"{original_filename}_face2.bmp"
    face3_path = path + f"{original_filename}_face3.bmp"
    face4_path = path + f"{original_filename}_face4.bmp"

    imageio.imwrite(face1_path, s1)
    imageio.imwrite(face2_path, s2)
    imageio.imwrite(face3_path, s3)
    imageio.imwrite(face4_path, s4)

    # Perform image processing using sa_aes module
    process_image(face1_path, path + f"{original_filename}_face1enc.bmp")
    process_image(face2_path, path + f"{original_filename}_face2enc.bmp")
    process_image(face3_path, path + f"{original_filename}_face3enc.bmp")
    process_image(face4_path, path + f"{original_filename}_face4enc.bmp")
    p1="/static/"+original_filename+"_face1enc.bmp"
    p2="/static/"+original_filename+"_face2enc.bmp"
    p3="/static/"+original_filename+"_face3enc.bmp"
    p4="/static/"+original_filename+"_face4enc.bmp"
    ogp="/static/"+ext


    qa="insert into image_upload values(NULL,'%s','%s','%s','%s','%s','%s')"%(id,ogp,p1,p2,p3,p4)
    r1=insert(qa)

    return r1




def filedecrypt(img1, img2, img3, img4, imga1, imga2, imga3, imga4):

    filename = []
    from sa_aes import  dec_process_image

    # Decrypt images
    dec_process_image(path + imga1, path1 + img1)
    dec_process_image(path + imga2, path1 + img2)
    dec_process_image(path + imga3, path1 + img3)
    dec_process_image(path + imga4, path1 + img4)

    # Add decrypted image paths to filename list
    filename.append(path1 + img1)
    filename.append(path1 + img2)
    filename.append(path1 + img3)
    filename.append(path1 + img4)

    # Read images
    images = [cv2.imread(file) for file in filename]

    # Stitch images
    panorama = Panaroma()
    if len(images) == 2:
        (result, matched_points) = panorama.image_stitch([images[0], images[1]], match_status=True)
    else:
        (result, matched_points) = panorama.image_stitch([images[-2], images[-1]], match_status=True)
        for i in range(len(images) - 2):
            (result, matched_points) = panorama.image_stitch([images[-i - 3], result], match_status=True)

    # Find contours of non-black regions
    gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Get bounding box of contours
    x, y, w, h = cv2.boundingRect(contours[0])

    # Crop image
    new_image = result[y:y+h, x:x+w]

    # Save cropped image
    cv2.imwrite(r"C:\\Users\\hp\\OneDrive\\Desktop\\proj\\ezyzip (2)\\ezyzip\\static\\CHECK\\" + "Panorama_image.jpg", new_image)

    return "OK"

    #
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()




