import tkinter
import tkinter.messagebox
import customtkinter
import requests
import webbrowser
from PIL import Image, ImageTk
import spotify

customtkinter.set_appearance_mode("system")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

class App(customtkinter.CTk):

    WIDTH = 960
    HEIGHT = 540

    URLS = []

    def __init__(self):
        super().__init__()

        self.title("KPOP Dictionary")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        image = Image.open("spotify-hex-colors-gradient-background.png").resize((self.WIDTH, self.HEIGHT))
        self.bg_image = ImageTk.PhotoImage(image)

        self.image_label = tkinter.Label(master=self, image=self.bg_image)
        self.image_label.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        # two frames -> grid 2x1
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self, width=320, corner_radius=2)
        self.frame_left.grid(row=0, column=0, sticky="nswe", padx=10, pady=10)

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=10, pady=10)

        # left frame -> grid 1x11
        self.frame_left.grid_rowconfigure(0, minsize=10)   # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(5, weight=1)  # empty row as spacing
        self.frame_left.grid_rowconfigure(9, minsize=20)    # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(11, minsize=10)  # empty row with minsize as spacing

        self.title_label = customtkinter.CTkLabel(master=self.frame_left,
                                                  text="KPOP Dictionary",
                                                  text_font=("Roboto Medium", -36))
        self.title_label.grid(row=1, column=0, padx=20, pady=20)

        self.search_label = customtkinter.CTkLabel(master=self.frame_left,
                                                   text="Type in search term",
                                                   text_font=("Roboto Medium", -24))
        self.search_label.grid(row=2, column=0, padx=20, pady=20)

        self.entrybox = customtkinter.CTkEntry(master=self.frame_left,
                                               width=300,
                                               placeholder_text="e.g. Next Level",
                                               text_font=("Roboto Medium", -22))
        self.entrybox.grid(row=3, column=0, padx=20, pady=20)

        self.type_label = customtkinter.CTkLabel(master=self.frame_left,
                                                 text="Choose term type",
                                                 text_font=("Roboto Medium", -24))
        self.type_label.grid(row=4, column=0, padx=20, pady=20)
        
        self.radio_var = tkinter.IntVar(value=0)
        self.radio_button_1 = customtkinter.CTkRadioButton(master=self.frame_left,
                                                           variable=self.radio_var,
                                                           value=0,
                                                           text="Song",
                                                           text_font=("Roboto Medium", -22),
                                                           command=self.radiobutton_event)
        self.radio_button_1.grid(row=6, column=0, padx=20, pady=10)
        self.radio_button_2 = customtkinter.CTkRadioButton(master=self.frame_left,
                                                           variable=self.radio_var,
                                                           value=1,
                                                           text="Album",
                                                           text_font=("Roboto Medium", -22),
                                                           command=self.radiobutton_event)
        self.radio_button_2.grid(row=7, column=0, padx=20, pady=10)
        self.radio_button_3 = customtkinter.CTkRadioButton(master=self.frame_left,
                                                           variable=self.radio_var,
                                                           value=2,
                                                           text="Artist",
                                                           text_font=("Roboto Medium", -22),
                                                           command=self.radiobutton_event)
        self.radio_button_3.grid(row=8, column=0, padx=20, pady=10)

        self.button = customtkinter.CTkButton(master=self.frame_left,
                                              text="Search term",
                                              text_font=("Roboto Medium", -22),
                                              command=self.button_event)
        self.button.grid(row=9, column=0, padx=20, pady=10)

    def button_event(self):
        print(self.entrybox.get())
        if self.entrybox.get() == "":
            return

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=10, pady=10)
        
        image_urls = []
        urls = []
        image_urls, App.URLS = spotify.search_spotify(self.entrybox.get(), self.radio_var.get())
        count = len(image_urls) if len(image_urls) <= 9 else 9
        for i in range(0, count):
            image = Image.open(requests.get(image_urls[i], stream=True).raw).resize((150, 150))
            button = customtkinter.CTkButton(self.frame_right, image=ImageTk.PhotoImage(image), text="")
            if i == 0:
                button.configure(command = self.button_1)
            elif i == 1:
                button.configure(command = self.button_2)
            elif i == 2:
                button.configure(command = self.button_3)
            elif i == 3:
                button.configure(command = self.button_4)
            elif i == 4:
                button.configure(command = self.button_5)
            elif i == 5:
                button.configure(command = self.button_6)
            elif i == 6:
                button.configure(command = self.button_7)
            elif i == 7:
                button.configure(command = self.button_8)
            else:
                button.configure(command = self.button_9)    
            r = int(i / 3)
            c = int(i % 3)
            button.grid(row=r,column=c, padx=20, pady=10)

    def button_1(self):
        webbrowser.open(App.URLS[0])
    
    def button_2(self):
        webbrowser.open(App.URLS[1])
    
    def button_3(self):
        webbrowser.open(App.URLS[2])

    def button_4(self):
        webbrowser.open(App.URLS[3])

    def button_5(self):
        webbrowser.open(App.URLS[4])

    def button_6(self):
        webbrowser.open(App.URLS[5])

    def button_7(self):
        webbrowser.open(App.URLS[6])

    def button_8(self):
        webbrowser.open(App.URLS[7])

    def button_9(self):
        webbrowser.open(App.URLS[8])

    def radiobutton_event(self):
        print("radiobutton toggled, current value:", self.radio_var.get())

    def on_closing(self, event=0):
        self.destroy()

if __name__ == "__main__":
    app = App()
    app.mainloop()