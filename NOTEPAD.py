from tkinter import *
from tkinter.messagebox import *
root=Tk()
root.geometry("600x450")
root.title("hb.notepad")
m=Menu(root)
def t():
    pass


filemenu=Menu(m,tearoff=0)
filemenu.add_command(label="New",command=t)
filemenu.add_command(label="Open",command=t)
filemenu.add_command(label="Save",command=t)
filemenu.add_command(label="Save as",command=t)
filemenu.add_command(label="Exit",command=t)

m.add_cascade(label="File",menu=filemenu)

editmenu=Menu(m)
editmenu.add_command(label="Cut",command=t)
editmenu.add_command(label="Copy",command=t)
editmenu.add_command(label="Paste",command=t)
editmenu.add_command(label="Delete",command=t)
editmenu.add_command(label="Time",command=t)
m.add_cascade(menu=editmenu,label="Edt")

helpmenu=Menu(m,tearoff=0)
helpmenu.add_command(label="Need Help",command=t)
helpmenu.add_command(label="About Us",command=t)
m.add_cascade(menu=helpmenu,label="Help")


formatmenu=Menu(m,tearoff=0)
formatmenu.add_command(label="Font Size",command=t)
formatmenu.add_command(label="Font Style",command=t)
m.add_cascade(menu=formatmenu,label="Format")


#text area
TextArea=Text(root,font="lucida 13 ")
file=None
TextArea.pack(expand=True,fil=BOTH)

#scrollbar
Scroll=Scrollbar(TextArea)
Scroll.pack(side=RIGHT,fill=Y)
Scroll.config(command=TextArea.yview)
TextArea.config(yscrollcommand=Scroll.set)


root.config(menu=m)
root.mainloop()