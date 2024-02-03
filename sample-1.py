import tkinter as tk
from tkinter import messagebox
import pygame
from pygame.locals import *

# Function to start the workout and open the OpenGL window
def start_workout():
    # Additional setup for the workout can be added here
    # For simplicity, let's just open a basic Pygame OpenGL window

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

# Create the main window
root = tk.Tk()
root.title("Welcome to KIWI")

# Create and configure GUI components
title_label = tk.Label(root, text="Welcome to KIWI", font=("Helvetica", 16))
title_label.pack(pady=20)

start_button = tk.Button(root, text="Push button to start workout", command=start_workout)
start_button.pack()

# Run the Tkinter event loop
root.mainloop()
