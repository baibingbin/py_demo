import os
import sys

import sayhi

from Study import Study

temp = '中\n文测试'
print(temp.encode())
print(os.name)

with open('C:\\bing\\test.txt', mode='wb') as w:
    w.write(temp.encode())

with open('C:\\441zm903747.txt', mode='r') as r:
    print(r.read())

print(dir(sys))

print(sys.path)

sayhi.sayhi('bai')

TEST = Study('bai','bingbin')
TEST.score = 60
TEST.test = 1

btest = isinstance(TEST, Study)
print(TEST._Study__fullname)

TEST.cal()

TEST = [1, 3, 4]
#TEST.reverse()
TEST.pop()
print(TEST)

abs(-11)
