"""
Creates a graphical user interface (GUI) application using the Tkinter library for helping users decide where to dine.
It provides options for selecting the dining method (dine-in or take-out), generating random restaurant choices, and
viewing a complete list of restaurants.
"""

# src/main.py
import tkinter as tk
from tkinter import (
    Button,
    font,
    Frame,
    Label,
    Listbox,
    Scrollbar
    )

from restaurants import Restaurants

# GLOBAL VARIABLES
# Initialize an empty String to store the order method
order_method = ""

# Initialize an empty list to store restaurant data
restaurant_list = []

# Define width and height for the main window
WIDTH = 750
HEIGHT = 500

# Define a dictionary for color configurations
COLORS_DICTIONARY = {
    "back_button_bg": "red",
    "back_button_fg": "white",
    "button_bg": "blue",
    "button_fg": "white",
    "background": "skyblue",
    "text": "black"
}



# EVENT HANDLERS
def dine_in_button_action(root, font_styles):
    """
    Sets the order method to "dine-in" and calls the function to display the option selector frame.
    Args:
        root (Tk): The root Tkinter window.
        font_styles (list): A list of font styles.
    Returns:
        None
    """
    global order_method
    order_method = "dine-in"
    display_option_selector_frame(root, font_styles)

def take_out_button_action(root, font_styles):
    """
    Sets the order method to "take-out" and calls the function to display the option selector frame.
    Args:
        root (Tk): The root Tkinter window.
        font_styles (list): A list of font styles.
    Returns:
        None
    """
    global order_method
    order_method = "take-out"
    display_option_selector_frame(root, font_styles)

def random_choice_button_action(root, font_styles):
    """
    Generates a random restaurant choice and calls the funciton to displays the random restaurant frame.
    Handles assertion errors thrown by the Restaurants class and any other exception thrown otherwise.
    Args:
        root (Tk): The root Tkinter window.
        font_styles (list): A list of font styles.
    Returns:
        None
    """
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
    """
    Generates a random list of restaurants and calls the function to displays the random list frame.
    Handles assertion errors thrown by the Restaurants class and any other exception thrown otherwise.
    Returns:
        None
    """
    # Declares the size of the list to generate
    LIST_SIZE = 3

    try:
        restaurants = Restaurants(order_method)
        global restaurant_list
        restaurant_list = restaurants.generate_random_list(LIST_SIZE)
        display_random_list_frame(root, font_styles)
    except AssertionError as e:
        print("Error in Restaurant class: {e}")
    except Exception as e:
        print(f"Exception thrown from view_all_button_action function: {e}")

def view_all_button_action():
    """
    Retrieves the complete list of restaurants and displays the view all frame.
    Handles assertion errors thrown by the Restaurants class and any other exception thrown otherwise.
    Returns:
        None
    """
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
    """
    Displays the order method selection frame.
    Args:
        root (Tk): The root Tkinter window.
        font_styles (list): A list of font styles.
    Returns:
        None
    """
    # Creates and configures the frame
    order_method_frame = Frame(root)
    order_method_frame.grid(row = 0, column = 0, sticky = "nsew")
    order_method_frame.configure(background = COLORS_DICTIONARY["background"])
    order_method_frame.columnconfigure(0, weight = 1)
    order_method_frame.columnconfigure(1, weight = 1)
    order_method_frame.rowconfigure(0, weight = 1)

    # Creates and configures the dine in button
    dine_in_button = Button(order_method_frame, width = 15, height = 5,
                            text = "Dine In", font = font_styles[5],
                            background = COLORS_DICTIONARY["button_bg"], foreground = COLORS_DICTIONARY["button_fg"],
                            command = lambda: dine_in_button_action(root, font_styles)
                            )
    dine_in_button.grid(row = 0, column = 0, padx = 10, pady = 10)

    # Creates and configures the take out button
    take_out_button = Button(order_method_frame, width = 15, height = 5,
                             text = "Take Out", font = font_styles[5],
                             background = COLORS_DICTIONARY["button_bg"], foreground = COLORS_DICTIONARY["button_fg"],
                             command = lambda: take_out_button_action(root, font_styles))
    take_out_button.grid(row = 0, column = 1, padx = 10, pady = 1)

def display_option_selector_frame(root, font_styles):
    """
    Displays the option selector frame with buttons.
    Args:
        root (Tk): The root Tkinter window.
        font_styles (list): A list of font styles.
    Returns:
        None
    """
    # Creates and configures the frame
    option_selector_frame = Frame(root)
    option_selector_frame.grid(row = 0, column = 0, sticky = "nsew")
    option_selector_frame.configure(background = COLORS_DICTIONARY["background"])
    option_selector_frame.columnconfigure(0, weight = 1)
    option_selector_frame.rowconfigure(0, weight = 1)
    option_selector_frame.rowconfigure(1, weight = 1)
    option_selector_frame.rowconfigure(2, weight = 1)
    option_selector_frame.rowconfigure(3, weight = 1)

    # Creates and configures the random choice button
    random_choice_button = Button(
        option_selector_frame, width = 35, height = 2,
        text = "Random Resturant", font = font_styles[5],
        background = COLORS_DICTIONARY["button_bg"], foreground = COLORS_DICTIONARY["button_fg"],
        command = lambda: random_choice_button_action(root, font_styles)
        )
    random_choice_button.grid(row = 0, column = 0, padx = 10, pady = 10)

    # Creates and configures the random list button
    random_list_button = Button(
        option_selector_frame, width = 35, height = 2,
        text = "Generate Random List", font = font_styles[5],
        background = COLORS_DICTIONARY["button_bg"], foreground = COLORS_DICTIONARY["button_fg"],
        command = random_list_button_action
        )
    random_list_button.grid(row = 1, column = 0, padx = 10, pady = 10)

    # Creates and configures the view All button
    view_all_button = Button(
        option_selector_frame, width = 35, height = 2,
        text = "View All Options", font = font_styles[5],
        background = COLORS_DICTIONARY["button_bg"], foreground = COLORS_DICTIONARY["button_fg"],
        command = view_all_button_action
        )
    view_all_button.grid(row = 2, column = 0, padx = 10, pady = 10)

    # Creates and configures the back button
    back_button = Button(
        option_selector_frame,
        text="Go Back", font = font_styles[0],
        background = COLORS_DICTIONARY["back_button_bg"], foreground = COLORS_DICTIONARY["back_button_fg"],
        command = lambda: display_order_method_frame(root, font_styles)
        )
    back_button.grid(row = 3, column = 0, padx = 10, pady = 10)

def display_random_restaurant_frame(root, font_styles):
    """
    Displays a random restaurant and its details.
    Args:
        root (Tk): The root Tkinter window.
        font_styles (list): A list of font styles.
    Returns:
        None
    """
    # Declares the Strings for the text of the labels
    restaurant_reason_string = "How about " + restaurant_list[0]["reason"]
    restaurant_name_string = "at " + restaurant_list[0]["name"]

    # Creates and configures the frame
    random_restaurant_frame = Frame(root, width = WIDTH, height = HEIGHT)
    random_restaurant_frame.place(x = 0, y = 0, relx = 0, rely = 0)
    random_restaurant_frame.configure(background = COLORS_DICTIONARY["background"])

    # Creates and configures the restaurant's reason label
    reason_label = Label(
        random_restaurant_frame,
        text = restaurant_reason_string, font = font_styles[3],
        background = COLORS_DICTIONARY["background"], foreground = COLORS_DICTIONARY["text"]
        )
    reason_label.place(x = 10, y = (HEIGHT / 2 - 110))

    # Creates and configures the restaurant's name label
    name_label = Label(
        random_restaurant_frame,
        text = restaurant_name_string, font = font_styles[3],
        background = COLORS_DICTIONARY["background"], foreground = COLORS_DICTIONARY["text"]
        )
    name_label.place(x = 10, y = (HEIGHT / 2 - 110 + 40))

    # Creates and configures the regenerate response button
    regen_button = Button(
        random_restaurant_frame,
        text = "Regenerate", font = font_styles[2],
        background = COLORS_DICTIONARY["button_bg"], foreground = COLORS_DICTIONARY["button_fg"],
        command = lambda: random_choice_button_action(root, font_styles)
        )
    regen_button.place(x = 315, y = HEIGHT - 110)

    # Creates and configures the back button
    back_button = Button(
        random_restaurant_frame,
        text = "Go Back", font = font_styles[0],
        background = COLORS_DICTIONARY["back_button_bg"], foreground = COLORS_DICTIONARY["back_button_fg"],
        command = lambda: display_option_selector_frame(root, font_styles)
        )
    back_button.place(x = 337, y = HEIGHT - 57)

def display_random_list_frame(root, font_styles):
    """
    Displays a list of random restaurants.
    Args:
        root (Tk): The root Tkinter window.
        font_styles (list): A list of font styles.
    Returns:
        None
    """
    # Declares the Strings for the text of the labels
    restaurant1 = "1. " + restaurant_list[0]["name"]
    restaurant2 = "2. " + restaurant_list[1]["name"]
    restaurant3 = "3. " + restaurant_list[2]["name"]

    # Creates and configures the frame
    random_list_frame = Frame(root, width = WIDTH, height = HEIGHT)
    random_list_frame.place(x = 0, y = 0, relx = 0, rely = 0)
    random_list_frame.configure(background = COLORS_DICTIONARY["background"])

    # Creates and configures the restaurant 1 label
    restaurant1_label = Label(
        random_list_frame,
        text = restaurant1, font = font_styles[3],
        background = COLORS_DICTIONARY["background"], foreground = COLORS_DICTIONARY["text"]
        )
    restaurant1_label.place(x = 20, y = 100)

    # Creates and configures the restaurant 2 label
    restaurant2_label = Label(
        random_list_frame,
        text = restaurant2, font = font_styles[3],
        background = COLORS_DICTIONARY["background"], foreground = COLORS_DICTIONARY["text"]
        )
    restaurant2_label.place(x = 20, y = 150)

    # Creates and congiures the restaurant 3 label
    restaurant3_label = Label(
        random_list_frame,
        text = restaurant3, font = font_styles[3],
        background = COLORS_DICTIONARY["background"], foreground = COLORS_DICTIONARY["text"]
        )
    restaurant3_label.place(x = 20, y = 200)
    
    # Creates and configures the regenerate response button
    regen_button = Button(
        random_list_frame,
        text = "Regenerate", font = font_styles[2],
        background = COLORS_DICTIONARY["button_bg"], foreground = COLORS_DICTIONARY["button_fg"],
        command = lambda: random_list_button_action()
        )
    regen_button.place(x = 315, y = (HEIGHT - 110))

    # Creates and configures the back button
    back_button = Button(
        random_list_frame,
        text = "Go Back", font = font_styles[0],
        background = COLORS_DICTIONARY["back_button_bg"], foreground = COLORS_DICTIONARY["back_button_fg"],
        command = lambda: display_option_selector_frame(root, font_styles)
        )
    back_button.place(x = 337, y = HEIGHT - 57)

def display_view_all_frame(root, font_styles):
    """
    Displays the complete list of restaurants.
    Args:
        root (Tk): The root Tkinter window.
        font_styles (list): A list of font styles.
    Returns:
        None
    """
    # Creates and configures the frame
    view_all_frame = Frame(root, width = WIDTH, height = HEIGHT)
    view_all_frame.place(x = 0, y = 0, relx = 0, rely = 0)
    view_all_frame.configure(background = COLORS_DICTIONARY["background"])

    # Creates the list box
    listbox = Listbox(
        view_all_frame, activestyle = 'dotbox',
        font = font_styles[1],
        background = COLORS_DICTIONARY["background"], foreground = COLORS_DICTIONARY["text"]
        )
    
    # Creates and configures the scroll bar
    scrollbar = Scrollbar(view_all_frame)
    scrollbar.config(command = listbox.yview)
    scrollbar.place(x = (WIDTH - 18), y = 0, height = 400)

    # Configures the list box
    listbox.config(yscrollcommand = scrollbar.set)
    listbox.place(x = 0, y = 0, height = 400, width = 732)

    # Populate the list box with restaurant names
    for index in range(len(restaurant_list)):
        if (index < 9):
            listbox.insert(index, "  " + str(index+1) + ". " + restaurant_list[index])
        else:
            listbox.insert(index, str(index+1) + ". " + restaurant_list[index])

    # Creates and configures the back button
    back_button = Button(
        view_all_frame,
        text = "Go Back", font = font_styles[0],
        background = COLORS_DICTIONARY["back_button_bg"], foreground = COLORS_DICTIONARY["back_button_fg"],
        command = lambda: display_option_selector_frame(root, font_styles)
        )
    back_button.place(x = 337, y = (HEIGHT - 57))



# MAIN
if __name__ == "__main__":
    # Creates and configure the GUI window
    root = tk.Tk()
    root.iconbitmap("src/images/dining_icon.ico")
    root.title("Dining Dilemma")
    root.geometry("750x500")
    root.columnconfigure(0, weight = 1)
    root.rowconfigure(0, weight = 1)
    root.resizable(False, False)

    # Declares an array for font sizes
    font_styles = [
        font.Font(size = 12),
        font.Font(size = 14),
        font.Font(size = 16),
        font.Font(size = 18),
        font.Font(size = 20),
        font.Font(size = 22)
        ]

    # Bring the display order's frame to the front
    display_order_method_frame(root, font_styles)

    # Execute the GUI
    root.mainloop()