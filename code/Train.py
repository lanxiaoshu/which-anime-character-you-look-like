from ultralytics import YOLO

model = YOLO("yolo-cls/yolov8x-cls.pt")
if __name__ == '__main__':
    model.train(data='dataset', epochs=100, batch=-1, imgsz=150) # 可根据需要设置参数