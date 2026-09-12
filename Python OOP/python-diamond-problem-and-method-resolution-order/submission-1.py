class A:
    def print_method(self) -> None:
        print("A")

class B(A):
    def print_method(self) -> None:
        print("B")

class C(A):
    def print_method(self) -> None:
        print("C")

class D(B, C): 
    #since it first finds the print method in B, 
    pass


# Do not change the code below
d = D()
d.print_method()
