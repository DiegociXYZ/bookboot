def word_count(text):
    count = 0
    split_text = text.split()
    for slice in split_text:
        count+=1
    return count

#################################

def char_count(text):
    char_dict = {}
    lower_text = text.lower()
    for char in lower_text:
        if char not in char_dict:
            char_dict[char]=1
        else:
            char_dict[char] +=1
    return char_dict

#################################

def dict_list(char_dict):
    list_dict =[]
    for key_dict in char_dict:
        char = key_dict
        num = char_dict[key_dict]
        list_dict.append({"char":char,"num":num})
    return list_dict

#######################################

