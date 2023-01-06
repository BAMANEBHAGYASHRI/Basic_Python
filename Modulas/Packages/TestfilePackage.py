import TestFile
TestFile.demo3()
from TestFile import *
print(demo1(2,8))
from TestFile import demo2
print(TestFile.demo2(25,9))
print(TestFile.demo1(89,45))