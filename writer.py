i = 0
sum_data = 0
while i <= 100:
    sum_data += i
    i += 1
print(sum_data)

# 单字符获取内容
str_data = 'ksdjfldjsl'  # 定义一个普通的字符串
# 标准演示
# 输出 jfl 的内容, 第7个位置的索引是6
print(str_data[3:6:1])
# 输出：kdfd 的内容
print(str_data[0:7:2])
