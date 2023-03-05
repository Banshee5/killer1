d = dict()
while True:
    place = input()
    if place == "off":
        print(d)
        break
    else:
        place = int(place)
        musician = input()
        track = input()
        kort = (place, musician)
        d[kort] = track