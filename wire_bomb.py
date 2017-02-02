"""flow of wire cutting to diffuse ordinance"""


def bombo():
    print("""C'mon Riggs! We've got to diffuse this thing!\nThere's a bunch of wires:
           White, Black, Red, Green, Purple, and Orange!""")
    cut_flow()


def win():
    print("Phew, I'm getting to old fo this!")

def dead():
    print("Kablooey!")
    exit()
    return None


def next_wire(next_wire):
    wire_to_cut = int(input("How many wires are left? "))
    #wire_to_cut -= 1
    while wire_to_cut > 0:
        next_wire = input("Alright man, now which? ")
        wire_to_cut -= 1
        next_wire(next_wire)
    if wire_to_cut == 0:
        win()


def white(next_wire):
    next_wire(next_wire)
    if next_wire == "White":
        dead()
    elif next_wire == "Black":
        dead()
    elif next_wire == "Red":
        red(next_wire)
    elif next_wire == "Green":
        green(next_wire)
    elif next_wire == "Purple":
        purple(next_wire)
    elif next_wire == "Orange":
        orange(next_wire)
    else:
        dead()


def black(next_wire):
    next_wire(next_wire)
    if next_wire == "White":
        white(next_wire)
    elif next_wire == "Black":
        black(next_wire)
    elif next_wire == "Red":
        red(next_wire)
    elif next_wire == "Orange":
        dead()
    elif next_wire == "Green":
        dead()
    elif next_wire == "Purple":
        purple(next_wire)
    else:
        dead()


def red(next_wire):
    next_wire(next_wire)
    if next_wire == "Green":
        green(next_wire)
    elif next_wire == "Red":
        red(next_wire)
    else:
        dead()


def green(next_wire):
    next_wire(next_wire)
    if next_wire == "White":
        white(next_wire)
    elif next_wire == "Orange":
        orange(next_wire)
    elif next_wire == "Green":
        green(next_wire)
    else:
        dead()


def purple(next_wire):
    next_wire(next_wire)
    if next_wire == "Red":
        red(next_wire)
    elif next_wire == "White":
        white(next_wire)
    else:
        dead()


def orange(next_wire):
    next_wire(next_wire)
    if next_wire == "Red":
        red(next_wire)
    elif next_wire == "Black":
        black(next_wire)
    else:
        dead()


def cut_flow():
    #wires_to_cut = int(input("How many wires are there? "))
    wire_cut = input("Which wire do you want to cut? ")
    #while 2 == 2:
    if wire_cut == "White":
        white(next_wire)
    elif wire_cut == "Black":
        black(next_wire)
    elif wire_cut == "Red":
        red(next_wire)
    elif wire_cut == "Green":
        green(next_wire)
    elif wire_cut == "Purple":
        purple(next_wire)
    elif wire_cut == "Orange":
        orange(next_wire)
    else:
        dead()



bombo()
