import stalk_viewer
import time

# Pseudo du streamer :
USERNAME = 'USERNAME'

# Période d'actualisation :
TEMPO = 60

if __name__ == "__main__":
    while True:
        stalk_viewer.stalk(USERNAME)
        time.sleep(TEMPO)
