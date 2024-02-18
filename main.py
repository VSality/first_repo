import math

def single_lists(list_data:list):

    list_by_lists = [[]]
    for num in list_data:
        list_by_lists.append([num])
    return list_by_lists

def neighours_lists(list_data:list):

    list_by_lists = []
    iter = 0
    for _ in list_data:
        if(iter + 1 < len(list_data)):
            list_by_lists.append([list_data[iter], list_data[iter + 1]])
        
        iter += 1

    iter = 0
    for _ in list_data:
        if(iter + 2 < len(list_data)):
            list_by_lists.append([list_data[iter], list_data[iter + 1], list_data[iter + 2]])
        
        iter += 1
    return list_by_lists

    

def data_preparation(list_data):
    list_result = []
    print(list_data)

    list_result.extend(single_lists(list_data))
    list_result.extend(neighours_lists(list_data))
    list_result.extend([list_data])

    print(list_result)


    for sublist in list_data:
        pass
       
    


d = [4, 6, 1, 3]
data_preparation(d)