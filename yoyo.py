import cv2
import pygame
import pyrealsense2 as rs
import numpy as np

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((640, 480))

# Initialize the RealSense pipeline and device
pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)

try:
    # Start the RealSense pipeline
    pipeline.start(config)

    # Wait for a few frames to allow auto-exposure to stabilize
    for i in range(30):
        pipeline.wait_for_frames()

    # Define the cvimage_to_pygame function
    def cvimage_to_pygame(image):
        """Convert cvimage into a pygame image"""
        return pygame.image.frombuffer(image.tobytes(), image.shape[1::-1], "RGB")

    while True:
        # Wait for a coherent pair of frames: depth and color
        frames = pipeline.wait_for_frames()
        color_frame = frames.get_color_frame()

        if not color_frame:
            continue

        # Convert the RealSense color frame to a NumPy array
        frame = np.asanyarray(color_frame.get_data())

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
