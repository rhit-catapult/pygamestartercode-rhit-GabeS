import play

background = play.new_image("background.png")

airplane = play.new_image("airplane.png", size = 20, x = -300, y = 200)
rocks = []
scissors_list = []
for k in range(3):
    scissors = play.new_image("scissors.png", size = 20)
    scissors.go_to(play.random_position())
    scissors.y += 300
    scissors_list.append(scissors)
for k in range(10):
    rock = play.new_image("rocks.png", size = 20)
    rock.go_to(play.random_position())
    rocks.append(rock)



@play.repeat_forever
def repeat_loop():
    airplane.point_towards(play.mouse)
    airplane.move(5)
    for rock in rocks:
        if airplane.is_touching(rock):
            rocks.remove(rock)
            rock.remove()
    for scissors in scissors_list:
        scissors.point_towards(airplane)
        scissors.move(1)
        if scissors.is_touching(airplane):
            airplane.go_to(-300, 200)



play.start_program()
