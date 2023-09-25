import tkinter as tk
from PIL import Image, ImageDraw, ImageTk, ImageColor

# Create a function to draw a color wheel
def draw_color_wheel():
    # Create a new image with a white background
    size = 300
    color_wheel = Image.new("RGB", (size, size), "white")
    draw = ImageDraw.Draw(color_wheel)

    # Define the colors for the color wheel
    num_colors = 128
    colors = []
    for i in range(num_colors):
        hue = 360 * i // num_colors
        color = ImageColor.getrgb(f"hsv({hue}, 100%, 100%)")
        colors.append(color)

    # Calculate the size and position of each color segment
    angle = 360 / num_colors
    start_angle = 0
    for color in colors:
        end_angle = start_angle + angle
        draw.pieslice([10, 10, size - 10, size - 10], start_angle, end_angle, fill=color)
        start_angle = end_angle

    # Create a transparent circle in the center to make it look like a wheel
    draw.ellipse([size // 4, size // 4, size * 3 // 4, size * 3 // 4], outline="black")

    # Convert the PIL image to a Tkinter PhotoImage
    color_wheel_tk = ImageTk.PhotoImage(color_wheel)

    # Update the label image with the color wheel
    label.config(image=color_wheel_tk)
    label.image = color_wheel_tk

# Create a Tkinter window
window = tk.Tk()
window.title("Color Wheel")

# Create a label to display the color wheel image
label = tk.Label(window)
label.pack()

# Create a button to draw the color wheel
button = tk.Button(window, text="Draw Color Wheel", command=draw_color_wheel)
button.pack()

# Start the Tkinter main loop
window.mainloop()
