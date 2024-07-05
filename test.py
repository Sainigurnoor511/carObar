import tkinter as tk

def validate_entry(value):
    # Check if the value is a 10-digit number
    return value.isdigit() and len(value) == 10

def main():
    root = tk.Tk()
    root.title("10-Digit Number Entry")

    # Register the validation function
    validate_command = root.register(validate_entry)

    # Create an entry widget with validation
    entry = tk.Entry(root, validate="key", validatecommand=(validate_command, '%P'))
    entry.pack(padx=20, pady=20)

    # Add a label to show messages
    message_label = tk.Label(root, text="")
    message_label.pack(pady=10)

    # Add a button to check the entry
    def check_entry():
        value = entry.get()
        if validate_entry(value):
            message_label.config(text="Valid 10-digit number", fg="green")
        else:
            message_label.config(text="Invalid entry. Please enter a 10-digit number.", fg="red")

    check_button = tk.Button(root, text="Check", command=check_entry)
    check_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
