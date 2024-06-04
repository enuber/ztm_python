# functional programming

# separation of concerns. each part is packaged together over one thing. we separate data and functions. Instead of combining attributes and methods, we keep them separated.

# Clear + understandable
# easy to extend
# easy to maintain
# memory efficient
# DRY - don't repeat yourself.

# pure functions - separation of data of a program and behaviour of a program
# it is a simple function but when we use that function we always get back the same output given the same input. it should not produce any side effects. ie should not effect anything outside of the function.

# is this a pure function? given the same input it will always give us back the same output. So that is one part of what is needed. Then does it produce side effects? It doesn't touch anything outside of the function itself.

# if we did return print(new_list) it would be using the print() function which is considered a side effect as we don't know what print() will always be. It interacts with the screen.
# if new_list was defined outside the function it would also produce a side effect.

def multiply_by2(li):
    new_list = []
    for num in li:
        new_list.append(num*2)
    return new_list


print(multiply_by2([1, 2, 3]))  # [2,4,6]

# pure functions is a guideline and not an absolute. We want to strive for that when it is possible.
