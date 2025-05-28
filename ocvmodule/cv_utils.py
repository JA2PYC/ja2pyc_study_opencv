import cv2
import os
from datetime import datetime


class CVUtils:

    def save_image(self, img, filename, output_dir):
        os.makedirs(output_dir, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        full_name = f"{filename}_{timestamp}.jpg"
        path = os.path.join(output_dir, full_name)
        cv2.imwrite(path, img)
        return full_name, path
