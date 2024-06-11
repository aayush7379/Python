from PIL import Image, ImageDraw

# Define the size of the image
width, height = 200, 200

# Create a new image with white background
image = Image.new('RGB', (width, height), 'white')

# Initialize the drawing context
draw = ImageDraw.Draw(image)

# Define the points of the triangle
triangle_points = [(100, 20), (20, 180), (180, 180)]

# Draw the triangle
draw.polygon(triangle_points, outline='black', fill='blue')

# Save the image to a file
image.save('triangle_image.png')

# Display the image
image.show()
