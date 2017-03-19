import cv2


class FaceRecognizer:
    def __init__(self, faces):
        self.faces = faces

    def face_recoginaze(self):
        cascade_path = "/usr/local/opt/opencv/share/OpenCV/haarcascades/haarcascade_frontalface_alt.xml"
        color = (255, 255, 255)

        image_gray = cv2.cvtColor(self.faces, cv2.cv.CV_BGR2GRAY)

        cascade = cv2.CascadeClassifier(cascade_path)
        facerect = cascade.detectMultiScale(image_gray, scaleFactor=1.1, minNeighbors=1, minSize=(1, 1))

        print "face rectangle"
        print facerect

        if len(facerect) > 0:
            for rect in facerect:
                cv2.rectangle(self.faces, tuple(rect[0:2]), tuple(rect[0:2] + rect[2:4]), color, thickness=2)
        else:
            print("no face")

        cv2.imshow("detected.jpg", self.faces)
        any_key = raw_input('Press any key to exit >> ')
