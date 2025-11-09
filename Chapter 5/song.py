# ===============================
# Terminal Karaoke - Sunny Days
# Non-Copyright Music by FSM Team
# ===============================

import time
import sys

lyrics = [
    ("It's a brand new day, the sun is shining bright", 3),
    ("Take a little breath, everything feels right", 3),
    ("Walking down the road, my worries fade away", 3),
    ("Oh, I'm feeling those sunny days", 3),
    ("Life's a song, so sing it loud", 3),
    ("Let your heart dance in the crowd", 3),
    ("Every step’s a brand new way", 3),
    ("Oh, I'm feeling those sunny days", 3)
]

print("\n🎶 Starting 'Sunny Days' karaoke... 🎶\n")
time.sleep(2)

for line, delay in lyrics:
    for char in line:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    print()
    time.sleep(delay)

print("\n✨ End of song ✨")





import builtins, sys, time

def slow_print(*args, delay=0.03, **kwargs):
    text = " ".join(map(str, args))
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")
    sys.stdout.flush()

builtins.print = slow_print





















# # ===============================
# # GUI Karaoke - Sunny Days
# # ===============================

# import tkinter as tk
# import time

# lyrics = [
#     ("It's a brand new day, the sun is shining bright", 2.5),
#     ("Take a little breath, everything feels right", 2.5),
#     ("Walking down the road, my worries fade away", 2.5),
#     ("Oh, I'm feeling those sunny days", 2.5),
#     ("Life's a song, so sing it loud", 2.5),
#     ("Let your heart dance in the crowd", 2.5),
#     ("Every step’s a brand new way", 2.5),
#     ("Oh, I'm feeling those sunny days", 2.5)
# ]

# root = tk.Tk()
# root.title("🎵 Sunny Days Karaoke 🎵")
# root.geometry("800x300")
# root.configure(bg="#ffe680")

# label = tk.Label(root, text="", font=("Helvetica", 24, "bold"), bg="#ffe680", fg="#ff6600")
# label.pack(expand=True)

# def display_lyrics():
#     for line, delay in lyrics:
#         label.config(text=line)
#         root.update()
#         time.sleep(delay)
#     label.config(text="✨ End of song ✨")

# root.after(1000, display_lyrics)
# root.mainloop()
