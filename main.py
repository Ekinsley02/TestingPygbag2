import subprocess
import pygame
import asyncio
import sys

# Initialize pygame
pygame.init()

# Set up the display window
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Display C Output with Pygbag")

# Set font for rendering text
font = pygame.font.Font(None, 48)
text_color = (255, 255, 255)  # White

"""
async def fetch_output():
    try:
        # Run the C program asynchronously and capture the output
        result = await asyncio.create_subprocess_exec(
            "./main",
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        stdout, _ = await result.communicate()
        output_text = stdout.decode().strip()
        return output_text
    except Exception as e:
        print(f"Error running C program: {e}")
        return "Error running C program."
"""
        

async def main():
    # Fetch the output of the C program
    # output_text = await fetch_output()
    output_text = "Hello world12!"
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Clear the screen
        screen.fill((0, 0, 0))  # Black background

        # Render the output text
        text_surface = font.render(output_text, True, text_color)
        text_rect = text_surface.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
        screen.blit(text_surface, text_rect)

        # Update the display
        pygame.display.flip()
        
        # Control frame rate
        await asyncio.sleep(0.016)  # Roughly 60 FPS

# Run the main async loop
asyncio.run(main())

# Quit pygame
pygame.quit()
sys.exit()
