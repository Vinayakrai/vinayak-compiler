from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename
from tkinter import messagebox
import subprocess

compiler=Tk()   # Construct a GUI app
compiler.title('Vinayak Compiler')
filepath=''
filetypes1 = [('Python Files', '*.py'), ('Java Files', '*.java')]

def run():
    if filepath == '':
        messagebox.askretrycancel('Save File', 'Please save your file',
                                        icon='warning')
        return
    command=f'java {filepath}'  # Change python to java for java compiler
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    code_output.insert('1.0', output)
    code_output.insert('1.0', error)

def save_as():
    if filepath=='':
        global filetypes1
        path=asksaveasfilename(filetypes=filetypes1)
    else:
        path=filepath
    with open(path, 'w') as file:
        code=editor.get('1.0', END)
        file.write(code)
        save_file(path)

def save_file(path):
    global filepath
    filepath=path

def new_file(event=None):
    global filepath
    filepath=''
    MsgBox = messagebox.askquestion('New File Permission', 'Are you sure you want to create new file?', icon='warning')
    if MsgBox == 'yes':
        editor.delete(1.0, END)
    else:
        editor.delete(1.0, 1.0)

def open_file():
    global filetypes1
    path=askopenfilename(filetypes=filetypes1)
    with open(path, 'r') as file:
        code=file.read()
        editor.delete('1.0', END)
        editor.insert('1.0', code)
        save_file(path)

menu_bar=Menu(compiler)   # On top of compiler

# FILE
file_menu=Menu(menu_bar, tearoff=False)   # On top of menu bar
file_menu.add_command(label='New', command=new_file)
file_menu.add_command(label='Open', command=open_file)
file_menu.add_command(label='Save', command=save_as)
file_menu.add_command(label='Save As', command=save_as)
file_menu.add_command(label='Exit', command=run)
menu_bar.add_cascade(label='File', menu=file_menu)

# RUN
run_bar=Menu(menu_bar, tearoff=False)   # On top of menu bar
run_bar.add_command(label='Run', command=run)
menu_bar.add_cascade(label='Run', menu=run_bar)

compiler.config(menu=menu_bar)

editor=Text()      # Main area where we write code
editor.pack()

code_output=Text(height=10)
code_output.pack()

compiler.mainloop()