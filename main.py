import stalk_viewer
import time

# Pseudo du streamer :
USERNAME = 'b4tiste_sw'

# Période d'actualisation :
TEMPO = 120

if __name__ == "__main__":
    while True:
        stalk_viewer.stalk(USERNAME)
        time.sleep(TEMPO)
