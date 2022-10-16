import torch

num_dict = torch.load('runs/train/exp5/weights/best.pt')
for k, v in num_dict.item():  # k 参数名 v 对应参数值
        print(k, v)

# python train.py --batch-size -1
# --data data/test.yaml --cfg models/yolov5s.yaml --weights yolov5s.pt --workers 16 --cache disk