import tkinter as tk
from tkinter import ttk, messagebox

class FoodManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Food Management System")
       
        # Contact information database
        self.donation_contacts = {
            "Orphanages": [
                {"name": "Sunshine Children's Home", "phone": "555-0111"},
                {"name": "Hope Haven Orphanage", "phone": "555-0112"}
            ],
            "Senior Citizens": [
                {"name": "Golden Years Center", "phone": "555-0221"},
                {"name": "Community Eldercare", "phone": "555-0222"}
            ],
            "Manure Manufacturers": [
                {"name": "Green Earth Compost", "phone": "555-0331"},
                {"name": "Eco Manure Co.", "phone": "555-0332"}
            ]
        }
       
        # Raw Food Section
        self.raw_frame = ttk.LabelFrame(root, text="Raw Food Items (Max 10)")
        self.raw_frame.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")
        self.raw_entries = []
        self.add_raw_item_ui()
       
        # Cooked Food Section
        self.cooked_frame = ttk.LabelFrame(root, text="Cooked Food Items (Max 10)")
        self.cooked_frame.grid(row=0, column=1, padx=10, pady=5, sticky="nsew")
        self.cooked_entries = []
        self.add_cooked_item_ui()
       
        # Donation Options
        self.donation_frame = ttk.LabelFrame(root, text="Donation Options")
        self.donation_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky="ew")
       
        self.orphan_var = tk.BooleanVar()
        self.manure_var = tk.BooleanVar()
        ttk.Checkbutton(self.donation_frame, text="Donate to Orphanage", variable=self.orphan_var).pack(side=tk.LEFT, padx=5)
        ttk.Checkbutton(self.donation_frame, text="Donate for Manure Making", variable=self.manure_var).pack(side=tk.LEFT, padx=5)
       
        # New Contact Display Button
        self.contact_btn = ttk.Button(root, text="Show Donation Contacts", command=self.show_contacts)
        self.contact_btn.grid(row=2, column=0, pady=5)
       
        # Report Generation
        self.report_btn = ttk.Button(root, text="Create Report", command=self.generate_report)
        self.report_btn.grid(row=2, column=1, pady=5)
       
        root.grid_columnconfigure(0, weight=1)
        root.grid_columnconfigure(1, weight=1)

    def add_raw_item_ui(self):
        def add_item():
            if len(self.raw_entries) >= 10:
                messagebox.showwarning("Limit Reached", "You can only add up to 10 raw food items.")
                return
            name = name_entry.get().strip()
            qty = qty_entry.get().strip()
            preserved = preserved_var.get()
            if name and qty:
                self.raw_entries.append({
                    "name": name,
                    "qty": qty,
                    "preserved": preserved
                })
                name_entry.delete(0, tk.END)
                qty_entry.delete(0, tk.END)
                preserved_var.set(False)
            else:
                messagebox.showwarning("Input Error", "Please fill in both fields.")

        name_entry = ttk.Entry(self.raw_frame, width=20)
        name_entry.grid(row=0, column=0, padx=5, pady=5)

        qty_entry = ttk.Entry(self.raw_frame, width=10)
        qty_entry.grid(row=0, column=1, padx=5, pady=5)

        preserved_var = tk.BooleanVar()
        preserved_check = ttk.Checkbutton(self.raw_frame, text="Preserved", variable=preserved_var)
        preserved_check.grid(row=0, column=2, padx=5)

        add_button = ttk.Button(self.raw_frame, text="Add Raw Item", command=add_item)
        add_button.grid(row=0, column=3, padx=5, pady=5)

    def add_cooked_item_ui(self):
        def add_item():
            if len(self.cooked_entries) >= 10:
                messagebox.showwarning("Limit Reached", "You can only add up to 10 cooked food items.")
                return
            name = name_entry.get().strip()
            qty = qty_entry.get().strip()
            if name and qty:
                self.cooked_entries.append({
                    "name": name,
                    "qty": qty
                })
                name_entry.delete(0, tk.END)
                qty_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Input Error", "Please fill in both fields.")

        name_entry = ttk.Entry(self.cooked_frame, width=20)
        name_entry.grid(row=0, column=0, padx=5, pady=5)

        qty_entry = ttk.Entry(self.cooked_frame, width=10)
        qty_entry.grid(row=0, column=1, padx=5, pady=5)

        add_button = ttk.Button(self.cooked_frame, text="Add Cooked Item", command=add_item)
        add_button.grid(row=0, column=2, padx=5, pady=5)

    def show_contacts(self):
        contact_window = tk.Toplevel()
        contact_window.title("Donation Contacts")
       
        notebook = ttk.Notebook(contact_window)
       
        # Orphanage Contacts Tab
        orphan_tab = ttk.Frame(notebook)
        for contact in self.donation_contacts["Orphanages"]:
            ttk.Label(orphan_tab,
                     text=f"{contact['name']}\nPhone: {contact['phone']}",
                     padding=5).pack(pady=2)
        notebook.add(orphan_tab, text="Orphanages")
       
        # Senior Citizens Tab
        senior_tab = ttk.Frame(notebook)
        for contact in self.donation_contacts["Senior Citizens"]:
            ttk.Label(senior_tab,
                     text=f"{contact['name']}\nPhone: {contact['phone']}",
                     padding=5).pack(pady=2)
        notebook.add(senior_tab, text="Senior Citizens")
       
        # Manure Manufacturers Tab
        manure_tab = ttk.Frame(notebook)
        for contact in self.donation_contacts["Manure Manufacturers"]:
            ttk.Label(manure_tab,
                     text=f"{contact['name']}\nPhone: {contact['phone']}",
                     padding=5).pack(pady=2)
        notebook.add(manure_tab, text="Manure Services")
       
        notebook.pack(expand=1, fill='both')

    def generate_report(self):
        report = "=== Food Management Report ===\n\n"
       
        report += "Raw Food Items:\n"
        for item in self.raw_entries:
            report += f"- {item['name']} ({item['qty']}) {'[Preserved]' if item['preserved'] else ''}\n"
           
        report += "\nCooked Food Items:\n"
        for item in self.cooked_entries:
            report += f"- {item['name']} ({item['qty']})\n"
           
        report += "\nSelected Donation Options:\n"
        if self.orphan_var.get():
            report += "- Donate to Orphanage\n"
            report += "  Recommended Contacts:\n"
            for contact in self.donation_contacts["Orphanages"]:
                report += f"  {contact['name']}: {contact['phone']}\n"
               
        if self.manure_var.get():
            report += "- Donate for Manure Making\n"
            report += "  Recommended Contacts:\n"
            for contact in self.donation_contacts["Manure Manufacturers"]:
                report += f"  {contact['name']}: {contact['phone']}\n"
       
        messagebox.showinfo("Report", report)

if __name__ == "__main__":
    root = tk.Tk()
    app = FoodManagementApp(root)
    root.mainloop()
