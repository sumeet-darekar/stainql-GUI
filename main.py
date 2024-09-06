import webbrowser
from customtkinter import *
from help import Help
from PIL import Image, ImageTk
import time
from introspection import Intros
from csrf import csrf_attack
from batching import Batching
from fuzzing import Fuzz
import tkinter as tk


help_section = Help()
selected_choice = None


def show_frame(frame):
    frame.tkraise()

def open_link(url):
    webbrowser.open(url)

def retrieve_url():
    url = url_entry.get()
    if url.startswith("http://") or url.startswith("https://"):
        # Update the URL label with the entered URL
        url_label.configure(text=url)
    else:
        url_label.configure(text="Enter a valid url 😤")

def on_entry_change(event):
    # Get the current text from the entry widget and update the label
    input_text = endurl.get()
    url_label6.configure(text=f"Url : {input_text}/FUZZing")


#FUZZING 
def retrieve_url_fuzz():
    url_label2.configure(text="")
    url = endurl.get()
    
    if url.startswith("http://") or url.startswith("https://"):
        # Update the URL label with the entered URL

        url_label1.configure(text=url+"/FUZZing")
        f = Fuzz()
        result = f.fuzzing_graphql(url)

        url_label1.configure(text=result)
    else:
        url_label1.configure(text="Enter a valid url 😤")


#mAin Page
def introspection_query():
    url = url_entry.get()  # Get the URL from the url_label
    if url and (url.startswith("http://") or url.startswith("https://")):
        i = Intros()
        output = i.introspection_query(url)  # Await the async introspection_query method
        
        print(i.introspection_query(url))
        url_label.configure(text=output)
    else:
        url_label.configure(text="Enter a valid url 😤")

'''
def combobox_callback(choice):
    global selected_choice
    selected_choice = choice
    print(f"Combobox selection: {selected_choice}")
'''
def combobox_callback(choice):
    url_label2.configure(text="")
    url_label3.configure(text="")
    url_label4.configure(text="")
    url_label5.configure(text="")
    
    url = url_entry.get()
    print(url, choice)
    
    if choice == "csrf vulnerability" and url:
        c = csrf_attack()
        url_label2.configure(text=c.attack_get(url))
        c = csrf_attack()
        url_label3.configure(text=c.attack_post(url))
    elif choice == "Query based Batching attack" and url:
        url_label2.configure(text="Scanning query based batching attack...")
        url = url_entry.get()

        b = Batching()
        url_label2.configure(text=b.query_batching(url))
    elif choice == "All checks" and url:
        url = url_entry.get()
        url_label2.configure(text="Scanned for both vulnerabilities ...")
        
        # CSRF checks
        c = csrf_attack()
        url_label3.configure(text=c.attack_get(url))
        url_label4.configure(text=c.attack_post(url))
        
        # Batching check
        b = Batching()
        url_label5.configure(text=b.query_batching(url))
	

    else:
        url_label2.configure(text="Something went wrong")


app = CTk()
height = 900
width = 700

app.geometry(f"{height}x{width}")
set_default_color_theme("NightTrain.json")
window_title = "Stainql GUI"
app.title(window_title)

default_frame = CTkFrame(master=app, width=width, height=height)
help_frame = CTkFrame(master=app, width=width, height=height)
fuzz_frame = CTkFrame(master=app, width=width, height=height)

default_frame.grid(row=0, column=0, sticky="nsew")
help_frame.grid(row=0, column=0, sticky="nsew")
fuzz_frame.grid(row=0, column=0, sticky="nsew")

app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=1)

# Create a frame to hold the title and the Help button
top_frame_default = CTkFrame(default_frame, width=width, height=60)
top_frame_default.pack(fill="x", side="top")

bottom_frame = CTkFrame(default_frame, width=width, height=60)
bottom_frame.pack(fill="x", side="bottom")

bottom_frame_help = CTkFrame(help_frame, width=width, height=60)
bottom_frame_help.pack(fill="x", side="bottom")

# Help button aligned to the right
to_help_button = CTkButton(top_frame_default, text="Help", command=lambda: show_frame(help_frame), fg_color=top_frame_default.cget("fg_color"))
to_help_button.pack(pady=5, side="right")

# Fuzz button
to_fuzz_button = CTkButton(top_frame_default, text="FUZZ", command=lambda: show_frame(fuzz_frame), fg_color=top_frame_default.cget("fg_color"))
to_fuzz_button.pack(pady=5, padx=(10, 0), side="right")

window_lower_title = "A graphql testing tool"
title_label = CTkLabel(default_frame, text=window_lower_title, font=("Helvetica", 20), text_color="white")
title_label.pack(pady=10)

# Create a frame to hold the Back to Default button
top_frame_help = CTkFrame(help_frame, width=width, height=60)
top_frame_help.pack(fill="x", side="top")

top_frame_fuzz = CTkFrame(fuzz_frame, width=width, height=60)
top_frame_fuzz.pack(fill="x", side="top")

# Back to Default button aligned to the right
to_default_button = CTkButton(top_frame_help, text="Back to Default Page", command=lambda: show_frame(default_frame))
to_default_button.pack(pady=5, padx=(0, 20), side="right")

to_default_button = CTkButton(top_frame_fuzz, text="Back to Default Page", command=lambda: show_frame(default_frame))
to_default_button.pack(pady=5, padx=(0, 20), side="right")

# Input frame
target_frame = CTkFrame(default_frame, fg_color=default_frame.cget("fg_color"))
target_frame.pack(pady=10)

target_label = CTkLabel(target_frame, text="Target URL:", font=("Helvetica", 15), text_color="white")
target_label.pack(side="left", padx=(0, 10))

url_entry = CTkEntry(target_frame, placeholder_text="https://example.com/graphql", font=("Helvetica", 16), width=300, height=40)
url_entry.pack(side="left", padx=(0, 10), pady=5)

retrieve_button = CTkButton(target_frame, text="Submit", command=retrieve_url)
retrieve_button.pack(side="left", padx=(10, 0), pady=5)

# Output URL label below the input
url_label = CTkLabel(default_frame, text="", font=("Helvetica", 18), text_color="white")
url_label.pack(side="top", pady=10)

vuln_frame = CTkFrame(default_frame, fg_color=default_frame.cget("fg_color"))
vuln_frame.pack(pady=10)

retrieve_button = CTkButton(vuln_frame, text="Introspection query is ON/OFF", font=("Helvetica", 18), command=introspection_query)
retrieve_button.pack(side="left", padx=(10, 0), pady=7)

# Vulnerability check
combobox = CTkComboBox(vuln_frame, values=["Select option", "csrf vulnerability", "Query based Batching attack", "All checks"],
                                     command=combobox_callback, width=210, height=30, font=("Helvetica", 16))
combobox.pack(side="left", padx=20, pady=10)
combobox.set("All checks")

#vuln output print
url_label2 = CTkLabel(default_frame, text="", font=("Helvetica", 18), text_color="white")
url_label2.pack(side="top", pady=10)

url_label3 = CTkLabel(default_frame, text="", font=("Helvetica", 18), text_color="white")
url_label3.pack(side="top", pady=10)

url_label4 = CTkLabel(default_frame, text="", font=("Helvetica", 18), text_color="white")
url_label4.pack(side="top", pady=10)


url_label5 = CTkLabel(default_frame, text="", font=("Helvetica", 18), text_color="white")
url_label5.pack(side="top", pady=10)


# Button container for external links
button_container = CTkFrame(bottom_frame)
button_container.pack(pady=10)

button_container_help = CTkFrame(bottom_frame_help)
button_container_help.pack(pady=10)

stainql_cli_button = CTkButton(button_container, text="stainql CLI", command=lambda: open_link("https://github.com/sumeet-darekar/stainql"), fg_color=top_frame_default.cget("fg_color"))
stainql_cli_button.pack(side="left", padx=5, pady=10)

# Help Sec
stainql_cli_button = CTkButton(button_container_help, text="Documentation", command=lambda: open_link("https://github.com/sumeet-darekar/stainql"), fg_color=top_frame_default.cget("fg_color"))
stainql_cli_button.pack(side="left", padx=5, pady=10)
# Help Sec

portfolio_button = CTkButton(button_container, text="Portfolio", command=lambda: open_link("https://www.noobstain.tech"), fg_color=top_frame_default.cget("fg_color"))
portfolio_button.pack(side="left", padx=5, pady=10)

portfolio_button = CTkButton(button_container, text="Learn Graphql security", command=lambda: open_link("https://noobstain.gitbook.io/graphql"), fg_color=top_frame_default.cget("fg_color"))
portfolio_button.pack(side="left", padx=5, pady=10)

# HELP section
text = help_section.greet()
help_label = CTkLabel(help_frame, text="Help", font=("Helvetica", 20), text_color="white")
help_label.pack(pady=10)

help_sec = CTkLabel(help_frame, text=text, font=("Helvetica", 16), text_color="white", anchor="w", justify="left")
help_sec.pack(pady=10)

# Image help
image_path = "1.png"
img = CTkImage(light_image=Image.open(image_path), size=(500, 400))  # Adjust size as needed

# Display the image in the Help section
image_label = CTkLabel(help_frame, image=img, text="")  # Empty text for pure image display
image_label.pack(pady=10)


# FUZZ page
fuzz_label = CTkLabel(fuzz_frame, text="FUZZing for Endpoints", font=("Helvetica", 20), text_color="white")
fuzz_label.pack(pady=10)

fuzzer_container = CTkFrame(fuzz_frame, fg_color=top_frame_default.cget("fg_color"))
fuzzer_container.pack(pady=10)

endpoint = CTkLabel(fuzzer_container, text="target url :", font=("Helvetica", 20), text_color="white")
endpoint.pack(side="left", padx=5, pady=10)


endurl = CTkEntry(fuzzer_container, placeholder_text="https://example.com", font=("Helvetica", 16), width=300, height=40)
endurl.pack(side="left", padx=(0, 10), pady=5)

retrieve_button1 = CTkButton(fuzzer_container, text="Start", command=retrieve_url_fuzz)
retrieve_button1.pack(side="left", padx=(10, 0), pady=5)

# Move the URL label below the target input
#tar = endurl.get()
url_label6= CTkLabel(fuzz_frame, text=f"", font=("Helvetica", 18), text_color="white")
url_label6.pack(pady=10, side="top")  # Placed in the fuzz_frame, not inside fuzzer_container

endurl.bind("<KeyRelease>", on_entry_change)

url_label1 = CTkLabel(fuzz_frame, text="", font=("Helvetica", 18), text_color="white")
url_label1.pack(pady=10, side="top")  # Placed in the fuzz_frame, not inside fuzzer_container




show_frame(default_frame)

# Run the Tkinter main loop
app.mainloop()
