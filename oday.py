import tkinter as tk
from tkinter import messagebox
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from datetime import datetime
import cv2
import pyrealsense2 as rs
import numpy as np

# Initialize Pygame
pygame.init()

# Initialize the RealSense pipeline
pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)

# Function to open the depth camera
def open_depth_camera():
    pipeline.start(config)

    def cvimage_to_pygame(image):
        """Convert cvimage into a pygame image"""
        return pygame.image.frombuffer(image.tobytes(), image.shape[1::-1], "RGB")

    while True:
        frames = pipeline.wait_for_frames()
        color_frame = frames.get_color_frame()

        if not color_frame:
            continue

        frame = np.asanyarray(color_frame.get_data())
        image = cvimage_to_pygame(frame)

        screen.blit(image, (0, 0))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                cv2.destroyAllWindows()
                pipeline.stop()
                exit()

# Function to start the workout and open the OpenGL window
def start_workout():
    open_depth_camera()  # Call the function to open the depth camera

    pygame.init()
    screen = pygame.display.set_mode((800, 600), DOUBLEBUF | OPENGL)
    gluPerspective(45, (800 / 600), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glBegin(GL_TRIANGLES)
        glVertex3fv((0, 1, -5))
        glVertex3fv((-1, -1, -5))
        glVertex3fv((1, -1, -5))
        glEnd()

        pygame.display.flip()
        pygame.time.wait(10)

# Function to update the date and time label
def update_datetime_label():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_date = now.strftime("%Y-%m-%d")
    datetime_label.config(text=f"Date: {current_date}\nTime: {current_time}")
    root.after(1000, update_datetime_label)

# Create the main window
root = tk.Tk()
root.title("Welcome to KIWI")

# Create and configure GUI components
title_label = tk.Label(root, text="Welcome to KIWI", font=("Helvetica", 16))
title_label.pack(pady=20)

start_button = tk.Button(root, text="Push button to start workout", command=start_workout)
start_button.pack()

datetime_label = tk.Label(root, text="")
datetime_label.pack()

# Initial update of date and time
update_datetime_label()

# Run the Tkinter event loop
root.mainloop()
