from face_recognizer import FaceRecognizer
import cv2


def load_face_images():
    image_path = "dataset/test.png"
    return image_path


def create_faces_image():
    images = cv2.imread(load_face_images())
    face_recognize = FaceRecognizer(images)
    face_recognize.face_recoginaze()


if __name__ == '__main__':
    create_faces_image()
