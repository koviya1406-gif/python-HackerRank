from collections import OrderedDict
item_dict = OrderedDict()
n = int(input())
for _ in range(n):
    data = input().rsplit(' ', 1)
    item_name = data[0]
    price = int(data[1])
    if item_name in item_dict:
        item_dict[item_name] += price
    else:
        item_dict[item_name] = price
for item, net_price in item_dict.items():
    print(f"{item} {net_price}")
