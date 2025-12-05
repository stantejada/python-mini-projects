from src.ui import FlashCardUI
from src.config import *
from src.data_handler import load_data
from src.logic import FlashManager

data = load_data()
manager = FlashManager(cards=data)


if __name__ == "__main__":
    window = FlashCardUI()
    window.mainloop()