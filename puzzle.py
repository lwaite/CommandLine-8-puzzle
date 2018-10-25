import random

state = []
new_state = []
win_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]

def display_board(state):
    print("-------------")
    print("| %i | %i | %i |" % (state[0], state[1], state[2]))
    print("-------------")
    print("| %i | %i | %i |" % (state[3], state[4], state[5]))
    print("-------------")
    print("| %i | %i | %i |" % (state[6], state[7], state[8]))
    print("-------------")

def move(state, direction):
    new_state = state
    index = new_state.index(0)
    if direction == 'u' and index not in [0, 1, 2]:
        temp = new_state[index - 3]
        new_state[index - 3] = new_state[index]
        new_state[index] = temp
        return new_state
    
    elif direction == 'd' and index not in [6, 7, 8]:
        temp = new_state[index + 3]
        new_state[index + 3] = new_state[index]
        new_state[index] = temp
        return new_state
    
    elif direction == 'l' and index not in [0, 3, 6]:
        temp = new_state[index - 1]
        new_state[index - 1] = new_state[index]
        new_state[index] = temp
        return new_state
    
    elif direction == 'r' and index not in [2, 5, 8]:
        temp = new_state[index + 1]
        new_state[index + 1] = new_state[index]
        new_state[index] = temp
        return new_state

    else:
        print("Impossible movement")
        return new_state

def main():
    state = random.sample(range(9), 9)
    new_state = state
    display_board(state)
    while new_state != win_state:
        display_board(move(new_state, input()))

if __name__ == '__main__':
        main()
