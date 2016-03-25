# encoding:utf-8
import json
from IPy import IP
from os import getcwd
class QueryIP(object):
    def __init__(self):
        print getcwd()
        try:
            f=open(getcwd()+u"/data.json".encode("gbk"))
        except Exception,e:
            print Exception,":","Not found data.json"
        self.data=json.loads(f.read())
        f.close()
    def CheckIP(self,ip):
        try:
            IP(ip)
            return True
        except:
            return False
    def Query(self,ip):
        for d in self.data.keys():
            print "打开板块：",d
            for o in self.data[d].keys():
                print "正在检查:",o
                for r in range(len(self.data[d][o]["data"])):
                    start_ip=self.data[d][o]["data"][r][0]
                    end_ip=self.data[d][o]["data"][r][1]
                    if IP(start_ip)<=IP(ip)<=IP(end_ip):
                        IP_Info={u"板块":d,u"单位":o}
                        IP_Info.update(dict(zip(self.data[d][o]["row_names"],self.data[d][o]["data"][r])))
                        return IP_Info
        return False

go=QueryIP()
ip="1.1.1.1"
if go.CheckIP(ip):
    result=go.Query(ip)
    if result:
        print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
        for i in result.keys():
            print i ,":",result[i]
    else:
        print "没有查询到此IP。"
else:
    print "不是合法的IP地址。"




