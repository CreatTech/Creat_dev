class A:

    def __init__(self):
        print("in init A")

    def feature1(self):
        print("feature 1 working")

    def feature2(self):
        print("feature 2 working")

class B:     #class B inheriting class A


    def __init__(self):
       # super().__init__()    # to call init of A also
        print("in init B")

    def feature3(self):
        print("feature 3 working")

    def feature4(self):
        print("feature 4 working")

class C(A,B):

    def __init__(self):
        super().__init__()  #calling _init of A ...why becuase of MRO  ...left to right
        print("in init C")

# = A()

#a1.feature1()
#a1.feature2()

a1 = B()
