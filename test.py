#!/usr/bin/env python

# derived (a lot) from: https://www.youtube.com/watch?v=Bn1n1diGv_0

import tkinter
import pandas as pd
from tkinter import ttk
import numpy

root = tkinter.Tk()
root.title('Testing')
root.geometry('700x1000')

my_frame = tkinter.Frame(root)
my_frame.pack(pady=20,fill = tkinter.BOTH, expand = True)

my_scrollbar = tkinter.Scrollbar(my_frame)
my_scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)

df = pd.read_csv('./db.csv')

my_tree = tkinter.ttk.Treeview(my_frame, yscrollcommand=my_scrollbar.set)
my_tree.delete(*my_tree.get_children())

my_scrollbar.config(command=my_tree.yview)

my_tree['column'] = list(df.columns)
my_tree['show'] = 'headings'
for column in my_tree['column']:
    my_tree.heading(column, text=column)

# put data in treeview
df_rows = df.to_numpy().tolist()
for row in df_rows:
    my_tree.insert('', 'end', values=row)

my_tree.pack(fill = tkinter.BOTH, expand = True)


root.mainloop()
