import stalk_viewer
import time

# Pseudo du streamer :
USERNAME = 'b4tiste_bh'

# Période d'actualisation :
TEMPO = 60

if __name__ == "__main__":
    while True:
        stalk_viewer.stalk(USERNAME)
        time.sleep(TEMPO)
