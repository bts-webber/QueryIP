#coding=utf-8
from Tkinter import *
from QueryIP import QueryIP
def query_ip():
    ip=var.get()
    Go=QueryIP()
    if Go.CheckIP(ip):
        text.delete(0.0,END)
        text.insert(END,"正在查询，请稍定片刻......")
        result=Go.Query(ip)
        if result:
            text.delete(0.0,END)
            for i in result.keys():
                text.insert(END,i+":"+result[i]+"\n")
        else:
            text.delete(0.0,END)
            text.insert(END,"没有查询到此IP。")
    else:
        text.delete(0.0,END)
        text.insert(END,"IP地址格式不正确")
if __name__=="__main__":
    frmMain=Tk()
    frmMain.title("内网IP地址查询工具 By:Webber")
    frmMain.geometry("400x500")
    frmMain.resizable(width=True,height=True)
    var=StringVar()
    entry=Entry(frmMain,textvariable=var,font=("Arial",15))
    entry.pack(side=TOP)
    text=Text(frmMain,width=40,height=20,font=("Arial",13))
    text.pack(side=BOTTOM)
    Button(frmMain,text="查询",command=query_ip,font=("Arial",15)).pack(side=TOP)
    frmMain.mainloop()




