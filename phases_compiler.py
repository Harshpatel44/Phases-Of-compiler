import tkinter as tk
import os
main=tk.Tk()
main.title("Phases Of Compiler")
var=tk.StringVar()
def preprocess(input_text):
	input_text=input_text.get()
	os.system("cpp "+input_text+" > "+input_text[:-2]+".i")
	print("cpp "+input_text+" > "+input_text[:-2]+".i")
	f=open(input_text[:-2]+".i",'r')
	text_box.delete(1.0,tk.END)
	text_box.insert(tk.END,f.read())
def compiling(input_text):
	input_text=input_text.get()
	os.system("gcc -S "+input_text[:-2]+".i")
	f=open(input_text[:-2]+".s",'r')
	text_box.delete(1.0,tk.END)
	text_box.insert(tk.END,f.read())

def assembly(input_text):
	input_text=input_text.get()
	os.system("as "+input_text[:-2]+".s -o "+input_text[:-2]+".o")
	f=open(input_text[:-2]+".o",'r', errors='ignore')
	text_box.delete(1.0,tk.END)
	text_box.insert(tk.END,f.read())
input_text=tk.Entry(main,width="50")
input_text.focus_set()
input_text.pack()
frame=tk.Frame()
frame.pack()
btn=tk.Button(frame,text="Preprocessing",command=lambda: preprocess(input_text))
btn.pack(side="left")
btn2=tk.Button(frame,text="Compiling",command=lambda:compiling(input_text))
btn2.pack(side="left")
btn3=tk.Button(frame,text="Assembly",command=lambda:assembly(input_text))
btn3.pack(side="left")

text_box=tk.Text(main,height=50)
text_box.pack(side="left")
scroll=tk.Scrollbar(main,command=text_box.yview,orient=tk.VERTICAL)
scroll.pack(side="right")
text_box.config(yscrollcommand=scroll.set)



main.mainloop()
