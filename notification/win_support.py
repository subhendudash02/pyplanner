# import win10toast
from win10toast import ToastNotifier
import sys

# create an object to ToastNotifier class
notify = ToastNotifier()

if len(sys.argv) == 2:
    notify.show_toast("Reminder", sys.argv[1])
else:
    print("Bad params passed")
    exit()
