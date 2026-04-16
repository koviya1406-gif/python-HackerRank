def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        substring = string[i:i + k]
        u_i = "".join(dict.fromkeys(substring))        
        print(u_i)
