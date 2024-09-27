__all__ = ["is_attacking"]

def is_attacking(queens):
    for i in range(len(queens)):
        for j in range(i+1, len(queens)):
            if queens[i][0] == queens[j][0] or queens[i][1] == queens[j][1] or abs(queens[i][0] - queens[j][0]) == abs(queens[i][1] - queens[j][1]):
                return False
    return True

queens_positions = [(2, 1), (4, 2), (6, 3), (8, 4), (1, 5), (3, 6), (5, 7), (7, 8)]
result = is_attacking(queens_positions)
print(result)