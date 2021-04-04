# Stalk_viewer

`Stalk_viewer` est un outil permettant de connaître le nombre de personnes connectées sur un stream (Mods + viewers classiques)

Afin d'affecter le programme à un streamer en particulier, changer le champs suivant dans le fichier `main.py : 

```python
# Pseudo du streamer :
USERNAME = 'TWITCH_USERNAME'
```

De base, le programme s'actualise toutes les 2 minutes, vous pouvez modifier ce temps en changeant le code ci dessous dans le fichier `main.py`:

```python
# Période d'actualisation :
TEMPO = 120
```

By [B4tiste](github.com/B4tiste "Go to B4tiste GitHub Page"), *a French guy who doesn't know how to code anything else beside `Hello World`, and who's pretty garbage in English, but who wanna have fun*