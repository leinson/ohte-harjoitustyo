from logging import info
from tkinter import Tk, ttk, constants


class InfoView:
    """Luokka, joka kuvastaa Ohjeet näkymää graafisessa käyttöliittymässä.
    """

    def __init__(self, root, handle_start):
        """Luokan konstruktori, joka luo näkymän.

        Args:
            root: GUI juuri.
            handle_start: Reitti millä palataan start näkymään
        """
        self._root = root
        self._handle_start = handle_start
        self._frame = None
        self.bg_color = '#E4D6FF'
        self._initialize()

    def pack(self):
        """Pakkaa näkymän.
        """
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Tuhoaa näkymän.
        """
        self._frame.destroy()
    
    def _info_text(self):
        info_text = """
        Sovelluksen käyttöohje:

        - Syötä nimesi sekä kissasi nimen alkunäkymään.

        - Painamalla Aloita, siirryt päänäkymään, missä näet kissasi.

        - Nimet tallentuvat vain sovelluksen kyseiselle käyttökerralle.


        - Päänäkymässä näet kissasi tarpeet oikeasta yläkulmasta. 

        - Näet myös kissan ulkomuodosta, mitä hän mahdollisesti tarvitsee.
        
        - Painamalla nappeja, saat korotettua kissan tarpeita.
        
        - Kissa on tyytyväisimmillään, kun prosentit ovat lähellä sataa.
        
        - Prosentit tippuvat ajan myötä, jonka vuoksi on tärkeää muistaa pitää huolta kissasta.
        
        - Jos prosentit tippuvat alle nollan, kissa karkaa etkä voi jatkaa kissan huolenpitoa.
        

        - Voit halutessasi aloittaa uuden pelin siirtymällä takaisin aloitusnäkymään.
        
        - Poistut sovelluksesta painamalla raksia, tai aloitusnäkymän Poistu-painikkeella.
        """
        return info_text

    def _initialize(self):
        """Alustaa luokan ja näkymän.
        """
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text=f"{self._info_text()}", font=("Quicksand",12), background=self.bg_color)

        button = ttk.Button(
            master=self._frame,
            text="Takaisin",
            command=self._handle_start
        )

        label.grid(row=0, column=0, sticky=constants.W, padx=30, pady=5)
        button.grid(row=1, column=0, sticky=constants.W, padx=30, pady=20, ipady=5)
