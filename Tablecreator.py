# mathematics table creator tool
def table_creator():
    table_value = int(input('which table do you want: '))
    num_multi = int(input('upto which you want to multiply: '))
    for i in range(1,num_multi+1):
        print(table_value,'X',i,'=',table_value*i)

table_creator()
