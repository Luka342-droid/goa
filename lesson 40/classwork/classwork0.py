#1
def greet():
    return "hello world"

# 2
def count_sheeps(sheep):
    return sheep.count(True)

# 3
def no_space(x):
    return x.replace(" ", "")

# 4
def double_integer(i):
    return i*2

#5
def greet(name):
    return f"Hello, {name} how are you doing today?"

# 6
def boolean_to_string(b):
    return str(b)

# 7
def basic_op(operator, value1, value2):
    if operator == "+":
        return value1 + value2
    elif operator == "-":
        return value1 - value2
    elif operator == "":
        return value1 / value2
    else:
        return value1 / value2
    
# 8
def litres(time):
    return time // 2

# 9
def digitize(n):
    starting_str = str(n)
    reversed_str = starting_str[::-1]
    res_list = []

    for i in reversed_str:
        res_list.append(int(i))
    return res_list

# 10
def maps(a):
    saver=[]
    for i in a:
        saver.append(i*2)
    return saver

#11
def lovefunc( flower1, flower2 ):
    if flower1 % 2 == 0 and flower2 % 2 == 1:
        return True
    elif flower1 % 2 == 1 and flower2 % 2 == 0:
        return True
    else:
        return False
    
#12
def sum_array(a):
    return sum(a)