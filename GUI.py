import tkinter as tk
import PasswordGenerator

root = tk.Tk()
version = '1.0'
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
                self.passphraseCapital = tk.Checkbutton(passphraseSettingsFrame, text='Each word starts with a capital letter', variable=self.does_phrase_start_capitals, offvalue='false', onvalue='true') # Each word starts with a capital letter
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
                self.passwordSymbols = tk.Checkbutton(passwordSettingsFrame, text='Symbols', variable=self.does_pass_have_symbols, offvalue='weak', onvalue='strong') # Symbols
                self.passwordSymbols.pack(padx=5, pady=5)
                self.passwordSymbols.select()

                self.does_pass_have_capitals = tk.StringVar()
                self.passwordCapital = tk.Checkbutton(passwordSettingsFrame, text='Random capital letters', variable=self.does_pass_have_capitals, offvalue='false', onvalue='true') # Random capital letters
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
                        getpassword = self.passwordLength.get()
                        if getpassword.isdigit() == False:
                                return self.output.insert(1.0, f'Error: Password length option has an invalid input -> {getpassword}')

                        return self.output.insert(1.0, PasswordGenerator.password(self.does_pass_have_symbols.get(), getpassword, self.does_pass_have_capitals.get()).get_pass())

                def getphraseclick(): # Inserts generated passphrase to output !Lags program for a few seconds when the button is pressed (I don't know why)!

                        deleteOutput()
                        getphrase = self.passphraseLength.get()
                        if getphrase.isdigit() == False:
                                return self.output.insert(1.0, f'Error: Passphrase length option has an invalid input -> {getphrase}')
                        
                        return self.output.insert(1.0, PasswordGenerator.passphrase(getphrase, self.does_phrase_start_capitals.get()).get_phrase())
                
                lagWarning = tk.Label(master, text='Just a heads up! The passphrase button may take a couple seconds to load.') # Quick warning label that will be removed once the lag issue is resolved
                lagWarning.pack()

                # Start of Button Frame
                generateButtonsFrame = tk.Frame(master)
                self.makePassword = tk.Button(generateButtonsFrame, text='Generate Password', font=('Ariel', 18), command=getpassclick).place(relx=0.7, rely=0.5, anchor='center')
                self.makePassphrase = tk.Button(generateButtonsFrame, text='Generate Passphrase', font=('Ariel', 18), command=getphraseclick).place(relx=0.3, rely=0.5, anchor='center')

                generateButtonsFrame.pack(padx=10, pady=10, expand=True, fill='both')
                # End of Button Frame

                # Start of Output Frame
                outputFrame = tk.Frame(master)
                self.outputLabel = tk.Label(outputFrame, text='Your new secret:').pack(padx=5, pady=5) # Your new secret:
                self.output = tk.Text(outputFrame, height=5)
                self.output.pack(padx=5, pady=5)

                outputFrame.pack(padx=10, pady=10, expand=True, fill='both')
                # End of Output Frame

master = mainGUI(root)
root.mainloop()