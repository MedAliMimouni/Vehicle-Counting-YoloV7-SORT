This app is demonstrate simple vehicle counting on toll road or highway.

# Vehicle Counting YoloV7 SORT

### Steps to run Code
- Clone the repository.
```
git clone https://github.com/MedAliMimouni/Vehicle-Counting-YoloV7-SORT.git
```
- Goto the cloned folder.
```
cd Vehicle-Counting-YoloV7-SORT
```
- Create a virtual envirnoment (Recommended, If you dont want to disturb python packages)
```
### For Linux Users
python3 -m venv yolov7objtracking
source yolov7objtracking/bin/activate

### For Window Users
python3 -m venv yolov7objtracking
cd yolov7objtracking
cd Scripts
activate
cd ..
cd ..
```
- Upgrade pip with mentioned command below.
```
pip install --upgrade pip
```
- Install requirements with mentioned command below.
```
pip install -r requirements.txt
```
- Run the code with mentioned command below (by default, pretrained [yolov7](https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7.pt) weights will be automatically downloaded into the working directory if they don't already exist).
```
# for detection only
python detect.py --weights yolov7.pt --source "your video.mp4"


#for specific classes (Cars, motorcycle, bus and track)
python detect_count_track.py --weights yolov7.pt --source "your video.mp4" --classes 2 3 4 6
```

- Output file will be created in the ```working-dir/runs/detect/obj-tracking``` with original filename

#### demo example: https://youtu.be/vc66Fy0dARQ
#### Original video: https://drive.google.com/file/d/16ViS0tIUEAQPNS7NMqNrrIQAURGAVByJ/view?usp=share_link



 ### References
 - https://github.com/WongKinYiu/yolov7
 - https://github.com/abewley/sort
 - https://github.com/RizwanMunawar/yolov7-object-tracking
