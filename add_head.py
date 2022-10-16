import pandas as pd

data = pd.read_csv('result8.csv', sep=',', names=['file_name', 'file_code'])
# 排序
data = data.sort_values(by='file_name')
# 取消第一列的id
data = data.set_index('file_name')
# 将code转为int类型,不然会变成 111.0
data['file_code'] = data['file_code'].fillna(0)
data['file_code'] = data['file_code'].round(0).astype('int')
data.to_csv('result9.csv')
