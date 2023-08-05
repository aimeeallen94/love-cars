my_list = [1,2,3,4,4,4,5,5,2]
my_new_list = my_list.drop_duplicates(subset=None, keep='first', inplace=False)
print(my_new_list)