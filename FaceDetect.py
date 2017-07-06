
from os import walk
from PIL import Image
import face_recognition

imagePathInput = "F:/project_python/ClassificationFace/MyTam/"  # duong dan anh input
cascPath = "haarcascade_frontalface_default.xml"
imagePathOutput = "F:/project_python/ClassificationFace/MyTamOutPut/"  # duong dan output


# def detect_face(filepath):
#     faceCascade = cv2.CascadeClassifier(cascPath)
#     image = cv2.imread(filepath)
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#
#
#     faces = faceCascade.detectMultiScale(
#         gray,
#         scaleFactor=1.1,
#         minNeighbors=5,
#         minSize=(30, 30),
#         flags = cv2.CASCADE_SCALE_IMAGE
#     )
#
#     # Draw a rectangle around the faces
#     for (x, y, w, h) in faces:
#         return x , y , w , h , image


def detect_face(fileName):

    print fileName

    image = face_recognition.load_image_file(fileName)

    face_locations = face_recognition.face_locations(image)

    for face_location in face_locations:
        # Print the location of each face in this image
        top, right, bottom, left = face_location
        print("Face Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))

        face_image = image[top:bottom, left:right]
        pil_image = Image.fromarray(face_image)
        pil_image = pil_image.resize((128, 128), Image.ANTIALIAS)
    return pil_image;


# def crop_image(x , y , w , h , image,filename):
#     crop_img = image[y:y+h, x:x+w]
#     cv2.imwrite(imagePathOutput+filename, crop_img)

for (dirpath, dirnames, filenames) in walk(imagePathInput):
    for filename in filenames:
        print(filename)
        # filepath = imagePathInput+filename
        # x , y , w , h , image = detect_face(filepath)
        # crop_image(x , y , w , h , image,filename)
        detect_face(filename)
