

class employee:

    def hello(self,name=None):

        if name is not None:

            print('hello',name)

        else:

            print('hello')

s1=employee()

a=input('enter name: ')

s1.hello(a)
