import json

import cv2

json_dir = 'D:/a_tianchi/mchar_train.json'  # json文件路径
out_dir = 'D:/a_tianchi/yolov5/yolov5-master/labels/mchar_train/'  # 输出的 txt 文件路径
img_dir = 'D:/a_tianchi/yolov5/yolov5-master/images/mchar_train/'  # 图片所在路径


def main():
    # 读取 json 文件数据
    with open(json_dir, 'r') as load_f:
        content = json.load(load_f)
        # 循环处理
    for t, value in content.items():
        tmp = t.split('.')
        filename = out_dir + tmp[0] + '.txt'

        # 左上角x
        left = value['left']
        # 左上角y
        top = value['top']
        # 字符高度
        height = value['height']
        # 字符宽度
        width = value['width']
        # 字符值
        label = value['label']

        # 图片宽和高
        image_cv = cv2.imread(img_dir + tmp[0] + '.png')
        image_height = image_cv.shape[0]
        image_width = image_cv.shape[1]

        for index in range(len(left)):
            bbox0 = left[index]
            bbox1 = top[index]
            bbox2 = bbox0 + width[index]
            bbox3 = bbox1 + height[index]

            theLabel = label[index]

            # 计算 yolo 数据格式所需要的中心点的 相对 x, y 坐标, w,h 的值
            x = (bbox0 + bbox2) / 2 / image_width
            y = (bbox1 + bbox3) / 2 / image_height
            w = (bbox2 - bbox0) / image_width
            h = (bbox3 - bbox1) / image_height
            fp = open(filename, mode="a+", encoding="utf-8")
            file_str = str(theLabel) + ' ' + str(round(x, 6)) + ' ' + str(round(y, 6)) + ' ' + str(round(w, 6)) + \
                       ' ' + str(round(h, 6))

            fp.write(file_str + '\r\n')
            fp.close()


if __name__ == '__main__':
    main()
