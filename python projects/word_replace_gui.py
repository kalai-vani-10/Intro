import tkinter as tk

def replace_word():
    input_text = text_entry.get("1.0", "end-1c")
    word_to_replace = word_to_replace_entry.get()
    word_replacement = word_replacement_entry.get()
    
    if input_text and word_to_replace and word_replacement:
        modified_text = input_text.replace(word_to_replace, word_replacement)
        output_text.delete("1.0", "end")
        output_text.insert("1.0", modified_text)

# Create the main window
root = tk.Tk()
root.title("Word Replacement Tool")

# Create input widgets
text_label = tk.Label(root, text="Enter the text:")
text_label.pack()

text_entry = tk.Text(root, height=5, width=50)
text_entry.pack()

word_to_replace_label = tk.Label(root, text="Enter the word to replace:")
word_to_replace_label.pack()

word_to_replace_entry = tk.Entry(root)
word_to_replace_entry.pack()

word_replacement_label = tk.Label(root, text="Enter word replacement:")
word_replacement_label.pack()

word_replacement_entry = tk.Entry(root)
word_replacement_entry.pack()

replace_button = tk.Button(root, text="Replace", command=replace_word)
replace_button.pack()

output_label = tk.Label(root, text="Modified text:")
output_label.pack()

output_text = tk.Text(root, height=5, width=50)
output_text.pack()

root.mainloop()
