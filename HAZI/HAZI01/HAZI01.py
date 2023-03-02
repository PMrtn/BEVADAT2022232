# %%
#Create a function that returns with a subsest of a list.
#The subset's starting and ending indexes should be set as input parameters (the list aswell).
#return type: list
#function name must be: subset
#input parameters: input_list,start_index,end_index

# %%
def subset(input_list : list, start_index : int, end_index : int) -> list:
    sublist = []
    i = start_index - 1

    while(i < end_index and i < len(input_list)):
        sublist.append(input_list[i])
        i = i + 1

    return sublist

# %%
#Create a function that returns every nth element of a list.
#return type: list
#function name must be: every_nth
#input parameters: input_list,step_size

# %%
def every_nth(input_list : list, step_size : int) -> list:
    nthlist = []
    i = step_size - 1

    while(i < len(input_list)):
        nthlist.append(input_list[i])
        i = i + step_size
    
    return nthlist

# %%
#Create a function that can decide whether a list contains unique values or not
#return type: bool
#function name must be: unique
#input parameters: input_list

# %%
#Create a function that can flatten a nested list ([[..],[..],..])
#return type: list
#fucntion name must be: flatten
#input parameters: input_list

# %%
def flatten(input_list : list) -> list:
    
    flatlist = [num for sublist in input_list for num in sublist]
    return flatlist

# %%
#Create a function that concatenates n lists
#return type: list
#function name must be: merge_lists
#input parameters: *args


# %%
def merge_lists(*args) -> list:
    mergedlist = []

    for list in args:
        for element in list:
            if mergedlist.__contains__(element) == False: mergedlist.append(element)

    return mergedlist

# %%
#Create a function that can reverse a list of tuples
#example [(1,2),...] => [(2,1),...]
#return type: list
#fucntion name must be: reverse_tuples
#input parameters: input_list

# %%
def reverse_tuples(input_list : list) -> list:

    return [tuple[::-1] for tuple in input_list]

# %%
#Create a function that removes duplicates from a list
#return type: list
#fucntion name must be: remove_tuplicates
#input parameters: input_list

# %%
def remove_tuplicates(input_list : list) -> list:
    uniquelist = []

    [uniquelist.append(x) for x in input_list if x not in uniquelist]
    return uniquelist

# %%
#Create a function that transposes a nested list (matrix)
#return type: list
#function name must be: transpose
#input parameters: input_list

# %%
def transpose(input_list : list) -> list:
    return [list(x) for x in zip(*input_list)]

# %%
#Create a function that can split a nested list into chunks
#chunk size is given by parameter
#return type: list
#function name must be: split_into_chunks
#input parameters: input_list,chunk_size

# %%
def split_into_chunks(input_list : list, chunk_size : int) -> list:
    
    chunklist = [input_list[i:i + chunk_size] for i in range(0, len(input_list), chunk_size)]
    return chunklist

# %%
#Create a function that can merge n dictionaries
#return type: dictionary
#function name must be: merge_dicts
#input parameters: *dict

# %%
def merge_dicts(*dict) -> dict:
    d = {}

    for dictionary in dict:
        d = {**d, **dictionary}

    return d

# %%
#Create a function that receives a list of integers and sort them by parity
#and returns with a dictionary like this: {"even":[...],"odd":[...]}
#return type: dict
#function name must be: by_parity
#input parameters: input_list

# %%
def by_parity(input_list : list) -> dict:
    evenlist = []
    oddlist = []

    for num in input_list:
        if num & 1: oddlist.append(num)
        else: evenlist.append(num)

    return {"even":evenlist,"odd":oddlist}

# %%
#Create a function that receives a dictionary like this: {"some_key":[1,2,3,4],"another_key":[1,2,3,4],....}
#and return a dictionary like this : {"some_key":mean_of_values,"another_key":mean_of_values,....}
#in short calculates the mean of the values key wise
#return type: dict
#function name must be: mean_key_value
#input parameters: input_dict

# %%
def mean_key_value(input_dict : dict) -> dict:
    values = {}

    for key, value in input_dict.items():
        mean = 0

        for x in value:
            mean = mean + x

        values[key] = mean / len(value)

    return values

# %%
#If all the functions are created convert this notebook into a .py file and push to your repo


