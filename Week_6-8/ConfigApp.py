import json
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

class ConfigApp:
    """
    ConfigApp class provides a simple configuration application using Tkinter for GUI.
    It allows loading and saving configuration settings in JSON format.

    Attributes:
    - app_screen (tk.Tk): The main Tkinter application window.
    - log_file (tk.StringVar): Variable to store the log file path.
    - max_threads (ttk.Combobox): Dropdown to choose the maximum number of threads (1, 2, or 4).
    - event_types (dict): Dictionary of Tkinter BooleanVars for different event types.
    - supported_file_types (dict): Dictionary of Tkinter BooleanVars for supported file types.
    - debug_mode (tk.BooleanVar): Variable to store whether debug mode is on.
    - server_port (tk.StringVar): Variable to store the server port.

    Methods:
    - __init__(): Initializes the ConfigApp class and sets up the Tkinter application window.
    - setup_interface(): Sets up the user interface by calling grid setup and menu setup methods.
    - setup_grid(): Sets up the grid layout for the user interface.
    - setup_menu(): Sets up the menu bar with options for loading, saving, and quitting.
    - load_settings(): Loads configuration settings from a JSON file and updates the UI.
    - save_settings(): Saves configuration settings to a JSON file based on user inputs.
    - quit(): Quits the application with confirmation from the user.
    """

    def __init__(self):
        """
        Initialize the ConfigApp class.

        Sets up the Tkinter application window, variables, and calls
        the method to set up the user interface.
        """
        self.app_screen = tk.Tk()
        self.app_screen.geometry("500x400")

        # Variables to store configuration settings
        self.log_file = tk.StringVar()
        self.max_threads = ttk.Combobox(self.app_screen, state="readonly", values=[1, 2, 4])

        # Additional variables for new features
        self.event_types = {
            "Application": tk.BooleanVar(),
            "Security": tk.BooleanVar(),
            "Error": tk.BooleanVar(),
            "Input/Output": tk.BooleanVar(),
        }
        self.supported_file_types = {
            ".doc": tk.BooleanVar(),
            ".docx": tk.BooleanVar(),
            ".ppt": tk.BooleanVar(),
            ".pptx": tk.BooleanVar(),
            ".xls": tk.BooleanVar(),
            ".xlsx": tk.BooleanVar(),
            ".rtf": tk.BooleanVar(),
            ".pdf": tk.BooleanVar(),
            ".txt": tk.BooleanVar(),
            ".jpg": tk.BooleanVar(),
            ".png": tk.BooleanVar(),
            ".gif": tk.BooleanVar(),
            ".xml": tk.BooleanVar(),
            ".html": tk.BooleanVar(),
            ".zip": tk.BooleanVar(),
            ".mp4": tk.BooleanVar(),
            ".mov": tk.BooleanVar(),
        }
        self.debug_mode = tk.BooleanVar()
        self.server_port = tk.StringVar()

        # Set up the user interface
        self.setup_interface()

    def setup_interface(self):
        """
        Set up the user interface by calling grid and menu setup methods,
        then start the Tkinter main loop.
        """
        self.setup_grid()
        self.setup_menu()
        self.app_screen.mainloop()

    def setup_grid(self):
        """
        Set up the grid layout for the user interface.
        Include code to arrange widgets in a grid layout.
        """
        tk.Label(self.app_screen, text="Log File:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)
        tk.Entry(self.app_screen, textvariable=self.log_file).grid(row=0, column=1, padx=5, pady=5, columnspan=2, sticky=tk.W)

        tk.Label(self.app_screen, text="Max Threads:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)
        ttk.Combobox(self.app_screen, textvariable=self.max_threads, state="readonly", values=[1, 2, 4]).grid(row=1, column=1, padx=5, pady=5, columnspan=2, sticky=tk.W)

        tk.Label(self.app_screen, text="Event Types to Log:").grid(row=2, column=0, padx=5, pady=5, sticky=tk.E)
        for i, event_type in enumerate(self.event_types):
            tk.Checkbutton(self.app_screen, text=event_type, variable=self.event_types[event_type]).grid(row=2 + i, column=1, padx=5, pady=2, sticky=tk.W)

        tk.Label(self.app_screen, text="Supported File Types:").grid(row=2, column=2, padx=5, pady=5, sticky=tk.E)
        for i, file_type in enumerate(self.supported_file_types):
            tk.Checkbutton(self.app_screen, text=file_type, variable=self.supported_file_types[file_type]).grid(row=2 + i, column=3, padx=5, pady=2, sticky=tk.W)

        tk.Checkbutton(self.app_screen, text="Debug Mode", variable=self.debug_mode).grid(row=2, column=4, padx=5, pady=5, sticky=tk.W)

        tk.Label(self.app_screen, text="Server Port:").grid(row=3, column=4, padx=5, pady=5, sticky=tk.E)
        tk.Entry(self.app_screen, textvariable=self.server_port).grid(row=3, column=5, padx=5, pady=5, sticky=tk.W)

    def setup_menu(self):
        """
        Set up the menu bar with options for loading, saving, and quitting.

        Uses Tkinter Menus to create a simple menu structure.
        """
        top_menu = tk.Menu(self.app_screen)
        self.app_screen.config(menu=top_menu)

        file_menu = tk.Menu(top_menu)
        file_menu.add_command(label='Load Settings from JSON', command=self.load_settings)
        file_menu.add_command(label='Save Settings to JSON', command=self.save_settings)
        file_menu.add_command(label='Quit', command=self.quit)
        top_menu.add_cascade(label='Config Settings', menu=file_menu)

    def load_settings(self):
        """
        Load configuration settings from a JSON file.

        Opens a file dialog to select a JSON file and updates UI elements
        with the loaded settings.
        """
        file_path = filedialog.askopenfilename()
        if file_path:
            try:
                with open(file_path) as file:
                    settings = json.load(file)

                    # Update UI elements with loaded settings
                    self.log_file.set(settings.get("Logfile", ""))
                    self.max_threads.set(settings.get("Maxthread", ""))
                    for event_type in self.event_types:
                        self.event_types[event_type].set(settings.get(event_type, False))
                    for file_type in self.supported_file_types:
                        self.supported_file_types[file_type].set(settings.get(file_type, False))
                    self.debug_mode.set(settings.get("DebugMode", False))
                    self.server_port.set(settings.get("ServerPort", ""))

            except Exception as e:
                messagebox.showerror('Error', f'Error loading settings: {str(e)}')

    def save_settings(self):
        """
        Save configuration settings to a JSON file.

        Opens a file dialog to specify a location for saving the settings
        in JSON format.
        """
        file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON Files", "*.json")])
        if file_path:
            settings = {
                "Logfile": self.log_file.get(),
                "Maxthread": self.max_threads.get(),
                **{event_type: self.event_types[event_type].get() for event_type in self.event_types},
                **{file_type: self.supported_file_types[file_type].get() for file_type in self.supported_file_types},
                "DebugMode": self.debug_mode.get(),
                "ServerPort": self.server_port.get(),
            }
            try:
                with open(file_path, 'w') as file:
                    json.dump(settings, file, indent=4)
                messagebox.showinfo('Success', 'Settings saved successfully!')
            except Exception as e:
                messagebox.showerror('Error', f'Error saving settings: {str(e)}')

    def quit(self):
        """
        Quit the application.

        Asks for confirmation before destroying the main Tkinter window.
        """
        if messagebox.askyesno('Verify quit', 'Are you sure you want to quit?'):
            self.app_screen.destroy()

if __name__ == '__main__':
    ConfigApp()

