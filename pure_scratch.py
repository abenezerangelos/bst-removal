#below is a stand alone function call that has declarations within it lambda
print( (lambda f: (lambda x: f(f, x))(5))(lambda d,n:1 if n<=1 else n*d(d,n-1)))
#right side is declaration for functions (I/O)
#left side is standalone function class that can be called upon
factorial=lambda x:recursive_function_call(recursive_function_call,x)
recursive_function_call=lambda f:factorial
recursive_function_declaration_arguement=lambda d,n:1if n<=1 else n*d(d,n-1)
print((recursive_function_call(recursive_function_declaration_arguement))(5))
#function_call is just recursive_function

#example of what a lambda expression looks like normally
# def one(f):# one-declaration, f-argument (i.e., without bracket) one(1)-function call because passing argument(in lambda this is equivalent to (lambda f:f+1)(1)
#     def two(x):
#         pass
#     return
# print((lambda x,y: x+y)(2,3))
# def three(d,n):
#     return 1 if n<=1 else n*d(d,n-1)

# def recursive_function(f, n):#declaration
#     if n <= 1:
#         return 1
#     else:
#         return n * f(f, n - 1)
#
# def factorial(x):#declaration
#     return recursive_function(recursive_function, x)#call (return function call)

# Usage
#this whole statement right here is recursive_function_call
result=factorial(5)#function call(equivalent to (lambda x:f(f,x))(5)

