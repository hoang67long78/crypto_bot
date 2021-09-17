import logging

from connectors.binance import BinanceClient
from connectors.bitmex import BitmexClient

from interface.root_component import Root


# Create and configure the logger object

logger = logging.getLogger()

logger.setLevel(logging.DEBUG)  # Overall minimum logging level

stream_handler = logging.StreamHandler()  # Configure the logging messages displayed in the Terminal
formatter = logging.Formatter('%(asctime)s %(levelname)s :: %(message)s')
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)  # Minimum logging level for the StreamHandler

file_handler = logging.FileHandler('info.log')  # Configure the logging messages written to a file
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)  # Minimum logging level for the FileHandler

logger.addHandler(stream_handler)
logger.addHandler(file_handler)


if __name__ == '__main__':  # Execute the following code only when executing main.py (not when importing it)

    binance = BinanceClient("2c18b137231d7bfe964f0e5c5a1dc7180ca0b9be7aa98ae6b87748d71eb93c11",
                            "b49c9881385af9804da52f338d8a45fc3727c739fca8bb8d443aa497d1739af5",
                            testnet=True, futures=True)
    bitmex = BitmexClient("kDO56iaxAtMP7k8m56LBVZTJ", "Nb8LnoFARbb73c8Z_87YI6ousnl3aYpWMREFa24qR1s8Eq-a", testnet=True)

    root = Root(binance, bitmex)
    root.mainloop()
