# Welcome to my project! Kana Renshu!
# Github: https://github.com/users/nikkeisadev
# Made by: nikkeisadev, with love!

#Basicaly, the requirements are there, but what you must install is: pykakasi, customtkinter, and pillow!
import random, pykakasi, time, os, customtkinter
from PIL import Image

#Basic variables, and all Hiragana Character in one String.
answerIsRight = True
hiragana_chart = "あいうえおかがきぎくぐけげこごさざしじすずせぜそぞただちぢつづてでとどなにぬねのはばぱひびぴふぶぷへべぺほぼぽまみむめもやゆよらりるれろわゐゑをんゔ" 
katakana_chart = "アイウエオカガキギクグケゲコゴサザシジスズセゼソゾタダチヂツヅテデトドナニヌネノハバパヒビピフブプヘベペホボポマミムメモヤユヨラリルレロワヰヱヲンヴヷヸヹヺ"
charFormat = pykakasi.kakasi()
customtkinter.set_appearance_mode("dark")
consoleDebug = '[CONSOLE]> '
roundNumber, rightAnswears = None, None

class KanaRenshu(customtkinter.CTk):
    #If you borred of the background and want to make a bigger one, just change those values.
    width = 424
    height = 128
    #Well, if you noticed that, yes, the width and the height same as the banmners.
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Kana Renshū - The Japanese Learning Program")
        self.geometry(f"{self.width}x{self.height}")
        self.resizable(False, False)

        #Only for console testers, clearing the Console.
        #It's better to have a clean screen after answearing.
        os.system('cls')
        selectedChar = random.choice(hiragana_chart)
        result = charFormat.convert(selectedChar)[0]
               
        self.translatedChar = format(result['hepburn'])
        #Loading the banner, and starts displaying the interface.
        current_path = os.path.dirname(os.path.realpath(__file__))
        self.bg_image = customtkinter.CTkImage(Image.open(current_path + "\\banner.png"),
                                               size=(self.width, self.height))
        self.bg_image_label = customtkinter.CTkLabel(self, image=self.bg_image)
        self.bg_image_label.grid(row=0, column=0)
        self.text_label = customtkinter.CTkButton(self, font=("Arial", 55, 'bold'), text_color='#938CD9', bg_color="#938CD9", text=selectedChar, width=370, height=50, fg_color=("#4B4648", "#4B4648"), corner_radius=(30))
        self.text_label.grid(row=0, column=0, padx=30, pady=(0, 45))
        self.check_button = customtkinter.CTkButton(self, font=("Arial", 10, 'bold'), text_color='#938CD9', bg_color="#938CD9", text="Check ✔", width=370, height=10, fg_color=("#4B4648", "#4B4648"), command=self.checkUserInput, corner_radius=(50))
        self.check_button.grid(row=0, column=0, padx=30, pady=(46, 0))
        self.username_entry = customtkinter.CTkEntry(self, justify='center', text_color='#938CD9', bg_color="#938CD9", font=("Arial", 13, 'bold'), fg_color=("#4B4648", "#4B4648"),  width=370, height=29, placeholder_text="Type the character in romaji: ", corner_radius=(30))
        self.username_entry.grid(row=0, column=0, padx=30, pady=(98, 1))
    
    #Checking the answer.
    def checkUserInput(self):
        
        userInput = self.username_entry.get()
        print(f'{consoleDebug}Trying with {userInput} => {self.translatedChar}')
        
        if self.translatedChar == userInput.lower():
            
            print(f'{consoleDebug}Correct!')
            self.text_label = customtkinter.CTkButton(self, font=("Arial", 56, 'bold'), text_color='#938CD9', text="✔", width=370, height=50, fg_color=("#4B4648", "#4B4648"))
            
            os.system('cls')
            selectedChar = random.choice(hiragana_chart)
            result = charFormat.convert(selectedChar)[0]

            self.translatedChar = format(result['hepburn'])
            self.text_label = customtkinter.CTkButton(self, font=("Arial", 55, 'bold'), text_color='#938CD9', bg_color="#938CD9", text=selectedChar, width=370, height=50, fg_color=("#4B4648", "#4B4648"), corner_radius=(30))
            self.text_label.grid(row=0, column=0, padx=30, pady=(0, 45))
            self.check_button = customtkinter.CTkButton(self, font=("Arial", 10, 'bold'), text_color='#938CD9', bg_color="#938CD9", text="Check ✔", width=370, height=10, fg_color=("#4B4648", "#4B4648"), command=self.checkUserInput, corner_radius=(50))
            self.check_button.grid(row=0, column=0, padx=30, pady=(46, 0))
            self.username_entry = customtkinter.CTkEntry(self, justify='center', text_color='#938CD9', bg_color="#938CD9", font=("Arial", 13, 'bold'), fg_color=("#4B4648", "#4B4648"),  width=370, height=29, placeholder_text="Type the character in romaji: ", corner_radius=(30))
            self.username_entry.grid(row=0, column=0, padx=30, pady=(98, 1))
        
        else:
            os.system('cls')
            selectedChar = random.choice(hiragana_chart)
            result = charFormat.convert(selectedChar)[0]
            
            self.translatedChar = format(result['hepburn'])
            
            print(f'{consoleDebug}Wrong!')
            self.text_label = customtkinter.CTkButton(self, font=("Arial", 55, 'bold'), text_color='#938CD9', bg_color="#938CD9", text=selectedChar, width=370, height=50, fg_color=("#765793", "#765793"), corner_radius=(30))
            self.text_label.grid(row=0, column=0, padx=30, pady=(0, 45))
            self.check_button = customtkinter.CTkButton(self, font=("Arial", 10, 'bold'), text_color='#938CD9', bg_color="#938CD9", text="Check ✔", width=370, height=10, fg_color=("#765793", "#765793"), command=self.checkUserInput, corner_radius=(50))
            self.check_button.grid(row=0, column=0, padx=30, pady=(46, 0))
            self.username_entry = customtkinter.CTkEntry(self, justify='center', text_color='#938CD9', bg_color="#938CD9", font=("Arial", 13, 'bold'), fg_color=("#4B4648", "#4B4648"),  width=370, height=29, placeholder_text="Wrong romaji!", corner_radius=(30))
            self.username_entry.grid(row=0, column=0, padx=30, pady=(98, 1))

if __name__ == "__main__":
    
    app = KanaRenshu()
    app.mainloop()
