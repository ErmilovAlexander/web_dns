import re
import config_parse as CONF

PATH_TO_DBDNS = CONF.DEFAULT.get("path_to_dbdns")

def add_dns(name,address):
    # print (name)
    with open(PATH_TO_DBDNS, 'a') as f:
    # f = open('/home/alexander/PycharmProjects/web_dns/test', 'a')
        string="\n{}		A	{}".format(name,address)
    # print (string)
        f.write(string)
    # f.close()

def del_dns(name,address):
    f = open(PATH_TO_DBDNS, 'r')
    a = f.readlines()
    f.close()
    c=open(PATH_TO_DBDNS, 'a')
    for i in a:
        regular = re.search('([a-zA-Z-\d]+)\t\t(A)\t(\d*.\d*.\d*.\d*)',i)
        if regular is not None:
            name_exec = i[regular.start(1):regular.end(1)]
            type = i[regular.start(2):regular.end(2)]
            adress_exec = i[regular.start(3):regular.end(3)]
            if name_exec == name and adress_exec == address:
                print (name_exec)
                pass
            else:
                c.write(i)
        else:
            c.write(i)
    c.close()


def find():
    list_name = []
    with open(PATH_TO_DBDNS, 'r') as f:
    # f = open('/home/alexander/PycharmProjects/web_dns/test', 'r')
    # a=f.readlines()
    # f.close()
    # list_name = []
        for i in f.readlines():
            regular = re.search('([a-zA-Z-\d]+)\t\t(A)\t(\d*.\d*.\d*.\d*)',i)
            if regular is not None:
                name = i[regular.start(1):regular.end(1)]
                type = i[regular.start(2):regular.end(2)]
                adress = i[regular.start(3):regular.end(3)]
                list_name.append([name,type,adress])
    return list_name
# print (list_name)
# del_dns("test","2344532")

# print (find())