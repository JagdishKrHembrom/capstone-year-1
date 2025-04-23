import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

class RestaurantEventApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart Event Manager")
        self.events = []
        self.bookings = []
       
        self.load_sample_data()
       
        self.notebook = ttk.Notebook(root)
        self.customer_frame = ttk.Frame(self.notebook)
        self.management_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.customer_frame, text="Customer View")
        self.notebook.add(self.management_frame, text="Management View")
        self.notebook.pack(expand=1, fill="both")

        self.create_customer_view()
        self.create_management_view()

    def load_sample_data(self):
        self.events = [
            {
                "id": 1,
                "name": "Wine Tasting Night",
                "date": "2024-03-20",
                "type": "Wine Tasting",
                "capacity": 50,
                "booked": 0,
                "menu": ["Cheese Platter", "Red Wine Selection"],
                "price": 75.00
            }
        ]

    def create_customer_view(self):
        self.event_tree = ttk.Treeview(self.customer_frame, columns=("Name", "Date", "Type", "Availability"), show='headings')
        self.event_tree.heading("Name", text="Event Name")
        self.event_tree.heading("Date", text="Date")
        self.event_tree.heading("Type", text="Type")
        self.event_tree.heading("Availability", text="Availability")
        self.event_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
       
        filter_frame = ttk.Frame(self.customer_frame)
        ttk.Label(filter_frame, text="Filter By:").pack()
        self.event_type_var = tk.StringVar()
        self.event_type_combo = ttk.Combobox(filter_frame, textvariable=self.event_type_var, values=["All", "Wine Tasting", "Live Music"])
        self.event_type_combo.pack()
        ttk.Button(filter_frame, text="Apply Filters", command=self.update_event_list).pack()
        filter_frame.pack(side=tk.RIGHT, padx=10)
       
        self.booking_frame = ttk.LabelFrame(self.customer_frame, text="Booking Form")
        ttk.Label(self.booking_frame, text="Name:").grid(row=0, column=0)
        self.name_entry = ttk.Entry(self.booking_frame)
        self.name_entry.grid(row=0, column=1)
       
        ttk.Label(self.booking_frame, text="Event ID:").grid(row=1, column=0)
        self.event_id_entry = ttk.Entry(self.booking_frame)
        self.event_id_entry.grid(row=1, column=1)
       
        ttk.Label(self.booking_frame, text="Number of Attendees:").grid(row=2, column=0)
        self.attendees_entry = ttk.Entry(self.booking_frame)
        self.attendees_entry.grid(row=2, column=1)
       
        ttk.Button(self.booking_frame, text="Book Now", command=self.process_booking).grid(row=4, columnspan=2)
        self.booking_frame.pack(pady=10)
       
        self.update_event_list()
   
    def create_management_view(self):
        creation_frame = ttk.LabelFrame(self.management_frame, text="Create Event")
        ttk.Label(creation_frame, text="Event Name:").grid(row=0, column=0)
        self.event_name_entry = ttk.Entry(creation_frame)
        self.event_name_entry.grid(row=0, column=1)
       
        ttk.Label(creation_frame, text="Date (YYYY-MM-DD):").grid(row=1, column=0)
        self.event_date_entry = ttk.Entry(creation_frame)
        self.event_date_entry.grid(row=1, column=1)
       
        ttk.Label(creation_frame, text="Event Type:").grid(row=2, column=0)
        self.event_type_entry = ttk.Entry(creation_frame)
        self.event_type_entry.grid(row=2, column=1)
       
        ttk.Label(creation_frame, text="Capacity:").grid(row=3, column=0)
        self.event_capacity_entry = ttk.Entry(creation_frame)
        self.event_capacity_entry.grid(row=3, column=1)
       
        ttk.Button(creation_frame, text="Create Event", command=self.create_event).grid(row=5, columnspan=2)
        creation_frame.pack(pady=10)
   
    def update_event_list(self):
        self.event_tree.delete(*self.event_tree.get_children())
        selected_type = self.event_type_var.get()
        for event in self.events:
            if selected_type in ["All", "", event["type"]]:
                self.event_tree.insert("", "end", values=(event["name"], event["date"], event["type"], f"{event['booked']}/{event['capacity']}"))
   
    def process_booking(self):
        if not self.validate_booking():
            return
       
        if self.process_payment():
            self.save_booking()
            messagebox.showinfo("Success", "Booking confirmed!")
   
    def validate_booking(self):
        if not self.name_entry.get() or not self.event_id_entry.get() or not self.attendees_entry.get():
            messagebox.showerror("Error", "All fields are required")
            return False
        return True
   
    def process_payment(self):
        return True
   
    def create_event(self):
        try:
            new_event = {
                "id": len(self.events) + 1,
                "name": self.event_name_entry.get(),
                "date": self.event_date_entry.get(),
                "type": self.event_type_entry.get(),
                "capacity": int(self.event_capacity_entry.get()),
                "booked": 0
            }
            self.events.append(new_event)
            self.update_event_list()
            messagebox.showinfo("Success", "Event created successfully!")
        except ValueError:
            messagebox.showerror("Error", "Invalid data entered")
   
    def save_booking(self):
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = RestaurantEventApp(root)
    root.mainloop()