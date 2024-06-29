import tkinter as tk
import customtkinter as ctk
from CTkMenuBar import *
import time

class Clock(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.day_counter = ctk.CTkLabel(self, text="", font=("Arial", 50), text_color="#FFFFFF")
        self.percentage_of_year = ctk.CTkLabel(self, text="", font=("Arial", 50), text_color="#FFFFFF")

        self.day_counter.pack(fill="x", pady=10, padx=10)
        self.percentage_of_year.pack(fill="x", pady=10, padx=10)
        
        button = ctk.CTkButton(master, text="CTkButton")
        
        menu = CTkMenuBar(master, bg_color="#2b2b2b")
        font = menu.add_cascade("Font")
        tc = menu.add_cascade("Text Color")
        bc = menu.add_cascade("Background Color")
        
        fontdropdown = CustomDropdownMenu(widget=font)
        fontdropdown.add_option(option="Arial", command=lambda: self.set_font("Arial"))
        fontdropdown.add_option(option="Times New Roman", command=lambda: self.set_font("Times New Roman"))
        
        tcdropdown = CustomDropdownMenu(widget=tc)
        tcdropdown.add_option(option="Black", command=lambda: self.set_color("black"))
        tcdropdown.add_option(option="White", command=lambda: self.set_color("white"))
        tcdropdown.add_option(option="Red", command=lambda: self.set_color("red"))
        tcdropdown.add_option(option="Yellow", command=lambda: self.set_color("yellow"))
        tcdropdown.add_option(option="Green", command=lambda: self.set_color("green"))
        tcdropdown.add_option(option="Blue", command=lambda: self.set_color("blue"))
        tcdropdown.add_option(option="Cyan", command=lambda: self.set_color("cyan"))
        tcdropdown.add_option(option="Purple", command=lambda: self.set_color("purple"))
        
        bcdropdown = CustomDropdownMenu(widget=bc)
        bcdropdown.add_option(option="Black", command=lambda: self.set_background_color("black"))
        bcdropdown.add_option(option="White", command=lambda: self.set_background_color("white"))
        bcdropdown.add_option(option="Blue", command=lambda: self.set_background_color("blue"))
        bcdropdown.add_option(option="Yellow", command=lambda: self.set_background_color("yellow"))
        bcdropdown.add_option(option="Red", command=lambda: self.set_background_color("red"))



        self.update_day_counter()
        self.update_percentage_of_year()

    def set_font(self, font_name):
        self.day_counter.configure(font=(font_name, 50))
        self.percentage_of_year.configure(font=(font_name, 50))

    def set_color(self, color):
        self.day_counter.configure(text_color=color)
        self.percentage_of_year.configure(text_color=color)

    def set_background_color(self, color):
        self.configure(fg_color=color)
        self.day_counter.configure(fg_color=color)
        self.percentage_of_year.configure(fg_color=color)

    def update_day_counter(self):
        now = time.localtime()
        self.day_counter.configure(text=f"Day Count: {now.tm_yday}")

    def get_current_day(self):
        now = time.localtime()
        return now.tm_yday - 1

    def update_percentage_of_year(self):
        current_day = self.get_current_day()
        total_days_in_year = 365
        self.percentage_of_year.configure(text=f"Year Completed: {round(current_day / total_days_in_year * 100, 1)}%")

    def update_labels(self):
        self.update_day_counter()
        self.update_percentage_of_year()

        self.after(1000, self.update_labels)

def main():
    root = ctk.CTk()
    root.title("Yearly Tracker")
    clock = Clock(root)
    clock.pack(fill="both", expand=True)
    clock.update_labels()
    root.mainloop()

if __name__ == "__main__":
    main()