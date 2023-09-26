string_lst = input().split()
dic = {word : string_lst.count(word) for word in string_lst}
for key, value in dic.items():
    print(key , value)