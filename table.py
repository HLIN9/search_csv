import pandas as pd
import tkinter as tk
from tkinter import ttk
def show_results():
    # Get the search term from the entry widget
    search_term = search_entry.get().lower()

    # Filter the data to find the rows that match the search term
    filtered_data = data[data['act'].str.lower().str.contains(search_term)]

    # Create a new window to display the search results
    result_window = tk.Toplevel(root)
    result_window.title("Search Results")

    # Create a Text widget to display the search results
    result_text = tk.Text(result_window)
    result_text.pack(side='left', fill='both', expand=True)

    # Insert the search results into the Text widget
    for _, row in filtered_data.iterrows():
        result_text.insert('end', f"Act: {row['act']}\n")
        result_text.insert('end', f"Prompt: {row['prompt']}\n\n")

    # Create a button to copy the search results to the clipboard
    def copy_results():
        root.clipboard_clear()
        root.clipboard_append(result_text.get('1.0', 'end-1c'))

    copy_button = tk.Button(result_window, text="Copy", command=copy_results)
    copy_button.pack(side='right', padx=10, pady=10)

    # Start the GUI event loop for the result window
    result_window.mainloop()

def show_all():
    # Create a new window to display the CSV file contents
    all_window = tk.Toplevel(root)
    all_window.title("All Results")

    # Create a Text widget to display the CSV file contents
    all_text = tk.Text(all_window)
    all_text.pack(side='left', fill='both', expand=True)

    # Insert the CSV file contents into the Text widget
    for _, row in data.iterrows():
        all_text.insert('end', f"Act: {row['act']}\n")
        all_text.insert('end', f"Prompt: {row['prompt']}\n\n")

    # Create a button to copy the CSV file contents to the clipboard
    def copy_all():
        root.clipboard_clear()
        root.clipboard_append(all_text.get('1.0', 'end-1c'))

    copy_button = tk.Button(all_window, text="Copy", command=copy_all)
    copy_button.pack(side='right', padx=10, pady=10)

    # Add a scrollbar to the Text widget
    scrollbar = ttk.Scrollbar(all_window, orient='vertical', command=all_text.yview)
    scrollbar.pack(side='right', fill='y')
    all_text.config(yscrollcommand=scrollbar.set)

    # Start the GUI event loop for the all window
    all_window.mainloop()


# Load the CSV file into a pandas dataframe
data = pd.read_csv('prompts.csv')

# Create a tkinter GUI window
root = tk.Tk()
root.title("Prompts Search")

# Create a label and an entry widget for the search keyword
search_label = ttk.Label(root, text='Search keyword:')
search_label.pack(side='left', padx=5, pady=5)
search_entry = ttk.Entry(root)
search_entry.pack(side='left', fill='x', expand=True, padx=5, pady=5)
search_entry.focus() # Set focus to the search entry widget

# Create a search button
search_button = ttk.Button(root, text='Search', command=show_results)
search_button.pack(side='left', padx=5, pady=5)

#Create a show-all button
show_all_button = ttk.Button(root, text='Show All', command=show_all)
show_all_button.pack(side='left', padx=5, pady=5)

# Start the GUI event loop
root.mainloop()

