from ultralytics import YOLO
import cv2

# Load your trained model
model = YOLO(r"C:\Users\vedaa\OneDrive\Desktop\Final Model\ved\best (1).pt")  # Note the raw string (r"") to handle backslashes

# Start webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Run detection
    results = model(frame)

    # Optionally filter only crow detections (uncomment below to activate)
    # for r in results:
    #     for box in r.boxes:
    #         cls = int(box.cls[0])
    #         if model.names[cls] == "crow":
    #             print("Crow detected!")

    # Show detection results
    annotated_frame = results[0].plot()
    cv2.imshow("Crow Detection", annotated_frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
