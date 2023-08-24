import requests
import tkinter as tk
from tkinter import simpledialog,messagebox
import webbrowser
import json

def get_user_input():
    # Create a new GUI window
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Prompt the user for input using simpledialog
    var1 = simpledialog.askstring("Input", "Enter Zone:")
    var2 = simpledialog.askstring("Input", "Enter Building:")
    var3 = simpledialog.askstring("Input", "Enter Street:")

    # Close the GUI window
    root.destroy()

    return var1, var2, var3

# Get user input
zone, bldg, st = get_user_input()

# Print the input values
print("zone 1:", zone)
print("bldg 2:", bldg)
print("street 3:", st)


weburl=f'https://services.gisqatar.org.qa/server/rest/services/Vector/QARS_wgs84/MapServer/0/query?where=zone_no={zone}+and+street_no={st}+and+building_no={bldg}&f=json'

response = requests.post(weburl)

data = response.json()

features = data.get('features', [])

if not features:
    # No features, show error message
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror("Invalid Address", "Invalid address entered.")
    root.destroy()
else:
    # Extract coordinates if features are present
    x_coord = features[0]['geometry']['x']
    y_coord = features[0]['geometry']['y']
    print("X Coordinate:", x_coord)
    print("Y Coordinate:", y_coord)


webbrowser.open_new(f'https://www.google.com/maps/search/?api=1&query={y_coord},{x_coord}')
