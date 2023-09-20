# src/main.py
from backend.restaurants import Restaurants
import tkinter as tk
from tkinter import (
    Button,
    font,
    Frame,
    Label,
    Listbox,
    Scrollbar
    )

# GLOBAL VARIABLES
order_method = ""
restaurant_list = []
WIDTH = 750
HEIGHT = 500



# EVENT HANDLERS
def dine_in_button_action(root, font_styles):
    global order_method
    order_method = "dine-in"
    display_option_selector_frame(root, font_styles)

def take_out_button_action(root, font_styles):
    global order_method
    order_method = "take-out"
    display_option_selector_frame(root, font_styles)

def random_choice_button_action(root, font_styles):
    try:
        restaurants = Restaurants(order_method)
        global restaurant_list
        restaurant_list = restaurants.generate_random_list()
        display_random_restaurant_frame(root, font_styles)
    except AssertionError as e:
        print("Error in Restaurant class: {e}")
    except Exception as e:
        print(f"Exception thrown from view_all_button_action function: {e}")

def random_list_button_action():
    list_size = 3

    try:
        restaurants = Restaurants(order_method)
        global restaurant_list
        restaurant_list = restaurants.generate_random_list(list_size)
        display_random_list_frame(root, font_styles)
    except AssertionError as e:
        print("Error in Restaurant class: {e}")
    except Exception as e:
        print(f"Exception thrown from view_all_button_action function: {e}")

def view_all_button_action():
    try:
        restaurants = Restaurants(order_method)
        global restaurant_list
        restaurant_list = restaurants.get_restaurants_list()
        display_view_all_frame(root, font_styles)
    except AssertionError as e:
        print("Error in Restaurant class: {e}")
    except Exception as e:
        print(f"Exception thrown from random_list_button_action: {e}")



# FRAMES
def display_order_method_frame(root, font_styles):
    order_method_frame = Frame(root, background="LightBlue1")
    order_method_frame.grid(row=0, column=0, sticky="nsew")

    order_method_frame.columnconfigure(0, weight=1)
    order_method_frame.columnconfigure(1, weight=1)
    order_method_frame.rowconfigure(0, weight=1)

    dine_in_button = Button(order_method_frame, text="Dine In", width=15, height=5, font=font_styles[5], command=lambda: dine_in_button_action(root, font_styles))
    dine_in_button.grid(row=0, column=0, padx=10, pady=10)

    take_out_button = Button(order_method_frame, text="Take Out", width=15, height=5, font=font_styles[5], command=lambda: take_out_button_action(root, font_styles))
    take_out_button.grid(row=0, column=1, padx=10, pady=1)

def display_option_selector_frame(root, font_styles):
    option_selector_frame = Frame(root, background="LightPink2")
    option_selector_frame.grid(row=0, column=0, sticky="nsew")

    option_selector_frame.columnconfigure(0, weight=1)
    option_selector_frame.rowconfigure(0, weight=1)
    option_selector_frame.rowconfigure(1, weight=1)
    option_selector_frame.rowconfigure(2, weight=1)
    option_selector_frame.rowconfigure(3, weight=1)

    random_choice_button = Button(option_selector_frame, text="Random Resturant", width=35, height=2, font=font_styles[5], command=lambda: random_choice_button_action(root, font_styles))
    random_choice_button.grid(row=0, column=0, padx=10, pady=10)

    random_list_button = Button(option_selector_frame, text="Generate Random List", width=35, height=2, font=font_styles[5], command=random_list_button_action)
    random_list_button.grid(row=1, column=0, padx=10, pady=10)

    view_all_button = Button(option_selector_frame, text="View All Options", width=35, height=2, font=font_styles[5], command=view_all_button_action)
    view_all_button.grid(row=2, column=0, padx=10, pady=10)

    back_button = Button(option_selector_frame, text="Go Back", font=font_styles[0], command=lambda: display_order_method_frame(root, font_styles))
    back_button.grid(row=3, column=0, padx=10, pady=10)


def display_random_restaurant_frame(root, font_styles):
    background_color = "Gold"
    restaurant_reason_string = "How about " + restaurant_list[0]["reason"]
    restaurant_name_string = "at " + restaurant_list[0]["name"]

    random_restaurant_frame = Frame(root, width=WIDTH, height=HEIGHT, background=background_color)
    random_restaurant_frame.place(x=0, y=0, relx=0, rely=0)

    reason_label = Label(random_restaurant_frame, text=restaurant_reason_string, font=font_styles[3], background=background_color)
    reason_label.place(x = 10, y= HEIGHT / 2 - 110)

    name_label = Label(random_restaurant_frame, text=restaurant_name_string, font=font_styles[3], background=background_color)
    name_label.place(x = 10, y= HEIGHT / 2 - 110 + 40)

    regen_button = Button(random_restaurant_frame, text="Regenerate", font=font_styles[2], command=lambda: random_choice_button_action(root, font_styles))
    regen_button.place(x = 315, y = HEIGHT - 110)

    back_button = Button(random_restaurant_frame, text="Go Back", font=font_styles[0], command=lambda: display_option_selector_frame(root, font_styles))
    back_button.place(x = 337, y = HEIGHT - 57)

def display_random_list_frame(root, font_styles):
    background_color = "SeaGreen"
    restaurant1 = "1. " + restaurant_list[0]["name"]
    restaurant2 = "2. " + restaurant_list[1]["name"]
    restaurant3 = "3. " + restaurant_list[2]["name"]

    random_list_frame = Frame(root, width=WIDTH, height=HEIGHT, background=background_color)
    random_list_frame.place(x=0, y=0, relx=0, rely=0)

    restaurant1_label = Label(random_list_frame, text=restaurant1, font=font_styles[3], background=background_color)
    restaurant1_label.place(x = 20, y = 100)

    restaurant2_label = Label(random_list_frame, text=restaurant2, font=font_styles[3], background=background_color)
    restaurant2_label.place(x = 20, y = 150)

    restaurant3_label = Label(random_list_frame, text=restaurant3, font=font_styles[3], background=background_color)
    restaurant3_label.place(x = 20, y = 200)
    
    regen_button = Button(random_list_frame, text="Regenerate", font=font_styles[2], command=lambda: random_list_button_action())
    regen_button.place(x = 315, y = HEIGHT - 110)

    back_button = Button(random_list_frame, text="Go Back", font=font_styles[0], command=lambda: display_option_selector_frame(root, font_styles))
    back_button.place(x = 337, y = HEIGHT - 57)

def display_view_all_frame(root, font_styles):
    background_color = "MediumPurple1"

    view_all_frame = Frame(root, width=WIDTH, height=HEIGHT, background=background_color)
    view_all_frame.place(x=0, y=0, relx=0, rely=0)

    listbox = Listbox(view_all_frame, activestyle = 'dotbox', background = background_color, font=font_styles[1])
    scrollbar = Scrollbar(view_all_frame)
    scrollbar.config(command = listbox.yview)
    listbox.config(yscrollcommand = scrollbar.set)
    listbox.place(x=0, y=0, height = 400, width = 732)
    scrollbar.place(x=WIDTH-18, y=0,height=400)

    # Populate the Listbox with restaurant names
    for index in range(len(restaurant_list)):
        if (index < 9):
            listbox.insert(index, "  " + str(index+1) + ". " + restaurant_list[index])
        else:
            listbox.insert(index, str(index+1) + ". " + restaurant_list[index])

    back_button = Button(view_all_frame, text="Go Back", font=font_styles[0], command=lambda: display_option_selector_frame(root, font_styles))
    back_button.place(x = 337, y = HEIGHT - 57)



# MAIN
if __name__ == "__main__":
    # CONFIGURE WINDOW
    root = tk.Tk()
    root.iconbitmap("resources\images\dining_icon.ico")
    root.title("Dining Dilemma")
    root.geometry("750x500")
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    root.resizable(False, False)

    font_styles = [font.Font(size=12), font.Font(size=14), font.Font(size=16), font.Font(size=18), font.Font(size=20), font.Font(size=22)]

    display_order_method_frame(root, font_styles)

    # EXECUTE GUI
    root.mainloop()