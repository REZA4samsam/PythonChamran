w = 19
h = 9

print("        ┌", end="")

for i in range(w - 2):
    print("─", end="")

print("┐")

for i in range(h - 2):
    print("        │" + " " * (w - 2) + "   │")

print("        └", end="")

for i in range(w - 2):
    print("─", end="")

print("┘")
