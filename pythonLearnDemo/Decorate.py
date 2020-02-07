# -*- encoding:utf-8 -*-

account = {
    "is_auth": False,
    "userName": 'abc',
    "password": '123'
}


# login
def login(func):
    def inner(*args, **kwargs):
        if account["is_auth"] is False:
            userName = input("input username: ")
            passWord = input("input password: ")
            if userName == account["userName"] and passWord == account["password"]:
                account["is_auth"] = True
                print("login successfully")
            else:
                print("Login fail, password or username is wrong")

        if account["is_auth"] is True:
            func(*args, **kwargs)  # 认证成功就执行传入进的函数

    return inner


def home():
    print("首页")


@login
def login_firstPage(n):
    print("login in Fisrt page", n)


@login
def login_secPage():
    print("login in Second page")


# login_firstPage= login(login_firstPage)  ---> @login装饰器， 不改变源代码原调用
# print(login_firstPage)
#
login_firstPage("2")
login_secPage()
#
