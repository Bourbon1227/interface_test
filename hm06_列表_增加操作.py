"""
列表实践 - 增加操作
"""

# 1 末尾追加元素
# append
# 作用：在当前列表默认追加一个独立元素
# 语法: list_data.append(元素)
# list_data = []
# list_data.append('a')  # ['a']
# list_data.append('b')  # ['a', 'b']
# list_data.append('c')  # ['a', 'b', 'c']
# print(list_data)
# list_data.append(['a', 'b', 'c']) # ['a', 'b', 'c', ['a', 'b', 'c']]
# print(list_data)


# 2 列表拼接操作
# extend
# 作用：将两个独立的列表 拼接成一个列表
# 语法：list_data.extend(list_data1)
# list_data1 = ['a', 'b', 'c']
# list_data2 = ['abc', True, 0]
# list_data1.extend(list_data2)  # ['a', 'b', 'c', 'abc', True, 0]
# print(list_data1)

# 3 列表插入操作
# insert
# 作用：在指定的位置处，插入一个数据元素
# 语法：list_data.insert("元素内容")
list_data = ['a', 'n', 'v']
list_data.insert(1, "hello world")  # ['a', "hello world", 'n', 'v']
print(list_data)

# 说明：
# 1 在当前列表末尾增加一个元素 append
# 2 在当前列表末尾拼接另外一个列表的所有元素 extend
# 3 在当前列表中，指定位置增加一个元素 insert
