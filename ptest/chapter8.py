# -*- coding: UTF-8 -*-

# 测试entry的使用

from tkinter import *
from tkinter import messagebox

fup = Frame()
# fup.pack()

username = StringVar()
password = StringVar()


# 校验函数
def check_name(what):
    print("check name")
    if len(what) > 8:
        Tip.config(text="用户名不可以超过8个字符", fg="red")
    else:
        Tip.config(text="")


def check_pwd(what):
    print("check password")
    if len(what) > 8:
        Tip.config(text="密码不可以超过8个字符", fg="red")
    else:
        Tip.config(text="")


# 用户名和密码框
la_username = Label(fup, text='用户名：', width=8, anchor=E)
in_username = Entry(fup, textvariable=username, width=20)
la_password = Label(fup, text='密码：', width=8, anchor=E)
in_password = Entry(fup, textvariable=password, show="*")

docheck1 = in_username.register(check_name)  # 注册校验函数
in_username.config(validate="focusout", validatecommand=(docheck1, '%P'))  # 校验
docheck2 = in_username.register(check_pwd)
in_password.config(validate="focusout", validatecommand=(docheck2, '%P'))

fup.pack()
la_username.grid(row=1, column=1)
in_username.grid(row=1, column=2)
la_password.grid(row=2, column=1)
in_password.grid(row=2, column=2)

label1 = Label(fup, text="当前用户信息：")
label1.grid(row=3, column=1)


def reset():
    username.set("")
    password.set("")
    Tip.config(text="")
    print("reset")


def done():
    global info
    name = in_username.get()
    pwd = in_password.get()
    if (name == "" or pwd == ""):
        messagebox.showwarning("错误提示", "请完善信息")
        return
    if (name in info) == True:
        messagebox.showwarning("错误提示", "用户名已存在")
        return
    str = "您的用户名为：" + name + "，密码为：" + pwd
    Tip.config(text=str, fg="black")

    info = info + "用户名：" + name + "，密码：" + pwd + "\n"
    listvar.set(info)
    messagebox.showinfo("确认信息", "添加成功")
    username.set("")
    password.set("")
    print("done")


# listbox
list_inf = ""
list_frame = Frame()
list_frame.pack()
listvar = StringVar()
info = "\n"
listvar.set(info)
list = Listbox(list_frame, listvariable=listvar, selectmode=MULTIPLE, height=10)
# list.grid(row=0,expand=1,fill=Y)
list.grid(row=0, column=0)

'''跨行删除存在问题：中间项在info中存在，但是listvar中不见了，怎么回事呢
   目前措施：删除后重新给listvar刷新一下'''


def deleteitem():
    global info
    print("deleteitem")
    index = list.curselection()
    print("index=" + str(index))
    if len(index) > 0:
        tobe_delete = ""
        '''先对info操作，删除应该想去除的内容，再在listvar中删除选中项'''
        for i in range(0, len(index)):
            print(i)
            tobe_delete = str(list.get(index[i]))
            print("tobe-delete=" + tobe_delete)
            temp = info.partition(tobe_delete)
            print('temp=' + "".join(temp))
            info = temp[0] + temp[-1]
            print("info=" + info)
            temp = ""
        if len(index) > 1:
            list.delete(index[0], index[-1])
        else:
            list.delete(index[0])
    listvar.set(info)


def showitem():
    print("showitem")
    index = list.curselection()
    if len(index) == 0: return
    tobe_show = ""
    if len(index) > 1:
        tobe_show = str(list.get(index[0], index[-1]))
    elif len(index) == 1:
        tobe_show = str(list.get(index[0]))
    label2.config(text=tobe_show)


def queryitem():
    print("queryitem")


def outitem():
    print("outitem")


bn_delete = Button(list_frame, text="删除", command=deleteitem)
bn_delete.grid(row=1, column=0)
bn_show = Button(list_frame, text="显示", command=showitem)
bn_show.grid(row=2, column=0)
bn_query = Button(list_frame, text="查询", command=queryitem)
bn_query.grid(row=3, column=0)
bn_output = Button(list_frame, text="导出", command=outitem)

label2 = Label(list_frame, text="Can you see me", justify=LEFT)
label2.grid(row=4, column=0)

# 确认/重置
fup2 = Frame()
fup2.pack()
reset = Button(fup2, text="重置", command=reset)
done = Button(fup2, text="添加", command=done)
reset.grid(row=1, column=1)
done.grid(row=1, column=2)

# 提示
Tip = Label(text="")
Tip.pack()

mainloop()
