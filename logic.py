""" 
Un día, un explorador comenzó a seguir algunos sonidos extraños, luego llegó a un lago donde encontró la fuente: 3 animalitos haciendo sonidos parecidos a una canción. Pasó poco tiempo y el explorador pudo diferenciar qué animal producía cada sonido.

Sonidos
Rana: brr, birip, brrah, croac
Libélula: fiu, plop, pep
Grillo: cric-cric, trri-trri, bri-bri

Después de un tiempo descubrió que estaban "cantando" juntos. Siempre que la rana comenzaba con brr, la libélula respondía a su sonido frotando su cola con una rama produciendo un sonido como fiu, después de la libélula, el grillo continuaba con cric-cric pero, cada vez que la rana sonaba como brrah o croac todos los animales se silenciaron. por un tiempo, y luego continuaron de nuevo. Antes de que el cielo se oscureciera, el explorador pudo escribir 3 "canciones" que todos hicieron juntos y se le ocurrieron estas notas.

Canciones
brr, fiu, cric-cric, brrah
pep, birip, trri-trri, croac
bri-bri, plop, cric-cric, brrah

Escriba un programa que le permita recibir un sonido dado de la lista de sonidos que hace cada animal y devuelva los sonidos restantes de cualquiera de las 3 canciones que escribió el explorador, por ejemplo:

Cuando se le da brr debe reproducir fiu, cric-cric, brrah de acuerdo con la primera canción.
Cuando se le da birip, debe reproducir trri-trri, croac según la segunda canción.
Cuando se le da plop debe reproducir cric-cric, brrah de acuerdo con la tercera canción.
Cuando se le da croac o brrah, no debería reproducir nada de acuerdo con todas las canciones.

"""

def play_song(firstSound):
    songIndex = -1
    songs = [
        ["brr", "fiu", "cric-cric", "brrah"],
        ["pep", "birip", "trri-trri", "croac"],
        ["bri-bri", "plop", "cric-cric", "brrah"],
    ]
    
    for i in range(len(songs)):
        if firstSound in songs[i][0]:
            songIndex = i
    if (songIndex == -1):
        return "nothing"
    
    return songs[songIndex]

firstSound = "brr"
song = play_song(firstSound)
print(f"When the first sound is:  {firstSound}, play {', '.join(song)}")

firstSound = "birip"
song = play_song(firstSound)
print(f"When the first sound is:  {firstSound}, play {', '.join(song)}")

firstSound = "plop"
song = play_song(firstSound)
print(f"When the first sound is:  {firstSound}, play {', '.join(song)}")

firstSound = "bri-bri"
song = play_song(firstSound)
print(f"When the first sound is:  {firstSound}, play {', '.join(song)}")



