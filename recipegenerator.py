import tkinter as tk
from tkinter import messagebox, scrolledtext
import google.generativeai as genai

# Important security note: Avoid hardcoding API keys in production code
# Consider using environment variables or secure configuration
GEMINI_API_KEY = "AIzaSyBlvVrY8W3ebzHuztExcBPuKIUjZKaip6M"

# Initialize the Gemini API
genai.configure(api_key=GEMINI_API_KEY)

def call_gemini_api(prompt, temperature=0.8):
    """Calls the Gemini 2.0 Flash model with a text prompt."""
    try:
        model = genai.GenerativeModel("gemini-2.0-flash")
        response = model.generate_content(prompt)
        return {"response": response.text if response else "No response from API."}
    except Exception as e:
        return {"response": f"Error calling API: {e}"}

def generate_recipe():
    """Generates recipe based on user inputs and displays the response."""
    include_items = include_text.get("1.0", tk.END).strip()
    exclude_items = exclude_text.get("1.0", tk.END).strip()

    if not include_items:
        messagebox.showwarning("Input Error", "Please enter items to include.")
        return

    # Build the recipe prompt
    prompt = f"Create a detailed recipe that includes: {include_items}"
    if exclude_items:
        prompt += f" and excludes: {exclude_items}"
    prompt += ". Include ingredients list and step-by-step instructions."

    # Call API
    result = call_gemini_api(prompt, temperature=0.8)

    # Display response
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, result["response"])

# -----------------------------
# Tkinter GUI Setup
# -----------------------------
root = tk.Tk()
root.title("AI Recipe Generator")
root.geometry("600x500")

# Frame for including food items
include_frame = tk.Frame(root)
include_frame.pack(pady=10, padx=10, fill=tk.X)
include_label = tk.Label(include_frame, text="Ingredients to include:")
include_label.pack(anchor="w")
include_text = tk.Text(include_frame, height=3, width=70)
include_text.pack()

# Frame for excluding food items
exclude_frame = tk.Frame(root)
exclude_frame.pack(pady=14, padx=10, fill=tk.X)
exclude_label = tk.Label(exclude_frame, text="Allergies/exclusions:")
exclude_label.pack(anchor="w")
exclude_text = tk.Text(exclude_frame, height=3, width=70)
exclude_text.pack()

# Generate button
generate_button = tk.Button(root, text="Generate Recipe",
                            command=generate_recipe, bg="green", fg="white",
                            font=("Helvetica", 12, "bold"))
generate_button.pack(pady=10)

# Frame for displaying output
output_frame = tk.Frame(root)
output_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
output_label = tk.Label(output_frame, text="Generated Recipe:")
output_label.pack(anchor="w")
output_text = scrolledtext.ScrolledText(output_frame, height=10, width=70)
output_text.pack(fill=tk.BOTH, expand=True)

# Run the Tkinter event loop
root.mainloop()