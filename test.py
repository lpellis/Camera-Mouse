'''
Created on Oct 21, 2012

@author: user
'''

class C(object):
    _p = 1

    def __init__(self):
        self.p = 4

#    @property
#    def p(self):
#        return self._p

    @p.setter
    def p(self, val):
        print 'don'
        self._p = val + 3


c = C()
print c.p
c.p = 34
print c.p

class Test(object):
    _p = 12
    def __init__(self):
        self.p0 = 12
        self.p1 = 33
        pass

    @property
    def p(self):
        return self._p
    @p.setter
    def p(self, value):
        self._p = value
        print 'setting'



test = Test()
print test.p
test.p = 33
test.p = 34
print test.p
