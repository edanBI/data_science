from Tkinter import *
import tkFileDialog, tkMessageBox
import pandas as pd
from dataPreProcess import PreProcess


class ClusterApplication(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        master.title("K Means Clustering")
        self.grid()
        self.data_frame = None
        self._usr_input = -1
        # text labels
        self.l_data_file_path = Label(self, text="Data set Path: ")
        self.l_data_file_path.grid(row=0, column=0, sticky=W)

        self.l_num_clusters = Label(self, text="Num of clusters k: ")
        self.l_num_clusters.grid(row=1, column=0, sticky=W)

        self.l_num_runs = Label(self, text="Num of runs: ")
        self.l_num_runs.grid(row=2, column=0, sticky=W)

        # user input entries
        preprocess_vcmd = master.register(self.validate_path)
        self.e_data_file_path = Entry(self, width=100, validate="key", validatecommand=(preprocess_vcmd, '%P'))
        self.e_data_file_path.grid(row=0, column=1)

        var_vcmd = master.register(self.validate)
        self.e_num_clusters = Entry(self, width=10, validate="key", validatecommand=(var_vcmd, '%P'))
        self.e_num_clusters.grid(row=1, column=1, sticky=W)

        self.e_num_runs = Entry(self, width=10, validate="key", validatecommand=(var_vcmd, '%P'))
        self.e_num_runs.grid(row=2, column=1, sticky=W)
        # buttons
        self.b_browse = Button(self, text="Browse", command=self.open_browser)
        self.b_browse.grid(row=0, column=5)

        self.b_pre_process = Button(self, text="Pre-Process", command=self.pre_process, bg="lime green")
        self.b_pre_process.grid(row=8, column=0, padx=10, pady=10, sticky=W)

        self.b_cluster = Button(self, text="Cluster", command=self.set_num_clusters, bg="medium turquoise")
        self.b_cluster.grid(row=8, column=1, padx=10, pady=10, sticky=W)

    def open_browser(self):
        self.data_file = tkFileDialog.askopenfilename(initialdir="/", title="Select file",
                                                      filetypes=(("xlsx files", "*.xlsx"), ("all files", "*.*")))
        if self.data_file:
            try:
                self.data_frame = pd.read_excel(self.data_file)
                self.e_data_file_path.delete(0, END)
                self.e_data_file_path.insert(0, self.data_file)
            except Exception:
                print "Error reading data file, Please try again."

    def validate(self, _in):
        if not _in:
            self._usr_input = 0
            return True
        try:
            self._usr_input = int(_in)
            return True
        except ValueError:
            tkMessageBox.showinfo("Error", "Please enter numeric value")
            # print "Wrong Input!   Try again..."
            return False

    def validate_path(self, _in):
        if not _in:
            return True
        try:
            self.data_file = _in
            return True
        except Exception:
            tkMessageBox.showerror("Error", "enter data file path")
            return False

    def set_num_clusters(self):
        if not self.e_num_clusters.get():
            tkMessageBox.showerror("Error", "Enter number of cluster ")
            return

        usr_in = int(self.e_num_clusters.get())
        print(usr_in)
        self.e_num_clusters.delete(0, END)

    def set_num_runs(self):
        if not self.e_num_runs.get():
            tkMessageBox.showerror("Error", "enter number of runs")
            return
        else:
            usr_in = int(self.e_num_runs.get())
        self.e_num_runs.delete(0, END)
        print(usr_in)

    def pre_process(self):
        if self.data_frame is None:
            tkMessageBox.showerror("Error", "enter data file path.")
            return
        processed = PreProcess(self.data_frame)
        tkMessageBox.showinfo("Pre-Processing", "Preprocessing completed successfully!")



