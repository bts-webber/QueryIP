#coding=utf-8
from os import listdir
from os import getcwd
import xlrd
import json
from IPy import IP
class InputIP(object):
    def __init__(self):
        self.subdir=[]
        self.file_name={}
        self.data={}
    def GetFileName(self,dir):
        self.subdir=listdir(dir)
        for d in self.subdir:
            self.file_name[d]=listdir(dir+"/"+d)
        for s in range(len(self.subdir)):
            self.subdir[s]=self.subdir[s].decode("gbk")
    def GetIpTable(self,dir):
        for d in self.subdir:
            self.data[d]={}
            for f in self.file_name[d.encode("gbk")]:
                path=dir+"/"+d.encode("gbk")+"/"+f
                print path.decode("gbk")
                table=xlrd.open_workbook(path).sheet_by_name(u"IP地址分配表")
                table_nrows=table.nrows
                organization_name=table.row_values(0)[1]
                self.data[d][organization_name]={}
                self.data[d][organization_name][table.row_values(0)[2]]=table.row_values(0)[3]
                self.data[d][organization_name][table.row_values(0)[4]]=table.row_values(0)[5]
                self.data[d][organization_name]["row_names"]=table.row_values(2)
                self.data[d][organization_name]["data"]=[]
                for n in range(table_nrows)[3:]:
                    row_value=table.row_values(n)
                    try:
                        if IP(row_value[0])>IP(row_value[1]):
                            print "IP地址格式不正确:",d," ",organization_name,":",n+3,"行",row_value[0],",",row_value[1]
                        self.data[d][organization_name]["data"].append(row_value)
                    except Exception,e:
                        print e,"IP地址格式不正确:",d," ",organization_name,":",n+3,"行",row_value[0],",",row_value[1]
                print path.decode("gbk")+" Finised!!"
        return self.data
go=InputIP()
go.GetFileName(u'E:/文档/IP地址/'.encode("gbk"))
data=go.GetIpTable(u'E:/文档/IP地址/'.encode("gbk"))
f=open(getcwd()+"/"+"data.json",'w')
data=json.dumps(data,encoding='utf-8')
f.write(data)
f.close()







