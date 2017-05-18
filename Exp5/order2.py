import tkinter
import tkinter.messagebox
import tkinter.ttk

root = tkinter.Tk()
root.title('菜单')
root['height']=400
root['width']=550
labelName=tkinter.Label(root,text=' 顾客姓名：',justify=tkinter.RIGHT,width=50)
labelName.place(x=10,y=5,width=50,height=20)
varName=tkinter.StringVar(value='')
entryName=tkinter.Entry(root,width=120,textvariable=varName)
entryName.place(x=70,y=5,width=120,height=20)
labelGrade=tkinter.Label(root,text="用餐人数",justify=tkinter.RIGHT,width=50)
labelGrade.place(x=10,y=40,width=50,height=20)
studentClasses={'1':['鱼香肉丝','宫保鸡丁','水煮肉片','溜肥肠','米饭','面条','包子','毛血旺','酸辣土豆丝','凉拌藕片'],
                '2':['鱼香肉丝','宫保鸡丁','水煮肉片','溜肥肠','米饭','面条','包子','毛血旺','酸辣土豆丝','凉拌藕片'],
                '3':['鱼香肉丝','宫保鸡丁','水煮肉片','溜肥肠','米饭','面条','包子','毛血旺','酸辣土豆丝','凉拌藕片']}
comboGrade=tkinter.ttk.Combobox(root,values=tuple(studentClasses.keys()),width=50)
comboGrade.place(x=70,y=40,width=50,height=20)
def comboChange(event):
    grade=comboGrade.get()
    if grade:
        comboClass["values"]=studentClasses.get(grade)
    else:
        comboClass.set([])
comboGrade.bind('<<ComboboxSelected>>',comboChange)
labelClass=tkinter.Label(root,text="点菜明细",justify=tkinter.RIGHT,width=50)
labelClass.place(x=130,y=40,width=50,height=20)
comboClass=tkinter.ttk.Combobox(root,width=50)
comboClass.place(x=190,y=40,width=50,height=20)
labelSex=tkinter.Label(root,text="菜品辣度：",justify=tkinter.RIGHT,width=50)
labelSex.place(x=10,y=70,width=50,height=20)

sex=tkinter.IntVar(value=1)
radioMan=tkinter.Radiobutton(root,variable=sex,value=1,text="正常")
radioMan.place(x=70,y=70,width=50,height=20)
radioWoman=tkinter.Radiobutton(root,variable=sex,value=0,text="不辣")
radioWoman.place(x=130,y=70,width=70,height=20)

smoker=tkinter.IntVar(value=0)
checkSmoker=tkinter.Checkbutton(root,text="是否吸烟？",variable=smoker,onvalue=1,offvalue=0)
checkSmoker.place(x=20,y=100,width=100,height=20)

def addInformation():
    result='姓名: '+entryName.get()
    result=result+';用餐人数：'+comboGrade.get()+' '
    result=result+';点菜明细：'+comboClass.get()+' '
    result=result+';菜品辣度：'+('正常' if sex.get() else '不辣')+' '
    result=result+';是否吸烟：'+('是' if smoker.get() else '否')
    listboxStudents.insert(0,result)
buttonAdd=tkinter.Button(root,text="增加",width=40,command=addInformation)
buttonAdd.place(x=130,y=100,width=40,height=20)

def deleteSelection():
    selection=listboxStudents.curselection()
    if not selection:
        tkinter.messagebox.showinfo(title='Information',massage='No Selection')
    else:
        listboxStudents.delete(selection)

buttonDelete=tkinter.Button(root,text="删除",width=100,command=deleteSelection)
buttonDelete.place(x=180,y=100,width=100,height=20)
listboxStudents=tkinter.Listbox(root,width=300)
listboxStudents.place(x=10,y=130,width=500,height=200)

root.mainloop()

   