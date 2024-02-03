import cv2
import pygame
import pyrealsense2 as rs
import numpy as np

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((1280, 480))

# Initialize the RealSense pipeline and device
pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)  # Left camera
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)  # Right camera
profile = pipeline.start(config)

# Get the depth sensor from the profile
depth_sensor = profile.get_device().first_depth_sensor()
depth_sensor.set_option(rs.option.visual_preset, rs.visual_preset("Default"))

# Define the cvimage_to_pygame function
def cvimage_to_pygame(image):
    """Convert cvimage into a pygame image"""
    return pygame.image.frombuffer(image.tobytes(), image.shape[1::-1], "RGB")

try:
    # Wait for a few frames to allow auto-exposure to stabilize
    for i in range(30):
        pipeline.wait_for_frames()

    while True:
        # Wait for a coherent pair of frames: depth and left/right color
        frames = pipeline.wait_for_frames()
        left_frame = frames.get_color_frame(0)
        right_frame = frames.get_color_frame(1)

        if not left_frame or not right_frame:
            continue

        # Convert the RealSense color frames to NumPy arrays
        left_image = np.asanyarray(left_frame.get_data())
        right_image = np.asanyarray(right_frame.get_data())

        # Concatenate the left and right images horizontally
        frame = np.concatenate((left_image, right_image), axis=1)

        # Convert the frame to a Pygame image
        image = cvimage_to_pygame(frame)

        # Display the image in the Pygame window
        screen.blit(image, (0, 0))
        pygame.display.flip()

        # Check for quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                cv2.destroyAllWindows()
                pipeline.stop()
                exit()

except Exception as e:
    print(f"Error: {e}")

finally:
    # Stop the RealSense pipeline when done
    pipeline.stop()
