import tkinter as tk
import threading
import time
import keyboard
import pyautogui
import random
import win32api, win32con

root = tk.Tk()
root.title("Coinbot")

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def update_colors():
    global colors
    colors = []
    color_list = [color_entry1.get(), color_entry2.get(), color_entry3.get(), color_entry4.get(), color_entry5.get(),color_entry6.get(), color_entry7.get()]
    for c in color_list:
        if c.strip() == '':
            continue
        c = c.strip("'")
        color = tuple(map(int, c.split(',')))
        colors.append(color)

def update_rgb_values():
    global colors
    update_colors()
    while keyboard.is_pressed('q') == False:
        flag = 0
        pic = pyautogui.screenshot(region=(320, 300, 900, 420))

        width, height = pic.size

        for x in range(0, width, 5):
            for y in range(0, height, 5):
                r, g, b = pic.getpixel((x, y))

                for color in colors:
                    if color == (r, g, b):
                        flag = 1
                        click(x + 320, y + 300)
                        time.sleep(0.05)
                        break

                if flag == 1:
                    break

            if flag == 1:
                break

def run_update_rgb_values_thread():
    thread = threading.Thread(target=update_rgb_values)
    thread.start()

colors = []

color_frame = tk.Frame(root)
color_frame.pack()

color_label = tk.Label(color_frame, text="RGB values:")
color_label.pack(side="top")

color1_label = tk.Label(color_frame, text="Bitcoin:")
color1_label.pack(side="top")

color_entry1 = tk.Entry(color_frame)
color_entry1.pack(side="top")

color2_label = tk.Label(color_frame, text="Dashcoin:")
color2_label.pack(side="top")

color_entry2 = tk.Entry(color_frame)
color_entry2.pack(side="top")

color3_label = tk.Label(color_frame, text="Dodgecoin:")
color3_label.pack(side="top")

color_entry3 = tk.Entry(color_frame)
color_entry3.pack(side="top")

color4_label = tk.Label(color_frame, text="Lightcoin:")
color4_label.pack(side="top")

color_entry4 = tk.Entry(color_frame)
color_entry4.pack(side="top")

color8_label = tk.Label(color_frame, text="Additional RGB values")
color8_label.pack(side="top")

color5_label = tk.Label(color_frame, text="R:")
color5_label.pack(side="left")

color_entry5 = tk.Entry(color_frame)
color_entry5.pack(side="left")

color6_label = tk.Label(color_frame, text="G:")
color6_label.pack(side="left")

color_entry6 = tk.Entry(color_frame)
color_entry6.pack(side="left")

color7_label = tk.Label(color_frame, text="B:")
color7_label.pack(side="left")

color_entry7 = tk.Entry(color_frame)
color_entry7.pack(side="left")

update_button = tk.Button(color_frame, text="Update", command=run_update_rgb_values_thread)
update_button.pack(side="top")

root.mainloop()





