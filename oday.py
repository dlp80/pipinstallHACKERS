import tkinter as tk
import subprocess  # Added to run external commands

# Function to open the Intel RealSense Viewer
def open_realsense_viewer():
    viewer_path = r"C:\Program Files (x86)\Intel RealSense SDK 2.0\tools\realsense-viewer.exe"
    subprocess.run([viewer_path])

# Function to start the workout and open the OpenGL window
def start_workout():
    # You can add your workout code here
    print("Workout started")

# Function to update the date and time label
def update_datetime_label():
    # Update the date and time label code here
    print("Updating date and time label")

# Create the main window
root = tk.Tk()
root.title("Welcome to KIWI")

# Create and configure GUI components
title_label = tk.Label(root, text="Welcome to KIWI", font=("Helvetica", 16))
title_label.pack(pady=20)

# Button to open Intel RealSense Viewer
viewer_button = tk.Button(root, text="Open RealSense Viewer", command=open_realsense_viewer)
viewer_button.pack()

# Button to start the workout
start_button = tk.Button(root, text="Push button to start workout", command=start_workout)
start_button.pack()

# Label to display date and time
datetime_label = tk.Label(root, text="")
datetime_label.pack()

# Initial update of date and time
update_datetime_label()

# Run the Tkinter event loop
root.mainloop()
import tkinter as tk
import subprocess  # Added to run external commands

# Function to open the Intel RealSense Viewer
def open_realsense_viewer():
    viewer_path = r"C:\Program Files (x86)\Intel RealSense SDK 2.0\tools\realsense-viewer.exe"
    subprocess.run([viewer_path])

# Function to start the workout and open the OpenGL window
def start_workout():
    # You can add your workout code here
    print("Workout started")

# Function to update the date and time label
def update_datetime_label():
    # Update the date and time label code here
    print("Updating date and time label")

# Create the main window
root = tk.Tk()
root.title("Welcome to KIWI")

# Create and configure GUI components
title_label = tk.Label(root, text="Welcome to KIWI", font=("Helvetica", 16))
title_label.pack(pady=20)

# Button to open Intel RealSense Viewer
viewer_button = tk.Button(root, text="Open RealSense Viewer", command=open_realsense_viewer)
viewer_button.pack()

# Button to start the workout
start_button = tk.Button(root, text="Push button to start workout", command=start_workout)
start_button.pack()

# Label to display date and time
datetime_label = tk.Label(root, text="")
datetime_label.pack()

# Initial update of date and time
update_datetime_label()

# Run the Tkinter event loop
root.mainloop()
