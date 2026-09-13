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
    #since it first finds the print method in B, that's the output that itll print
    #since B is the first method to have the print method 
    pass


# Do not change the code below
d = D()
d.print_method()
