# Made by: Andrea Baulita
# Date: 09-16-2024
# Description: A python program for checking if a given number is prime or not and finding the factorial of that given number.
#              This program makes use of custom tkinter GUI for user input and output.

import math # used for square root function
import time # used to time the functions for efficiency
import customtkinter as ctk # custom tkinter module used for the GUI

ctk.set_appearance_mode("system")  # You can also set "light" or "system"
ctk.set_default_color_theme("dark-blue")

class App(ctk.CTk):
    # function to check if a number is prime or not
    def prime_number_check(self, num):
        # a prime number must be greater than 1, so we return False if numbers <= 1
        if num <= 1:
            return False
        
        # we only need to check divisors up to the square root of the number for efficiency
        # if a number has a divisor greater than its square root, it will also have a divisor less than the square root
        for i in range(2, int(math.sqrt(num)) + 1):
            # if num is divisible by any number between 2 and sqrt(num), it is not prime so we return False in that case
            if num % i == 0:
                return False
        
        # if no divisors were found, the number is prime
        return True

    # function to calculate the factorial of a number
    def factorial_of_number(self, num):
        # initializing the result to 1, as factorial starts with multiplying by 1
        result = 1
        
        # loop through all numbers from 2 to num and multiply the result by each number
        for i in range(2, num + 1):
            result *= i
        
        # return the final result which is the factorial of the number
        return result
    
    # function to handle submit button click and display results
    def on_submit(self):
        try:
            num = int(self.entry.get())
            is_prime = self.prime_number_check(num)
            factorial_result = self.factorial_of_number(num)
            prime_text = "Prime" if is_prime else "Not Prime"
            
            result_text = f"Number: {num}\n{prime_text}\nFactorial:\n{factorial_result}"
            
            # displays the result in the label
            self.result_box_label.configure(text=result_text)
            self.result_frame.grid()  # this makes the result frame visible
        except ValueError:
            self.result_box_label.configure(text="Please enter a valid integer.")
            self.result_frame.grid()  # ensures the result frame is shown for error as well
    
    def __init__(self):
        super().__init__()
        self.title("Elinnov Demo")
        self.geometry("800x400")  # setting the starting window size to 800x400
        self.minsize(400, 200) # setting the minimum window size
        
        # configuring the grid weights for responsiveness
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)

         # a header label (with wrapping text for better UI)
        self.header_label = ctk.CTkLabel(self, text="Prime Number & Factorial Calculator",
                                 font=("Helvetica", 20, "bold"), wraplength=600)
        self.header_label.grid(row=0, column=0, padx=20, pady=10, sticky="ew")  # sticky allows the label to fill horizontally

        # an input box for the user to enter a number
        self.entry = ctk.CTkEntry(self, placeholder_text="Enter a number")
        self.entry.grid(row=1, column=0, padx=20, pady=10, sticky="ew") 

        # a submit button to run the calculations
        self.submit_button = ctk.CTkButton(self, text="Submit", command=self.on_submit, width=150, height=40, corner_radius=10)
        self.submit_button.grid(row=2, column=0, padx=20, pady=10)
        self.bind("<Return>", lambda event: self.on_submit()) # give the user the option to press "Enter" to submit

        # result Frame (initially hidden, only shown after submit)
        self.result_frame = ctk.CTkFrame(self, fg_color="gray15", corner_radius=10, width=500)
        self.result_frame.grid_forget() # initially hiding the result frame by removing it from the grid layout

         # result Label inside the frame (for displaying result with wrapping so the factorial result does not get cut out)
        self.result_box_label = ctk.CTkLabel(self.result_frame, text="", font=("Helvetica", 16), anchor="w", justify="left", wraplength=500)
        self.result_box_label.pack(padx=20, pady=20, fill="both", expand=True)


app = App() # creating the app object
app.mainloop() # running the main loop for the GUI


# ***** initial sample test for logic check (prints in terminal once session is terminated)*****
num = 5 # static value just for testing

# checking the runtime of the prime number check & factorial functions for efficiency
start_time = time.time()
is_prime = app.prime_number_check(num)
end_time = time.time()

start_time = time.time()
factorial_result = app.factorial_of_number(num)
end_time = time.time()

print(f"Prime Check: {is_prime}, Time Taken: {end_time - start_time:.6f} seconds")
print(f"Factorial: {factorial_result}, Time Taken: {end_time - start_time:.6f} seconds")