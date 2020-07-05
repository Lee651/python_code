name = ['Ai xiangfei','Wei sixiong','Li zhanglong','Li zhangwei','xxx']
#name.insert(2,"Shu Yawen")列表任意位置加元素
#name.append("Shu Yawen")列表末尾加元素
#del name[2]删除任意位置的元素（永久性删除）
#name_1 = name.pop()删除列表最后一个元素，且可以继续调用该元素。若在括号内加上索引，就可以删除任意位置的元素
#name_2 = name.remove("Wei sixiong")可以删除列表中任何一个不知道索引的元素，并且可以再次引用这个删除的元素，但在删除前需要将该元素赋值给一个变量，再调用该元素即可
message = "my best friend is" + " " + name[2] + "!"
print(message + "\n" + name_1)
