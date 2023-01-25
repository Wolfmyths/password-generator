import tkinter as tk
import pyperclip as pc
import PasswordGenerator
import threading

root = tk.Tk()
version = '1.2.2'
root.title(f"Wolfmyths' Password Generator V{version}")
root.geometry('800x600')


class mainGUI:

        def __init__(self, master=None): # The 'master' argument is set to optional to prevent a warning in the console, the None value is a placeholder to make python happy
                titleFrame = tk.Frame(master).pack(padx=10, pady=10)
                self.titleLabel = tk.Label(titleFrame, text="Wolfmyths' Password Generator", font=('Ariel', 18)).pack() # Wolfmyths' Password Generator

                # Start of Settings Frame
                settingsFrame = tk.Frame(master)

                # Start of Passphrase Settings Frame
                passphraseSettingsFrame = tk.Frame(settingsFrame)
                self.passphraseLabel = tk.Label(passphraseSettingsFrame, text='Passphrase Settings', font=('Ariel', 18)).pack(padx=5, pady=10) # Passphrase Settings

                self.does_phrase_start_capitals = tk.StringVar()
                self.passphraseCapital = tk.Checkbutton(passphraseSettingsFrame, text='Each word starts with a capital letter', variable=self.does_phrase_start_capitals, offvalue=False, onvalue=True) # Each word starts with a capital letter
                self.passphraseCapital.pack(padx=5, pady=5)
                self.passphraseCapital.deselect()

                self.phrase_allcaps = tk.StringVar()
                self.passphraseCapital = tk.Checkbutton(passphraseSettingsFrame, text='Words are in all caps', variable=self.phrase_allcaps, offvalue=False, onvalue=True) # Every word is in caps
                self.passphraseCapital.pack(padx=5, pady=5)
                self.passphraseCapital.deselect()
                

                self.passphraseLengthLabel = tk.Label(passphraseSettingsFrame, text='Amount of words (max 50) (0 defaults to a random amount)').pack(padx=5, pady=5) # Amount of words (max 50)

                self.passphraseLength = tk.Entry(passphraseSettingsFrame)
                self.passphraseLength.pack(padx=5, pady=5)

                passphraseSettingsFrame.pack(padx=10, pady=10, expand=True, fill='both', side='left')
                # End of Passphrase Settings Frame

                # Start of Password Settings Frame
                passwordSettingsFrame = tk.Frame(settingsFrame)
                self.passwordLabel = tk.Label(passwordSettingsFrame, text='Password Settings', font=('Ariel', 18)).pack(padx=5, pady=10) # Password Settings

                self.does_pass_have_symbols = tk.StringVar()
                self.passwordSymbols = tk.Checkbutton(passwordSettingsFrame, text='Symbols', variable=self.does_pass_have_symbols, offvalue=False, onvalue=True) # Symbols
                self.passwordSymbols.pack(padx=5, pady=5)
                self.passwordSymbols.select()

                self.does_pass_have_capitals = tk.StringVar()
                self.passwordCapital = tk.Checkbutton(passwordSettingsFrame, text='Random capital letters', variable=self.does_pass_have_capitals, offvalue=False, onvalue=True) # Random capital letters
                self.passwordCapital.pack(padx=5, pady=5)
                self.passwordCapital.select()

                self.passwordLengthLabel = tk.Label(passwordSettingsFrame, text='Length of password (max 250) (0 defaults to a random length)').pack(padx=5, pady=5) # Length of password (max 250)

                self.passwordLength = tk.Entry(passwordSettingsFrame)
                self.passwordLength.pack(padx=5, pady=5)


                passwordSettingsFrame.pack(padx=10, pady=10, expand=True, fill='both', side='left')
                # End of Password Settings Frame

                settingsFrame.pack(padx=10, pady=10)
                # End of Settings Frame

                def deleteOutput(): # Wipes the output text box cleans if theres any data in it
                        if len(self.output.get(index1=1.0)) > 0:
                                return self.output.delete(index1=1.0, index2='end')

                def getpassclick(): # Inserts generated password to output

                        deleteOutput()
                        getpasswordLength = self.passwordLength.get()
                        getpasswordSymbol = True if self.does_pass_have_symbols.get() == '1' else False
                        getpasswordCapital = True if self.does_pass_have_capitals.get() == '1' else False

                        if not getpasswordLength.isdigit() and getpasswordLength != '':
                                return self.output.insert(1.0, f'Error: Password length option has an invalid input -> {getpasswordLength}')
                        elif getpasswordLength == '':
                                getpasswordLength = 0

                        return self.output.insert(1.0, PasswordGenerator.password(symbols=getpasswordSymbol, length=getpasswordLength, capital=getpasswordCapital).get_pass())

                def getphraseclick(): # Inserts generated passphrase to output !Lags program for a few seconds when the button is pressed (I don't know why)!

                        deleteOutput()
                        getphraseLength = self.passphraseLength.get()
                        getpassphraseCapital = True if self.does_phrase_start_capitals.get() == '1' else False
                        getpassphraseAllcaps = True if self.phrase_allcaps.get() == '1' else False

                        if getphraseLength.isdigit() == False and getphraseLength != '':
                                return self.output.insert(1.0, f'Error: Passphrase length option has an invalid input -> {getphraseLength}')
                        elif getphraseLength == '':
                                getphraseLength = 0
                        
                        return self.output.insert(1.0, PasswordGenerator.passphrase(getphraseLength, getpassphraseCapital, getpassphraseAllcaps ).get_phrase())
                
                lagWarning = tk.Label(master, text='Just a heads up! The passphrase button may take a couple seconds to load depending on internet speed.') # Quick warning label that will be removed once the lag issue is resolved
                lagWarning.pack()

                # Start of Button Frame
                generateButtonsFrame = tk.Frame(master)
                self.makePassword = tk.Button(generateButtonsFrame, text='Generate Password', font=('Ariel', 18), command=threading.Thread(target=getpassclick).start).place(relx=0.7, rely=0.5, anchor='center')
                self.makePassphrase = tk.Button(generateButtonsFrame, text='Generate Passphrase', font=('Ariel', 18), command=threading.Thread(target=getphraseclick).start).place(relx=0.3, rely=0.5, anchor='center')

                generateButtonsFrame.pack(padx=10, pady=10, expand=True, fill='both')
                # End of Button Frame

                # Start of Output Frame
                outputFrame = tk.Frame(master)
                self.outputLabel = tk.Label(outputFrame, text='Your new secret:').pack(padx=5, pady=5) # Your new secret:
                self.output = tk.Text(outputFrame, height=5)
                self.output.pack(padx=5, pady=5)

                outputFrame.pack(padx=10, pady=10, expand=True, fill='both')
                # End of Output Frame
                
                self.stringvar = tk.StringVar() # String variable for self.ctcbLabel
                
                def copytoclipboard():
                        getText = self.output.get(index1=1.0, index2='end')

                        if len(getText) == 1 or getText.startswith('Error:'):
                                return self.stringvar.set('Nothing to copy')

                        pc.copy(getText)
                        return self.stringvar.set('Secret copied!')
                
                self.ctcbLabel = tk.Label(master, textvariable=self.stringvar, font=('ariel', 9)) # Secret copied! or Nothing to copy
                self.ctcbLabel.place(relx=0.5, rely=0.88, anchor='center')
                self.copytoclipboardButton = tk.Button(master, text='Copy to Clipboard', font=('ariel', 14), command=copytoclipboard)
                self.copytoclipboardButton.place(relx=0.5, rely=0.94, anchor='center')

master = mainGUI(root)
root.mainloop()
