from Tkinter import *
import Tkinter, tkFont, tkFileDialog
import pandas as pd


class ClusterApplication(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        master.title("K Means Clustering")
        self.grid()
        self.l_data_file_path = None
        self.l_num_clusters = None
        self.l_num_runs = None
        self.e_data_file_path = None
        self.e_num_clusters = None
        self.e_num_runs = None
        self.b_cluster = None
        self.b_pre_process = None
        self.b_browse = None
        self.data_file = None
        self.init_widgets()

    def init_widgets(self):
        # text labels
        self.l_data_file_path = Label(self, text="Data set Path: ")
        self.l_data_file_path.grid(row=0, column=0, sticky=W)

        self.l_num_clusters = Label(self, text="Num of clusters k: ")
        self.l_num_clusters.grid(row=1, column=0, sticky=W)

        self.l_num_runs = Label(self, text="Num of runs: ")
        self.l_num_runs.grid(row=2, column=0, sticky=W)

        # user input entries
        self.e_data_file_path = Entry(self, width=100)
        self.e_data_file_path.grid(row=0, column=1)

        self.e_num_clusters = Entry(self, width=10)
        self.e_num_clusters.grid(row=1, column=1, sticky=W)

        self.e_num_runs = Entry(self, width=10)
        self.e_num_runs.grid(row=2, column=1, sticky=W)
        # buttons
        self.b_browse = Button(self, text="Browse", command=self.open_browser)
        self.b_browse.grid(row=0, column=5)

        self.b_pre_process = Button(self, text="Pre-Process", bg="lime green")
        # self.b_pre_process = tkFont.Font(weight='bold')
        self.b_pre_process.grid(row=8, column=0, padx=10, pady=10, sticky=W)

        self.b_cluster = Button(self, text="Cluster", command=self.set_num_clusters, bg="medium turquoise")
        self.b_cluster.grid(row=8, column=1, padx=10, pady=10, sticky=W)

    def open_browser(self):
        self.data_file = tkFileDialog.askopenfilename(initialdir="/", title="Select file",
                                                      filetypes=(("xlsx files", "*.xlsx"), ("all files", "*.*")))
        if self.data_file:
            try:
                # save_file = tkFileDialog.asksaveasfilename(filetypes=(("xlsx files", "*.xlsx"), ("all files", "*.*")))
                self.data_frame = pd.read_excel(self.data_file)
                #
                print(self.data_frame.describe())
                #
                self.e_data_file_path.delete(0, END)
                self.e_data_file_path.insert(0, self.data_file)
                # data.to_excel(save_file + ".xlsx", index=False, sheet_name="Results")
                # self.message = "Complete"
                # self.label_text.set(self.message)
            except:
                print "Error. Please try again."
                # self.message = "Error. Please try again."
                # self.label_text.set(self.message)
                # showerror("Open Source File", "Failed to import file\n'%s'" % file)

    def set_num_clusters(self):
        usr_in = int(self.e_num_clusters.get())
        print(usr_in)

    def set_num_runs(self):
        usr_in = int(self.e_num_runs.get())
        print(usr_in)

    @staticmethod
    def get_dataframe():
        return data_frame

