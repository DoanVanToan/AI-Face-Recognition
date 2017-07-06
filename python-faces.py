import os

from PIL import Image
import face_recognition
from os import listdir
from os.path import isfile, join

def detect_face(infile):

        image = face_recognition.load_image_file(infile)

        face_locations = face_recognition.face_locations(image)

        for face_location in face_locations:
            # Print the location of each face in this image
            top, right, bottom, left = face_location
            print("Face Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom,right))

            face_image = image[top:bottom, left:right]
            pil_image = Image.fromarray(face_image)
            pil_image = pil_image.resize((128, 128), Image.ANTIALIAS)
            return pil_image;


