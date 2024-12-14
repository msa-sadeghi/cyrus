import turtle  

def draw_branch(branch_length):  
    if branch_length > 5:  
        turtle.forward(branch_length)  
        turtle.right(20)  
        draw_branch(branch_length - 15)  
        turtle.left(40)  
        draw_branch(branch_length - 15)  
        turtle.right(20)  
        turtle.backward(branch_length)  

turtle.speed("fastest")  
turtle.left(90)  
turtle.up()  
turtle.backward(100)  
turtle.down()  
turtle.forward(100)  
draw_branch(75)  
turtle.done()


# def my_func(number):
#     if number == 1:
#         return 1
#     return number * my_func(number-1)
    
# print(my_func(14))