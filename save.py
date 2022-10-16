import os

img_dir = 'D:/a_tianchi/mchar_test_a/'  # 测试图片路径
result_dir = 'D:/a_tianchi/yolov5/yolov5-master/runs/detect/exp11/labels/'  # 识别结果路径
out_dir = 'D:/a_tianchi/mchar_test_result/'  # 输出的 txt 文件路径


# 获取列表的第二个元素
def takeSecond(elem):
    return elem[1]


# 读取
dirs = os.listdir(img_dir)

fp = open(out_dir + 'result8.csv', mode="w+", encoding="utf-8")

for file in dirs:

    txtFileName = file.title().split(".")[0] + '.txt'

    listCode = []

    if os.access(result_dir + txtFileName, os.F_OK):

        with open(result_dir + txtFileName, "r") as f:
            for line in f.readlines():
                tmp = line.split(' ')
                listCode.append((tmp[0], float(tmp[1])))

                # 按tmp[1]从小到大排序
    listCode.sort(key=takeSecond)

    theNumber = ''
    for code in listCode:
        theNumber += code[0]

        # 保存到文件，格式：fileName,theNumber
    fileName = file.title()
    fp.write(fileName + ',' + theNumber + '\n')

fp.close()
