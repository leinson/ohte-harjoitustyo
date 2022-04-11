from tkinter import ttk, constants

class StartView:
    def __init__(self, root, handle_cat, handle_info, exit_appl):
        self._root = root
        self._handle_cat = handle_cat
        self._handle_info = handle_info
        self._exit_appl = exit_appl
        self._frame = None
        self._entry_user = None
        self._entry_cat= None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        heading_label = ttk.Label(master=self._frame, text="Tämä on MiukuM@uku, virtuaalinen kissalemmikkisovellus.\nSyötä tiedot alle:")
        user_label= ttk.Label(master=self._frame, text="Käyttäjätunnus:")
        self._entry_user = ttk.Entry(master=self._frame)

        cat_label= ttk.Label(master=self._frame, text="Kissan nimi:")
        self._entry_cat = ttk.Entry(master=self._frame)

        start_button = ttk.Button(
            master=self._frame,
            text="Aloita",
            command=self._handle_cat 
            ) #käytä lambdaa jos haluat parametreja mukaan commandiin
        info_button = ttk.Button(
            master=self._frame,
            text="Ohjeet",
            command=self._handle_info
            )
        exit_button = ttk.Button(
            master=self._frame,
            text="Poistu",
            command=self._exit_appl
        )

        heading_label.grid(row=0, column=0, columnspan=2, sticky=constants.W, padx=5, pady=15) #columnspan levii 2 sarakkeelle
        
        user_label.grid(row=1, column=0, padx=5, pady=5, sticky=constants.W)
        self._entry_user.grid(row=1, column=1,sticky=(constants.W,constants.E), padx=5, pady=5)
        cat_label.grid(row=2, column=0, sticky=constants.W, padx=5, pady=5)
        self._entry_cat.grid(row=2, column=1, sticky=(constants.W,constants.E), padx=5, pady=5)
        
        info_button.grid(row=3, column=0, sticky=constants.W, padx=5, pady=15)
        start_button.grid(row=3, column=1, sticky=(constants.W,constants.E), padx=5, pady=5)
        exit_button.grid(row=4, column=0, sticky=constants.W, padx=5, pady=5)

        self._root.grid_columnconfigure(1, weight=1, minsize=400)

    


    
    #     start click tiedon tallennus??
    #     entry_value_user = entry_user.get()
    #     entry_value_cat = entry_cat.get()
    #     print(f"Testi: {entry_value_user}, {entry_value_cat}")

    # Nämä varmaan ui luokkaan, niinkuin handle_cat
    def _handle_info_button_click(self):
        pass # move to info view
    def _handle_exit_button_click(self):
        pass # exit program