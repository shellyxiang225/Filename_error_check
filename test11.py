from openpyxl import Workbook

# 创建一个新的工作簿
workbook = Workbook()

# 选择默认的活动工作表
worksheet = workbook.active

# 假设您的列表为char_list
char_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

# 将每两个字符组合为一组，并逐个写入Excel行
for i in range(0, len(char_list), 3):
    row = [char_list[i], char_list[i + 1],cha]
    worksheet.append(row)

# 保存工作簿到文件
workbook.save('output.xlsx')