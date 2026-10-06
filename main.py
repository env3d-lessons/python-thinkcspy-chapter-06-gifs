# Constants for font size and spacing
font_size = 20
font_height = font_size
font_width = font_size * (1 - 0.39)

# Provided function – do not modify
def draw_letter(t, letter):
    height = font_size
    t.setx(t.xcor() - (font_width * 0.6))
    t.sety(t.ycor() - (font_height * 0.8))
    t.write(letter, font=('Courier', font_size))
    t.setx(t.xcor() + (font_width * 0.6))
    t.sety(t.ycor() + (font_height * 0.8))

# Exercise 1
def draw_carbon(t):
    """Draws a single CH₂ group (Carbon with 2 Hydrogens)"""

    # Below we are simply calling draw_letter to draw the letters C and H
    # You will need to modify this function to draw the CH₂ group correctly.
    draw_letter(t, 'C')
    draw_letter(t, 'H')
    draw_letter(t, 'H')
    

# Exercise 2
def draw_carbons(t, num_carbons):
    """Draws a straight line of CH₂ groups (without extra Hs at ends)"""
    # pass simply does nothing, you will need to replace it with your code.
    pass


# Exercise 3
def draw_carbon_chain(t, num_carbons):
    """Draws full CH₃–(CH₂)_n–CH₃ style carbon chain"""    
    # pass simply does nothing, you will need to replace it with your code.
    pass
    

######
## Instructor UI code.  DO NOT MODIFY 
######

def run_drawing(draw_func, *args):
    """Initializes turtle, executes the given drawing function, and exits on click."""
    import turtle
    screen = turtle.Screen()
    screen.title("Carbon Chain Drawer")
    t = turtle.Turtle()
    
    draw_func(t, *args)
    
    print("The output is saved to output.gif")
    screen.exitonclick()


def main_cli():
    print("\n--- Carbon Chain Drawer ---")
    print("1. Draw CH₂")
    print("2. Draw (CH₂)n")
    print("3. Draw Full Chain")            
    
    choice = input("Select an option (1-3): ").strip()

    if choice == "1":
        run_drawing(draw_carbon)

    elif choice == "2":
        try:
            n = int(input("How many CH₂ units? "))
            if n >= 1:
                run_drawing(draw_carbons, n)
            else:
                print("Please enter an integer >= 1.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    elif choice == "3":
        try:
            n = int(input("How many CH₂ units in chain (excluding ends)? "))
            if n >= 0:
                run_drawing(draw_carbon_chain, n)
            else:
                print("Please enter a non-negative integer.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    else:
        print("Invalid selection. Please choose a number between 1 and 3.")


if __name__ == "__main__":
    main_cli()