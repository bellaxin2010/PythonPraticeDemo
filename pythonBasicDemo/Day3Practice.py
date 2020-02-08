# -*- encoding :utf-8 -*-

# 有列表 li = [‘alex’, ‘egon’, ‘smith’, ‘pizza’, ‘alen’], 请将以字母“a”开头的元素的首字母改为大写字母；
li = ['alex', 'egon', 'smith', 'pizza', 'alen']

for key,value in enumerate(li):
    #print(value)
    if value.startswith('a') :
        newValue = value.title()
        print(newValue)


# 递归二分法
a = [1,3,4,6,7,8,9,11,15,17,19,21,22,25,29,33,38,69,107]
def binary_search(start,end,n,d_list):
    """
    每次把列表规模折半，查找一个数据最多只需2的n次方 < len(d_list) ,   是2的多少次方
    假如列表长度为200 ， 最多查询 8次， （2**8）
    :param start :查找的起点
    :param end : 查找的结束
    :param n : 查找的数字
    :param d_list : 查找列表

    """

    if start < end:
        mid = (start + end) //2 # 一半
        # 判断 左边， 再右边， 中间
        if d_list[mid] > n :
            print("在左边", start, mid, end, "-----", d_list[start], d_list[end- 1])
            binary_search(start,mid,n,d_list)
        elif d_list[mid]< n:
            print("在右边", start, mid, end, "-----", d_list[start], d_list[end- 1])
            binary_search(mid+1,end,n,d_list)
        else:
            print("找到了",d_list[mid],mid)
    else:
        print("%s不在" % n)

binary_search(0,len(a),33,a)