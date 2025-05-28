import cv2


class CVProcessor:
    #
    def to_grayscale(self, img):
        return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    def apply_blur(self, img, ksize=5):
        return cv2.GaussianBlur(img, (ksize, ksize), 0)
