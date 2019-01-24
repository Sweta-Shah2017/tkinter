from tkinter import *
from tkinter import scrolledtext, Tk, Menu, filedialog,messagebox
def quitq():
    print("Notepad editor is closed")
    quit()

def resize():
    root.geometry("300x350")
    print("windows is resize")
def full():
    root.geometry("800x600")
def openf( ):
    returns = filedialog.askopenfile(initialdir="/", title=" select files", filetypes=(("text files", ".txt"),("all files", ".*")))
    if returns!=None:
       textArea.delete(1.0, END)
       for line in returns:
         textArea.insert(END,line)
    returns.close()
def savef():
    savefile=filedialog.asksaveasfile(mode="w",defaultextension=".txt")
    if savefile is None:
        return
    sss= textArea.get(1.0,END)
    savefile.write(sss)
    savefile.clase()
def newf():
    textArea.delete(1.0,END)

def copyf():
    textArea.clipboard_clear()
    textArea.clipboard_append(textArea.selection_get())

def cutf():
    copyf()
    textArea.delete("sel.first","sel.last")

def pastef():
    textArea.insert(INSERT,textArea.clipboard_get())


root=Tk(className="Editor")

def ss():
   stas = Label(root, text="started running.....||100%", anchor=E, relief=SUNKEN, bd=1, fg="red", bg="white")
   stas.pack(side=BOTTOM, fill=X)

root.geometry("800x600")

textArea=scrolledtext.ScrolledText(root,width=100, undo=True)
textArea.pack()

menu1=Menu(root)
root.config(menu=menu1)

filem=Menu(menu1, tearoff=False)
menu1.add_cascade(label="File",menu=filem)
filem.add_command(label="New                 Ctrl+N",command=newf)
filem.add_command(label="Open               Ctrl+O",command=openf)
filem.add_command(label="Save           Ctrl+S ",command=savef )
filem.add_command(label="Exit", command=quitq)

editm=Menu(menu1,tearoff=False)
menu1.add_cascade(label="Edit",menu=editm)
editm.add_command(label="Copy                Ctrl+C",command=copyf)
editm.add_command(label="Cut                   Ctrl+X",command=cutf)
editm.add_command(label="Paste                Ctrl+V ", command=pastef)
editm.add_command(label="Undo                Ctrl+Z ")
editm.add_command(label="Select all          Ctrl+A ")
editm.add_command(label="Redo          Ctrl+A ")

formatm=Menu(menu1,tearoff=False)
menu1.add_cascade(label="Format",menu=formatm)
formatm.add_command(label="Word Wrap")
formatm.add_command(label="Font")

viewm=Menu(menu1,tearoff=False)
menu1.add_cascade(label="View",menu=viewm)
viewm.add_command(label="Resize",command=resize)
viewm.add_command(label="Zoom", command=full)
viewm.add_command(label="Status Bar",command=ss)




root.mainloop()