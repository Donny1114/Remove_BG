from rembg import remove
from PIL import Image
input_path = "1.jpg"
output_path = "2.png"
inp = Image.open(input_path)
output = remove(inp)
output.save(output_path)
