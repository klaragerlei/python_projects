class A(object):
    def func(self,x):
        print("executing simple function   (%s,%s)"%(self,x))

    @classmethod
    def class_func(cls,x):
        print("executing class function   (%s,%s)"%(cls,x))

    @staticmethod
    def static_func(x):
        print("executing static function   (%s)"%x)    

a=A()

a.func(1)
print()

a.class_func(1)
A.class_func('he')
print()

a.static_func(1)
A.static_func('he')
print()