# y = f(x) = kx + b
# 定义函数  def 函数名([形参]):
# 调用函数  函数名([实参])
# 参数  0,1,2,或多个
# 有参有返

def f(x:str,) -> int:
    return 1 * x + 0 


# 有参无返
def s(x):
    print(f'您传递的参数是："{x}"')


# 无参无返
def pri():
    print('hello')

# 无参有返
def pins():
    return 80

# print(pins())

def add(x=0,y=0,z=38):
    """
    
    
    """
    for i  in range(y):
        print(i)
    # return x +y +z


def greet(say, *names, **name_say) -> None:
    print('say：', say)
    print('names：', names)
    print('name_say：', name_say)
    for name in names:
        print(name, say)
    for key in name_say.keys():
        print(key, name_say[key])


def fib(n):
    global x
    x = 1
    # print(j)
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)



if __name__ == '__main__':
    # j = 0
    a = f(5)
    print(f(5.1))
    # 递归代码
    # n = int(input('请输入一个正整数：'))
    # print('斐波那契数列的第{}项为：{}'.format(n, fib(n)))
    print([i for i in range(100) if i % 4 != 0])
    print({i : i*3 for i in range(100) if i % 4 != 0})
    s = 0 
    print(s.bit_count())
    # print(x)
    # pass

    # s("你好")
    # pri()

    # print(add(3,5,6))
    # print(add(x=4,z=6,y=8))
    # print(add(y=10))

    # greet('hi！', '小蓝', '小舞', 小红='你好！', 小明='hello！')