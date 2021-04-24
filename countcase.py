#-*- coding: UTF-8 -*-
from __future__ import division
from xmindparser import xmind_to_dict

class CountXmind():
    def __init__(self,filepath):
        self.total = 0
        self.success = 0
        self.failed = 0
        self.execd = 0

        self.filepath = filepath

    def covert(self):
        self.xmind_dict = xmind_to_dict(self.filepath)#将xmind转换成字典,返回的是一个list
        #print(self.xmind_dict)
        self.xmind_list = self.xmind_dict[0]['topic']['topics']
        #print(self.xmind_list)
        #print len(self.xmind_list)
        # for i in range(len(self.xmind_list)):
        #     return self.xmind_list[i]['title']
        self.count(self.xmind_list)
        return self.total,self.execd,self.success,self.failed,self.modelu

    def count(self,case):
        self.modelu = []
        for i in range(len(case)):
            self.modelu.append(case[i]['title'])
            if case[i].__contains__('topics'):#带topics标签意味挣有子标题，递归执行方法
                self.count(case[i]['topics'])
                #print case[i]['topics']['title']
            else:
                if case[i].__contains__('makers'):
                    self.execd += 1
                    if case[i]['makers'].__contains__('task-done'):
                        self.success += 1
                    elif case[i]['makers'].__contains__('symbol-wrong'):
                        self.failed += 1

                self.total += 1



if __name__ == '__main__':
    r = CountXmind('/Users/jia/Downloads/jiayu.xmind')
    result = r.covert()
    print ('用例总数为 %s' % result[0])
    print ('已执行用例数 %s' % result[1])
    print ('执行成功用例数 %s, 成功率为%1.f%%' % (result[2],(result[2]/result[1]*100)))
    print ('执行失败用例数 %s' % result[3])
    print ('模块 %s' % result[4])