#在程序运行过程中，所有的变量都在内存中；但是程序结束时，变量所占用的内存就被操作系统全部回收。
#我们把变量从内存中变成可存储或可传输的过程称之为序列化，在python中加pickling。反之，把变量
#内容从序列化的对象重新读取到内存中称之为反序列化，即unpickling

#python提供了pickle模块来实现序列化,pickle模块只能应用于python，与其他语言格式不通用
import pickle
d = dict(name='tonny',age=26,score=1000)
s = pickle.dumps(d) #dumps()函数能够把任意对象序列化成一个bytes，然后可以把bytes写入文件持久化
print(s)

f = open(r'C:\Users\Tonny\Documents\GitHub\PythonDev\test.txt','wb')
pickle.dump(d,f) #直接把序列化后的数据写入一个file-like object
f.close()

with open('test.txt','rb') as f:
    d = pickle.load(f) #unpickling
    f.close()
print(d) 

#json，如果要在不同语言之间传递对象，就必须把对象序列化为标准格式例如xml，但更好的选择是json
#因为json表示出来就是一个字符串，可以被所有语言读取，也可以方便的存储到磁盘或者通过网络传输。json
#不仅是标准，而且比xml更快，而且可以直接在web页面中读取，非常方便。但是在自解析上比xml弱。
#python内置提供了json模块提供了非常完整的python对象到json格式的转换。
import json
s = json.dumps(d) #序列化为json格式,同样可以用dump直接将序列化的对象写入文件
print(s)

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
d = json.loads(json_str) #反序列化json对象，由于json编码是utf-8，所以总是能够正确的在python的str与json字符串之间转换
print(d)

#高级json使用
class Student(object):
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score

def student2dict(std):
    return {
            'name':std.name,
            'age':std.age,
            'score':std.score
        }
def dict2student(d):
    return Student(d['name'],d['age'],d['score'])

s = Student('tonny',26,10000) 

#print(json.dumps(s)) #student不是一个可序列化的对象，TypeError
ss = json.dumps(s,default = student2dict)
print(ss)
print(json.loads(ss,object_hook = dict2student))
