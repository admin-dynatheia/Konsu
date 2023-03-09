import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox

video = cv2.VideoCapture(0)
labels = []

while True:
    ret, frame = video.read()
    # Bounding box.
    # the cvlib library has learned some basic objects using object learning
    # usually it takes around 800 images for it to learn what a phone is.
    bbox, label, conf = cv.detect_common_objects(frame)

    output_image = draw_bbox(frame, bbox, label, conf)

    cv2.imshow("Detection", output_image)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break