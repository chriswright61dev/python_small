# hanoi recursion
def move(from_position, to_position):
    print("Move Disk from {} to {} ".format(from_position, to_position))

def hanoi(number_of_disks, from_position, intermediate_position, to_position):
    if number_of_disks == 0:
        pass
    else:
        hanoi(number_of_disks-1,from_position, to_position, intermediate_position)
        move(from_position, to_position)
        hanoi(number_of_disks-1,intermediate_position , from_position, to_position )

hanoi(5,"a","b","c")