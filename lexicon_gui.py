import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import config_handler
import gui_handler
import gui_handler_2



class LexGUI:



    def __init__(self, win):
    	self.master = win
    	



    def createTabs(self):
        s = ttk.Style()
        s.theme_create( "MyStyle", parent="alt", settings={
        "TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0] } },
        "TNotebook.Tab": {"configure": {"padding": [40, 10],
                                        "font" : ('URW Gothic L', '11', 'bold')},}})
        s.theme_use("MyStyle")
        s.configure('TButton', relief='raised', padding= 6)
        

        self.tabControl = ttk.Notebook(self.master)
        
        self.tab1 = ttk.Frame(self.tabControl)
        self.tab2 = ttk.Frame(self.tabControl)
        self.tab3 = ttk.Frame(self.tabControl)
        #self.tab4 = ttk.Frame(self.tabControl)

        self.tabControl.add(self.tab1, text = 'Process Google')
        self.tabControl.add(self.tab2, text = 'Mass Process')      
        self.tabControl.add(self.tab3, text = 'Settings')
        #self.tabControl.add(self.tab4, text = 'Upload')


        #display tabs
        self.tabControl.pack(expand = 1, fill = "both")

    def fileDialog(self):
        self.filename = filedialog.askopenfilename(initialdir = "E:/FULLTEXT/GOOGLE", 
            title = "Select a clean map", filetypes = (("JSON files", "*.json"), ("all files", "*.*")))
        if (self.filename):
            self.filepath.set(self.filename) #set the textbox to the file path
            #self.button2.config(state = "normal")
            cf = config_handler.ConfigHandler()
            cf.set_config_value(cf.RECENT_OPEN_FILE,self.filename)

    def dirDialog(self):
        self.filename2 = filedialog.askdirectory()
        if (self.filename2):
            self.filepath2.set(self.filename2) #set the textbox to the file path        
            cf = config_handler.ConfigHandler()
            cf.set_config_value(cf.RECENT_OUTPUT_DIR,self.filename2)
    
    def processText(self):
        if(self.filepath.get(), self.filepath2.get()):
            gui_handler.prepareMongoWrite(self.filepath.get(), self.filepath2.get())
        else:
            messagebox.showwarning("Error", "Missing input file")
   
    def createTab1(self):
        #frame

        self.labelFrame = ttk.LabelFrame(self.tab1, text= 'Select a clean map file:')
        self.labelFrame.grid(column=0, row=0, padx = 20, pady = 20)

        #textbox
        self.filepath = tk.StringVar()
        #load defaults
        cf = config_handler.ConfigHandler()
        value = cf.get_config_value(cf.RECENT_OPEN_FILE)
        self.filepath.set(value)
        s = ttk.Style()
        s.configure('TEntry', font = ('Courier', 24), padding = 4)


        self.path = ttk.Entry(self.labelFrame, width=90, textvariable = self.filepath)
        self.path.grid(column = 0, row = 1, sticky = "w")

        #button 1
        self.button1 = ttk.Button(self.labelFrame, text = "Browse A File", command=self.fileDialog)
        self.button1.grid(column = 1, row = 1, sticky = "w")

        #label 2
        self.label2 = ttk.Label(self.labelFrame, text="Click button to start writing to MongoDB:")
        self.label2.grid(column = 0, row = 2, sticky = "w")
        
        #button no 5
        self.button5 = ttk.Button(self.labelFrame, text = "START PROCESS", command=self.processText)
        self.button5.grid(column = 0, row = 5)

    def dirDialog2(self):
        self.filename3 = filedialog.askdirectory()
        if (self.filename3):
            self.filepath3.set(self.filename3) #set the textbox to the file path        
            cf = config_handler.ConfigHandler()
            cf.set_config_value(cf.RECENT_OUTPUT_DIR2,self.filename3)

    def processText2(self):
        if(self.filepath3.get(), self.filepath2.get()):
            gui_handler_2.processMultiple (self.filepath3.get(), self.filepath2.get())
        else:
            messagebox.showwarning("Error", "Missing input or output folder")

  
    def createTab2(self):
        self.labelFrame2 = ttk.LabelFrame(self.tab2, text= 'Select input directory:')
        self.labelFrame2.grid(column=0, row=0, padx = 20, pady = 20)
        
        self.filepath3 = tk.StringVar()
        #load config value
        cf = config_handler.ConfigHandler()
        value = cf.get_config_value(cf.RECENT_OUTPUT_DIR2)
        self.filepath3.set(value) 
        self.path3 = ttk.Entry(self.labelFrame2, width=90, textvariable = self.filepath3)
        self.path3.grid(column = 0, row = 1, sticky = "w")
        
        #button 4
        self.button4 = ttk.Button(self.labelFrame2, text = "Browse Directory", command=self.dirDialog2)
        self.button4.grid(column = 1, row = 1, sticky = "w")
  
        #label 3
        self.label3 = ttk.Label(self.labelFrame2, text="Click button to start mass processing:")
        self.label3.grid(column = 0, row = 2, sticky = "w")
        
        #button no 6
        self.button6 = ttk.Button(self.labelFrame2, text = "START PROCESS", command=self.processText2)
        self.button6.grid(column = 0, row = 3)


    def createTab3(self):

        self.labelFrame3 = ttk.LabelFrame(self.tab3, text= 'Select output directory:')
        self.labelFrame3.grid(column=0, row=0, padx = 20, pady = 20)

        self.filepath2 = tk.StringVar()
        #load config value
        cf = config_handler.ConfigHandler()
        value = cf.get_config_value(cf.RECENT_OUTPUT_DIR)
        self.filepath2.set(value) 
        self.path2 = ttk.Entry(self.labelFrame3, width=90, textvariable = self.filepath2)
        self.path2.grid(column = 0, row = 3, sticky = "w")
        

        #button 3
        self.button3 = ttk.Button(self.labelFrame3, text = "Browse Directory", command=self.dirDialog)
        self.button3.grid(column = 1, row = 3, sticky = "w")
  



    def createGUI(self):
        self.createTabs()    
        self.createTab1()
        self.createTab2()
        self.createTab3()
   