words = ["PoGo","Spange","Lie-Fi"]
definitions = ["Slang for Pokemon Go","To collect spare change, either from couches, passerbys on the street or any numerous other ways and means","When your phone or tablet indicates that you are connected to a wireless network, however you are still unable to load webpages or use any internet services with your device"]

cooldictionary = dict()

for i in range(len(words)):
    cooldictionary[words[i]] = definitions[i]

for word,definition in cooldictionary.items():
    print(str(word)+':',definition,'\n')
