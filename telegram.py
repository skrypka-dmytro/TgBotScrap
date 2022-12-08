import os

from bs4 import BeautifulSoup
import requests

import random


TOKEN = os.environ.get("TOKEN")
URL = "https://paper-trader.frwd.one"


def send_message(message):
    from_data = {
        "pair": message.text,
        "timeframe": random.choice(["5m", "15m", "1h", "4h", "1d", "1w", "1M"]),
        "candles": random.randint(0, 1000),
        "ma": random.randint(0, 100),
        "tp": random.randint(0, 100),
        "sl": random.randint(0, 100),
    }
    response = requests.post(URL, data=from_data)
    soup = BeautifulSoup(response.text, "html.parser")
    image = soup.find("img")["src"]
    return image[1:]
