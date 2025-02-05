def cmap(index):
    if not ( -1 <= index <= 1):
        raise ValueError("index must be in the range [-1,1]")

    return [int(1-index * 255),int(1+index * 255), 0]

if __name__ == "__main__":
    from turtle import Turtle, Screen
    import turtle
    t = Turtle()
    screen = Screen()

    screen.colormode(255)

    STEP = 0.01
    val = -1

    while(val <= 1):
        t.color(cmap(val))
        t.forward(1)
        val += STEP

    turtle.done()