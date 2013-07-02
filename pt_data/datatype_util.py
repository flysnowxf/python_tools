#encoding: utf-8
'''
Created on 2013-7-1

@author: fengxuefeng
'''

# 判断是否为空
def is_null(string):
    if(not string or string == "" or string == "null"):
        return True
    return False

# 从map中获取值，不存在返回空字符串
def get_value(kv_map, key):
    if not kv_map.has_key(key):
        return ''
    else:
        return kv_map[key]

# 对每行的日志封装map数据
def package_data_map(row):
    data_map = {}
    
    for pair in row.strip().split("<|>"):
        array = pair.split("=")
        if len(array) == 2:
            if is_null(array[1]):
                continue
            data_map[array[0]] = array[1]
        elif len(array) > 2:
            data_map[array[0]] = pair[pair.find("=") + 1:]
    
    return data_map

# 调用一次，算一个值
def count_pv(unique_key, pv_map):
    if not pv_map.has_key(unique_key):
        pv = 1
        pv_map[unique_key] = pv
    else:
        pv = pv_map[unique_key] + 1
        pv_map[unique_key] = pv

# 调用一次，算一个值
def count_uv(unique_key, user, uv_map):
    if not uv_map.has_key(unique_key):
        uv_map[unique_key] = {}
    # 借用pv算法
    count_pv(user, uv_map[unique_key])

# 获取pv
def get_pv(unique_key, pv_map):
    if pv_map.has_key(unique_key):
        return pv_map.get(unique_key)
    else:
        return 0

# 获取uv
def get_uv(unique_key, uv_map):
    # 统计user的个数
    if uv_map.has_key(unique_key):
        return len(uv_map[unique_key].keys())
    else:
        return 0
    
# 根据value排序，并返回排序后的key list
def sorted_by_value(kv_map, reverse, top = None):
    key_list = []
    if len(kv_map) == 0:
        return key_list
    
    map_list = sorted(kv_map.items(), key = lambda d:d[1], reverse = reverse)
    if top == None:
        for item in map_list:
            key, value = item
            key_list.append(key)
    else:
        # 取top n
        i = 1
        for item in map_list:
            if i > top:
                break
            key, value = item
            key_list.append(key)
            i = i + 1
    
    return key_list