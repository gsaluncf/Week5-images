from PIL import Image, ImageTk
import tkinter as tk

root = tk.Tk() # Create the root (base) window where all widgets go
canvas = tk.Canvas(root) # Create a canvas to draw on
canvas.pack(padx=10, pady=10) # Pack the canvas into the root window
image_obj = Image.open("Peppers.jpg") # Load the image

# lets look at a pixel using a specific x and y coordinate
x = 100
y = 100
print(f"At {x}, {y}, pixel values are {image_obj.getpixel((x, y))}")


tk_image = ImageTk.PhotoImage(image_obj) # Create a Tkinter-compatible image object
canvas.create_image(0, 0, anchor=tk.NW, image=tk_image) # Put the image on the canvas
canvas.config(scrollregion=canvas.bbox(tk.ALL), width=image_obj.width, height=image_obj.height) # Set the canvas size to the image size
root.bind("<Button-1>", lambda event: root.quit()) # Allow user to exit the GUI when clicking on it
root.mainloop()
