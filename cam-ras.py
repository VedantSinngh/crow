from ultralytics import YOLO
import cv2

# Load the YOLO model
model = YOLO("/home/pi/best.pt")  # Path to your trained model on the Pi

# Start webcam (usually /dev/video0)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to grab frame.")
        break

    # Run detection
    results = model(frame)

    # Optional: Only print crow detections
    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])
            label = model.names[cls]
            if label.lower() == "crow":
                print("Crow detected!")

    # Display results
    annotated_frame = results[0].plot()
    cv2.imshow("Crow Detection", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
