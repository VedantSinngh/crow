

````markdown
# YOLO NCNN Object Detection

This project demonstrates how to export a YOLO model to the NCNN format and run object detection using a Python script. The script `yolo_detect.py` enables detection on various input sources, such as USB webcam, video files, and directories of images.

---

## 🔧 Requirements

- Python 3.7+
- NCNN-compatible YOLO model
- `wget` (or manually download `yolo_detect.py`)
- USB webcam or test media (images/videos)
- pip install ultralytics opencv-python numpy


---

## 🚀 Setup & Usage

### 1. Export YOLO model to NCNN format

Use the following command to export your model:

```bash
yolo export model=your_model.pt format=ncnn
````

This will generate NCNN model files (e.g., `.param`, `.bin`) from your `.pt` file.

### 2. Download detection script

```bash
wget https://ejtech.io/code/yolo_detect.py
```

This script handles loading the NCNN model and running detection on the selected source.

### 3. Run the Detector

#### a. Run on USB camera (e.g., webcam)

```bash
python yolo_detect.py --model=yolo11n_ncnn_model --source=picamera0 --resolution=640x480
```

* `--model`: folder or prefix of NCNN model files (e.g., `yolo11n_ncnn_model.param` and `.bin`)
* `--source`: input source (`usb0` refers to the default webcam)
* `--resolution`: width x height of camera feed

#### b. Run on a video file

```bash
python yolo_detect.py --model=yolo11n_ncnn_model --source=test_video.mp4
```

#### c. Run on a directory of images

```bash
python yolo_detect.py --model=custom_ncnn_model --source=img_dir
```

---

## 📁 Folder Structure

```plaintext
project/
├── your_model.pt
├── yolo_detect.py
├── yolo11n_ncnn_model.param
├── yolo11n_ncnn_model.bin
└── img_dir/
    ├── image1.jpg
    ├── image2.jpg
    └── ...
```

---

## 📌 Notes

* Ensure `ncnn` is installed or included within the Python wrapper used in `yolo_detect.py`.
* Modify the script as needed for specific preprocessing or postprocessing requirements.
* For accurate performance, use the same input resolution your model was trained on.

---

## 📄 License

This project follows the MIT License unless otherwise specified.

```
