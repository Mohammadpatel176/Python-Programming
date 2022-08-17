class A:
    def call(self):
        print("A:Call")




class B(A):
    def call(self):
        super().call()
        print("B:Call")


class C(A):
    def call(self):
        super().call()
        print("C:Call")



class D(B,C):
    def call(self):
        super().call()
        print("D:Call")




d1=D()
d1.call()

