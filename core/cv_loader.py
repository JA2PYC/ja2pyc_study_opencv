import cv2


class CVLoader:
    # Load Image
    def load_image(self, path):
        return cv2.imread(path)

    # Load Video
    def load_video(self, path):
        return cv2.VideoCapture(path)
