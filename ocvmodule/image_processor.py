import cv2

class ImageProcessor:
    def load(self, path):
        return cv2.imread(path)

    def resize(self, image, width=None, height=None):
        h, w = image.shape[:2]
        if width and not height:
            ratio = width / w
            return cv2.resize(image, (width, int(h * ratio)))
        elif height and not width:
            ratio = height / h
            return cv2.resize(image, (int(w * ratio), height))
        elif width and height:
            return cv2.resize(image, (width, height))
        return image

    def to_gray(self, image):
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    def save(self, image, path):
        cv2.imwrite(path, image)
