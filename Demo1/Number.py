# -*- coding =utf-8

def multi_number(index):
    for i in range (1,index):
        for j in range (1,i+1):
            print('{}x{}={}\t'.format(i,j,i*j),end='')
        print()


def multi_year(year):

    if(year %4 )==0 & (year %100)==0 &(year %400)==0:
        print('{0}'.format(year) +"it;s runnian")
    else:
        print('{0}'.format(year)+ "not runnian")


if __name__ == '__main__':
    multi_number(10)
    year = int(input("input year: \n"))
    multi_year(year)