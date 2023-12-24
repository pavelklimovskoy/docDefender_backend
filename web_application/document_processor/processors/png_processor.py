import cv2
import numpy as np
from PIL import Image
import easyocr
from IPython.display import display
from docDefender_backend import settings


class PNGProcessor:

    # def __init__(self, document_name: str, input_path, output_path):
    #     self.document_name: str = document_name
    #     self.output_document_name: str = f'{self.document_name}'
    #     self.input_path = input_path
    #     self.output_path = output_path

    def __init__(self, document_name: str):
        self.document_name: str = document_name
        self.output_document_name: str = f'{self.document_name}'

    def anonymize_doc(self):
        # input_path = self.input_path
        # output_path = self.output_path

        im = cv2.imread(f'{settings.MEDIA_ROOT}{self.document_name}')

        hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
        blue_lower = np.array([100, 80, 110])
        blue_higher = np.array([160, 174, 221])
        mask = cv2.inRange(hsv, blue_lower, blue_higher)

        text_lower = np.array([0, 0, 0])
        text_higher = np.array([30, 30, 30])
        text_mask = cv2.inRange(im, text_lower, text_higher)

        output_image = im.copy()

        for y in range(im.shape[0]):
            for x in range(im.shape[1]):
                if mask[y, x] > 0 and y > 1 and x > 1 and y < im.shape[0] - 2 and x < im.shape[1] - 2:
                    output_image[text_mask > 0] = im[text_mask > 0]
                    output_image[y - 2:y + 3, x - 2:x + 3] = [255, 255, 255]

        reader = easyocr.Reader(['ru'])
        results = reader.readtext(f'{settings.MEDIA_ROOT}{self.document_name}')

        for (bbox, text, prob) in results:
            if any(char.isdigit() for char in text):
                (top_left, top_right, bottom_right, bottom_left) = bbox
                top_left = tuple(map(int, top_left))
                bottom_right = tuple(map(int, bottom_right))
                cv2.rectangle(output_image, top_left, bottom_right, (255, 255, 255), -1)

        cv2.imwrite(f'{settings.MEDIA_ROOT}anon_{self.document_name}', output_image)

    def save_document(self) -> None:
        pass

        pass