# -*- coding = utf-8 -*-
# @Time : 2021/4/5 14:37
# @Author : brilliantZC
# @File : testRe.py
# @Software : PyCharm

# 正则表达式：字符串模式，判断字符串是否符合一定的标准

import re
# 1.创建模式对象
# pat = re.compile("AA") # 此处的AA是正则表达式，用来取验证其他的字符串
# m = pat.search("")   # search字符串被校验的内容
# m = pat.search("ABBAA")  # <re.Match object; span=(3, 5), match='AA'>
# m = pat.search("AABCAADDCCBAAA") # search方法，进行比对查找 <re.Match object; span=(0, 2), match='AA'>

# print(m)

# 2.没有模式对象
# m = re.search("asd","Aasd")  # 前面的字符串是规则（模板），后面的字符串是被校验的对象
# print(m)

# print(re.findall("a", "ASDaDFGAa"))  # 前面的字符串是规则（正则表达式），后面的字符串是被校验的对象
# print(re.findall("[A-Z]", "ASDaDFGAa"))
# print(re.findall("[A-Z]+", "ASDaDFGAa"))

# sub
print(re.sub("a", "A", "abcdcasd"))  # 在第三个字符串中，找到a用A替换 ：AbcdcAsd

# 建议在正则表达式中，前面被比较的字符串前面加上r,不用担心转义字符的问题
print(r"\aaa\'")




