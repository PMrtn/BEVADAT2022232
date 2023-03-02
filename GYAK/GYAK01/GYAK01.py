# %%
#Create a function that decides if a list contains any odd numbers.
#return type: bool
#function name must be: contains_odd
#input parameters: input_list

# %%
def contains_odd(input_list : list) -> bool:
    i = 0
    
    while(i < len(input_list) and input_list[i] % 2 == 0):
        i = i + 1

    if(i < len(input_list)): return True
    
    else: return False

# %%
#Create a function that accepts a list of integers, and returns a list of bool.
#The return list should be a "mask" and indicate whether the list element is odd or not.
#(return should look like this: [True,False,False,.....])
#return type: list
#function name must be: is_odd
#input parameters: input_list

# %%
def is_odd(input_list : list[int]) -> list[bool]:
    masklist = []

    for szam in input_list:
        if szam % 2 == 0: masklist.append(False)
        else: masklist.append(True)

    return masklist

# %%

#Create a function that accpects 2 lists of integers and returns their element wise sum. <br>
#(return should be a list)
#return type: list
#function name must be: element_wise_sum
#input parameters: input_list_1, input_list_2

# %%
def element_wise_sum(input_list_1 : list[int], input_list_2 : list[int]) -> list[int]:
    sumlist = []
    i = 0

    for szam in input_list_1:
        sumlist.append(szam + input_list_2[i])
        i = i + 1
    
    return sumlist

# %%
#Create a function that accepts a dictionary and returns its items as a list of tuples
#(return should look like this: [(key,value),(key,value),....])
#return type: list
#function name must be: dict_to_list
#input parameters: input_dict

# %%
def dict_to_list(input_dict : dict) -> list:
    tuplelist = []

    for key, value in input_dict.items():
        tuplelist.append((key, value))

    return tuplelist

# %%
#If all the functions are created convert this notebook into a .py file and push to your repo


