#Default simple code
# from rembg import remove
# from PIL import Image
# input_path = "1.jpg"
# output_path = "2.png"
# inp = Image.open(input_path)
# output = remove(inp)
# output.save(output_path)

#Added progress bar
from rembg import remove
from PIL import Image
from tqdm import tqdm
import numpy as np

input_path = "1.jpg"
output_path = "2.png"

# Open the input image
inp = Image.open(input_path)

# Create a dummy array to simulate processing
# Need to adjust this according to  image size for a better simulation
dummy_array = np.zeros((inp.size[1], inp.size[0]), dtype=np.uint8)

# Use tqdm to create a progress bar
with tqdm(total=100, desc="Removing background") as pbar:
    # Simulating processing in chunks
    for _ in range(10):  # Adjust the range for the number of chunks
        output = remove(inp)  # Perform background removal
        pbar.update(10)  # Update progress

# Save the output image
output.save(output_path)

# Print completion message
print(f"Background removal complete. Output saved as '{output_path}'.")

