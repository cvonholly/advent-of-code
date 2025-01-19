with open('input.txt', 'r') as file:
    data = file.read()
    # Split the data into two lists
    left_list = []
    right_list = []
    for line in data.strip().split('\n'):
        left, right = map(int, line.split())
        left_list.append(left)
        right_list.append(right)

    # Sort both lists
    left_list.sort()
    right_list.sort()

    # Calculate the total distance
    total_distance = sum(abs(l - r) for l, r in zip(left_list, right_list))

    print(total_distance)

with open('input.txt', 'r') as file:
    data = file.read()