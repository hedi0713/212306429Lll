#=====任务1======
#1.1创建一个包含 5 种动物名字的列表
animals = ["monkey","cat","dog","pig","tiger"]
print("初始列表为：",animals)

#1.2打印该列表中的第 1 和第倒数第3 个动物名字。
print("第1个动物是：",animals[0])
print("倒数第3个动物是：",animals[2])

#1.3在列表末尾添加2个新动物，并打印整个列表
animals.append("rabbit")
animals.insert(len(animals),"elephant")
print("添加2个动物后的新列表为：",animals)

#1.4修改列表中的第 2 个动物名字为另一个名字
animals[1] = "lion"
print("修改后列表中第2个动物的名字为：",animals[1])

#1.5删除列表中的第 4 个动物名字并打印最终列表
del animals[3]
print("删除列表第4个动物名字后的列表为：",animals)

#1.6用pop删除列表第一个元素，并观察列表的变化
first = animals.pop(0)
print("删除的第一个元素是：",first)
print("删除第一个元素后的列表为：",animals)

#1.7分别用sorted和sort对列表进行排序，分析两者的区别
print("当前的列表为：",animals)
#使用sorted
sorted_animals = sorted(animals)
print("使用sorted后返回的副本为：",sorted_animals)
print("使用sorted排序后的列表为：",animals)
#使用sort排序
animals.sort()
print("使用sort排序后列表为：",animals)

#1.8分别使用sorted和sort倒排列表
#使用sorted倒排列表
descending = sorted(animals,reverse=True)
print("使用sorted倒排后的列表为：",descending)
#使用sort倒排列表
animals.sort(reverse=True)
print("使用sort倒排后的列表为：",animals)

#======任务2======
#2.1创建1个数值列表nums，包含1-20之内所有的偶数
nums = []
for num in range(1,21):
    if num % 2 ==0:
        nums.append(num)
print("新建的数值列表为：",nums)

#2.2遍历数值列表，依次计算每个元素的平方（分别用for循环和列表推导式实现）。
#用for循环
for_nums = []
for num in nums:
    for_nums.append(num ** 2)
print("用for循环平方后的数值列表为：",for_nums)

#用列表推导式
square_com = [num ** 2 for num in nums]
print("用列表推导式平方后的列表为：",square_com)

#2.3用列表切片获取数值列表的后5个元素
last_pop5 = nums[len(nums)-5:]
print("最后5个元素是：",last_pop5)

last_neg5 = nums[-5:]
print("最后5个元素是：",last_neg5)

#2.4复现第四章PPT38-40页的代码，观察列表不同拷贝方式的区别
my_foods = ['pizza','cake','coffe']
friend_foods = my_foods
my_foods.append('juice')
friend_foods.append('ice_cream')
print("my_foods的列表为：",my_foods)
print("friend_foods的列表为：",friend_foods)

my_foods = ['pizza','cake','coffe']
friend_foods = my_foods[:]
my_foods.append('juice')
friend_foods.append('ice_cream')
print("my_foods的列表为：",my_foods)
print("friend_foods的列表为：",friend_foods)

#======任务3======
#3.1创建一个字符串“I Love Python I Love Programing”
code = "I Love Python I Love Programing"
print("原始字符串为：",code)

#3.2将字符串分割为单词列表
words = code.split()
print("单词列表为：",words)

#3.3使用join将单词列表组合成句子，但是每个单词间用逗号隔开
words_join = ",".join(words)
print("逗号分隔的句子为：",words_join)

#3.4将字符串分割为字符列表
chars = list(code)
print("字符列表为：",chars)

#3.5将字符列表组合成句子
text = "".join(chars)
print("由字符列表组成的句子为：",text)
