a = {
    'wm': '我们',
    'sj': '世界',
}
print(a['wm'])
print(type(a))

a ['woeld'] = '世界'
print(a)

print('------------')

b = {}
print(b,type(b))

b ['woeld'] = '世界'
print(b)

print('------------')

del a ['wm']
print(a)

print('-------------')

a.clear()
print(a)

print('--------------')

q = {
    'we' : '我们',
    'world' : '世界',
    'company' : '公司',
}
q1 = q
q2 = q.copy()
print(q)
print(q1)
print(q2)

print('---------------')

print(q.get('we'))
print(q.get('baidu'))