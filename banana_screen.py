import tkinter as tk
from tkinter import ttk
from banana_graph import Banana_graph_maker
class Banana_application(tk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
      
        
        

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x800")
    root.title("Banana Quality")
    app = Banana_application(root)
    root.mainloop()