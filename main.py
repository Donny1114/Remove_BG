import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from PIL import Image, ImageTk
from rembg import remove
import os


class BackgroundRemoverApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Background Remover App")
        self.root.geometry("500x300")

        # Labels and buttons
        self.label = tk.Label(root, text="Background Remover", font=("Helvetica", 16))
        self.label.pack(pady=10)

        self.upload_button = tk.Button(root, text="Select Image", command=self.select_image)
        self.upload_button.pack(pady=5)

        self.image_label = tk.Label(root, text="No image selected.")
        self.image_label.pack(pady=5)

        self.progress = ttk.Progressbar(root, orient=tk.HORIZONTAL, length=400, mode='determinate')
        self.progress.pack(pady=10)

        self.process_button = tk.Button(root, text="Remove Background", command=self.remove_background,
                                        state=tk.DISABLED)
        self.process_button.pack(pady=5)

        self.save_button = tk.Button(root, text="Save Output", command=self.save_output, state=tk.DISABLED)
        self.save_button.pack(pady=5)

        # Reset button
        self.reset_button = tk.Button(root, text="Reset", command=self.reset_app)
        self.reset_button.pack(pady=5)

        # Variables
        self.input_path = None
        self.output_image = None

    def select_image(self):
        self.input_path = filedialog.askopenfilename(title="Select Image",
                                                     filetypes=(("Image Files", "*.jpg *.jpeg *.png"), ("All Files", "*.*")))
        if self.input_path:
            self.image_label.config(text=f"Selected: {os.path.basename(self.input_path)}")
            self.process_button.config(state=tk.NORMAL)
        else:
            self.image_label.config(text="No image selected.")
            self.process_button.config(state=tk.DISABLED)

    def remove_background(self):
        if not self.input_path:
            messagebox.showerror("Error", "Please select an image first.")
            return

        self.progress['value'] = 0
        self.root.update_idletasks()

        try:
            # Load the image
            inp = Image.open(self.input_path)

            # Simulating a progress bar by updating in steps
            for i in range(1, 101, 25):  # Progress in 4 steps
                self.progress['value'] = i
                self.root.update_idletasks()

            # Remove background
            output = remove(inp)

            # Simulate completing the task
            self.progress['value'] = 100
            self.root.update_idletasks()

            # Store output image in memory
            self.output_image = output

            # Enable save button
            self.save_button.config(state=tk.NORMAL)
            messagebox.showinfo("Success", "Background removal complete! Click Save Output button to save the file.")

        except Exception as e:
            messagebox.showerror("Error", f"Failed to remove background: {e}")

    def save_output(self):
        if not self.output_image:
            messagebox.showerror("Error", "No output to save. Process the image first.")
            return

        output_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                   filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
        if output_path:
            try:
                self.output_image.save(output_path)
                messagebox.showinfo("Success", f"Image saved successfully as {os.path.basename(output_path)}")
                self.reset_app()  # Automatically reset the app after saving

            except Exception as e:
                messagebox.showerror("Error", f"Failed to save image: {e}")

    def reset_app(self):
        """Reset the application to its initial state."""
        self.input_path = None
        self.output_image = None
        self.image_label.config(text="No image selected.")
        self.progress['value'] = 0
        self.process_button.config(state=tk.DISABLED)
        self.save_button.config(state=tk.DISABLED)


# Main loop
if __name__ == "__main__":
    root = tk.Tk()
    app = BackgroundRemoverApp(root)
    root.mainloop()
