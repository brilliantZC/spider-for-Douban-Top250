# -*- coding = utf-8 -*-
# @Time : 2021/4/6 9:10
# @Author : brilliantZC
# @File : testXwlt.py
# @Software : PyCharm

import xlwt

# wookbook = xlwt.Workbook(encoding="utf-8")  # 创建wookbook对象
# wooksheet = wookbook.add_sheet("sheet1")  # 创建工作表
# wooksheet.write(0, 0, 'hello')  # 写入数据，第一行参数"行"，第二个参数"列"，第三个参数内容
# wookbook.save('student.xls')

wookbook = xlwt.Workbook(encoding="utf-8")  # 创建wookbook对象
wooksheet = wookbook.add_sheet("sheet1")
for i in range(1, 10):
    for j in range(i, 10):
        k = i*j
        wooksheet.write(i, j, "%d*%d=%d"%(i,j,k))
wookbook.save('student.xls')

# for i in range(1, 10):
#     for j in range(i, 10):
#         k = i*j
#         print("%d*%d=%d"%(i,j,k),end="\t")
#     print()
