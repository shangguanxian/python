x = [1,2,3,4,5]
x.append([6])
print(x)
#append每次只能新增添一个元素，如果要增添多个元素要使用extend
a = [1,2,3]
a.extend([4,5,6])
print(a)
#inset可以在中间添加元素
c = [1,2,3,7,8,9]
c.insert(4,'4,5,6')
print(c)