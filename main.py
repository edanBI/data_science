from GUI import *
# from dataPreProcess import *

root = Tk()  # creates a blank window
root.minsize(width=1000, height=400)
app = ClusterApplication(root)
root.mainloop()  # makes sure the window stays open