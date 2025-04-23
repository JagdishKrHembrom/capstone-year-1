import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Nutritional database with images (corrected image paths)
menu_items = {
    "Breakfast": [
        {"name": "Avocado Toast", "calories": 250, "image": r"D:\StudentProjects\Year1\capstone\images\avocado_toast.jpg", "health_info": "Healthy fats & fiber"},
        {"name": "Greek Yogurt Bowl", "calories": 180, "image": r"D:\StudentProjects\Year1\capstone\images\dhokla.jpg", "health_info": "High protein, probiotics"},
        {"name": "Oatmeal", "calories": 150, "image": r"D:\StudentProjects\Year1\capstone\images\\idli.jpg", "health_info": "Complex carbohydrates"},
    ],
    "Lunch": [
        {"name": "Grilled Chicken Salad", "calories": 320, "image": r"D:\StudentProjects\Year1\capstone\images\chicken_salad.jpg", "health_info": "Lean protein & veggies"},
        {"name": "Quinoa Bowl", "calories": 400, "image": r"D:\StudentProjects\Year1\capstone\images\mixveg.jpg", "health_info": "Complete protein & fiber"},
        {"name": "Veggie Wrap", "calories": 280, "image": r"D:\StudentProjects\Year1\capstone\images\paratha.jpg", "health_info": "Low-carb option"},
    ],
    "Dinner": [
        {"name": "Salmon & Veggies", "calories": 450, "image": r"D:\StudentProjects\Year1\capstone\images\quinoa_bowl.jpg", "health_info": "Omega-3 fatty acids"},
        {"name": "Turkey Meatballs", "calories": 380, "image": r"D:\StudentProjects\Year1\capstone\images\salmon.jpg", "health_info": "Low-fat protein"},
        {"name": "Stir-Fry Tofu", "calories": 300, "image": r"D:\StudentProjects\Year1\capstone\images\oatmeal.jpg", "health_info": "Vegetarian protein"},
    ]
}

class SmartMenuApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart Menu Advisor")
        self.total_calories = 0
        self.daily_goal = 2000  # Default calorie goal
        self.current_meal = ""
        self.current_items = []
        self.current_index = 0
        self.initialize_app()

    def initialize_app(self):
        self.set_calorie_goal()
    
    def set_calorie_goal(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        
        tk.Label(self.root, text="Set Your Daily Calorie Goal", font=("Arial", 16)).pack(pady=20)
        
        self.goal_entry = tk.Entry(self.root)
        self.goal_entry.pack(pady=10)
        self.goal_entry.insert(0, str(self.daily_goal))
        
        tk.Button(self.root, text="Confirm", command=self.save_goal).pack(pady=10)
    
    def save_goal(self):
        try:
            self.daily_goal = int(self.goal_entry.get())
            self.show_main_menu()
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number")

    def show_main_menu(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Select Meal Type", font=("Arial", 16)).pack(pady=20)
        
        for meal_type in menu_items.keys():
            tk.Button(self.root, text=meal_type, width=20,
                      command=lambda mt=meal_type: self.start_meal_selection(mt)).pack(pady=10)
            
        tk.Button(self.root, text="View Progress", command=self.show_progress).pack(pady=20)
    
    def start_meal_selection(self, meal_type):
        self.current_meal = meal_type
        self.current_items = menu_items[meal_type]
        self.current_index = 0
        self.show_menu_item()
    
    def show_menu_item(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        if self.current_index >= len(self.current_items):
            messagebox.showinfo("Selection Complete", "Meal selection finished!")
            self.show_main_menu()
            return

        item = self.current_items[self.current_index]
        
        # Display food image
        self.display_image(item["image"])
        
        # Display nutritional information
        info_text = f"{item['name']}\nCalories: {item['calories']}\n{item['health_info']}"
        tk.Label(self.root, text=info_text, font=("Arial", 12)).pack(pady=10)
        
        # Action buttons
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=20)
        
        tk.Button(btn_frame, text="Select This", 
                 command=lambda: self.add_to_meal(item)).pack(side=tk.LEFT, padx=10)
        tk.Button(btn_frame, text="Next Option", 
                 command=self.next_item).pack(side=tk.LEFT, padx=10)
        tk.Button(btn_frame, text="Back to Menu", 
                 command=self.show_main_menu).pack(side=tk.LEFT, padx=10)
    
    def display_image(self, image_path):
        try:
            image = Image.open(image_path)
            image = image.resize((300, 200), Image.Resampling.LANCZOS)  # Updated resampling method
            photo = ImageTk.PhotoImage(image)
            label = tk.Label(self.root, image=photo)
            label.image = photo  # Keep a reference to avoid garbage collection
            label.pack(pady=10)
        except Exception as e:
            print("Error loading image:", e)
            # Optionally display an error message in the GUI
            tk.Label(self.root, text="Image not found", fg="red").pack(pady=10)
    
    def add_to_meal(self, item):
        self.total_calories += item["calories"]
        messagebox.showinfo("Added", f"{item['name']} added to your daily intake!")
        self.next_item()
    
    def next_item(self):
        self.current_index += 1
        self.show_menu_item()
    
    def show_progress(self):
        progress = min(self.total_calories / self.daily_goal * 100, 100)
        remaining = max(self.daily_goal - self.total_calories, 0)
        
        report = (
            f"Daily Calorie Goal: {self.daily_goal}kcal\n"
            f"Consumed: {self.total_calories}kcal\n"
            f"Remaining: {remaining}kcal\n"
            f"Progress: {progress:.1f}%"
        )
        
        messagebox.showinfo("Daily Progress", report)

if __name__ == "__main__":
    root = tk.Tk()
    app = SmartMenuApp(root)
    root.mainloop()