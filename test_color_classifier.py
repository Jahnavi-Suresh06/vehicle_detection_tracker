
import cv2
from VehicleDetectionTracker.color_classifier.color_classifier import Classifier

video = cv2.VideoCapture("traffic.mp4")

if not video.isOpened():
    raise RuntimeError("Could not open traffic.mp4")

# Read a frame containing vehicles
success, frame = video.read()
video.release()

if not success:
    raise RuntimeError("Could not read a video frame")

# Crop a vehicle from the frame.
# Adjust these coordinates if the crop does not contain a car.
vehicle_crop = frame[300:700, 700:1100]

if vehicle_crop.size == 0:
    raise RuntimeError("Vehicle crop is empty")

classifier = Classifier()
predictions = classifier.predict(vehicle_crop)

print("Top 3 predicted colours:")
for item in predictions:
    print(
        f"Colour: {item['color']}, "
        f"Probability: {float(item['prob']):.4f}"
    )
