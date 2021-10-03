class A:

    def __init__(self):
        print("in init A")

    def feature1(self):
        print("feature 1 working")

    def feature2(self):
        print("feature 2 working")

class B(A):     #class B inheriting class A


    def __init__(self):
        super().__init__()    # to call init of A also
        print("in init B")

    def feature3(self):
        print("feature 3 working")

    def feature4(self):
        print("feature 4 working")



# = A()

#a1.feature1()
#a1.feature2()

a1 = B()  #if no init present in B it will call __init of A , if init is also present in B it will call from B

#what we need to call init from A ....use super

