
from flask import Flask, render_template, request, send_file
from scipy import  misc
from panorama import Panaroma
import imutils
import cv2
from database import *
import random
path=r"C:\Users\hp\OneDrive\Desktop\project\ezyzip (2)\ezyzip (2)\security\static\\"
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
    s4 = img[:, 3 * slize:]

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




def filedecrypt():

    filename = []


    from sa_aes import  dec_process_image

    dec_process_image(path + "face1enc.bmp", path + "face1d.bmp")
    dec_process_image(path + "face2enc.bmp", path + "face2d.bmp")
    dec_process_image(path + "face3enc.bmp", path + "face3d.bmp")
    dec_process_image(path + "face4enc.bmp", path + "face4d.bmp")

    print("1111")




    filename.append(
        r"C:\Users\hp\OneDrive\Desktop\project\ezyzip (2)\ezyzip (2)\ezyzip\static\face1d.bmp")
    filename.append(
        r"C:\Users\hp\OneDrive\Desktop\project\ezyzip (2)\ezyzip (2)\ezyzip\static\face2d.bmp")
    filename.append(
        r"C:\Users\hp\OneDrive\Desktop\project\ezyzip (2)\ezyzip (2)\ezyzip\static\face3d.bmp")
    filename.append(
        r"C:\Users\hp\OneDrive\Desktop\project\ezyzip (2)\ezyzip (2)\ezyzip\static\face4d.bmp")

    images = []
    no_of_images = 4

    for i in range(no_of_images):
        images.append(cv2.imread(filename[i]))

    # We need to modify the image resolution and keep our aspect ratio use the function imutils

    # for i in range(no_of_images):
    #     images[i] = imutils.resize(images[i], width=400)
    #
    # for i in range(no_of_images):
    #     images[i] = imutils.resize(images[i], height=400)


    panaroma = Panaroma()
    if no_of_images == 2:
        (result, matched_points) = panaroma.image_stitch([images[0], images[1]], match_status=True)
    else:
        (result, matched_points) = panaroma.image_stitch([images[no_of_images - 2], images[no_of_images - 1]],
                                                         match_status=True)
        for i in range(no_of_images - 2):
            (result, matched_points) = panaroma.image_stitch([images[no_of_images - i - 3], result], match_status=True)

    # to show the got panaroma image and valid matched points

    #
    # cv2.imshow("Keypoint Matches", matched_points)
    # cv2.imshow("Panorama", result)

    # to write the images
    cv2.imwrite("Matched_points.jpg", matched_points)
    cv2.imwrite(path+"Panorama_image.jpg", result)

    return send_file(path+"Panorama_image.jpg")


    #
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


