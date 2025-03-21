#radar gun 
prompt = "Enter speeds here "
radar = []
threshold = 35

while True:
    speed = input(prompt)
    radar.append(speed)
    print(f"entered {radar} so far")
    if speed == "quit":
        radar.remove("quit")
        print(f"congrats on your work, now make sure all speeds above 35 are delt with {radar}")

