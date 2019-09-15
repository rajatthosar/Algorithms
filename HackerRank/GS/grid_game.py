grid = [[0, 1, 0, 0],
        [0, 0, 0, 0]]

k = 2

rules = ["dead", "alive", "dead", "dead", "dead", "alive", "dead", "dead", "dead"]


def get_alive_neighbors(grid):
    status_grid = []
    for row_idx in range(len(grid)):
        row_status = []
        for col_idx in range(len(grid[0])):
            count = 0
            if (row_idx - 1 in range(0, len(grid))) and (
                    col_idx - 1 in range(0, len(grid[0]))) and grid[row_idx - 1][col_idx - 1] == 1:
                count += 1
            if (row_idx - 1 in range(0, len(grid))) and (col_idx in range(0, len(grid[0]))) and (
                    grid[row_idx - 1][col_idx] == 1):
                count += 1
            if (row_idx - 1 in range(0, len(grid))) and (
                    col_idx + 1 in range(0, len(grid[0]))) and (grid[row_idx - 1][col_idx + 1] == 1):
                count += 1
            if (row_idx in range(0, len(grid))) and (col_idx - 1 in range(0, len(grid[0]))) and (
                    grid[row_idx][col_idx - 1] == 1):
                count += 1
            if (row_idx in range(0, len(grid))) and (col_idx + 1 in range(0, len(grid[0]))) and (
                    grid[row_idx][col_idx + 1] == 1):
                count += 1
            if (row_idx + 1 in range(0, len(grid))) and (
                    col_idx - 1 in range(0, len(grid[0]))) and (grid[row_idx + 1][col_idx - 1] == 1):
                count += 1
            if (row_idx + 1 in range(0, len(grid))) and (col_idx in range(0, len(grid[0]))) and (
                    grid[row_idx + 1][col_idx] == 1):
                count += 1
            if (row_idx + 1 in range(0, len(grid))) and (
                    col_idx + 1 in range(0, len(grid[0]))) and (grid[row_idx + 1][col_idx + 1] == 1):
                count += 1
            row_status.append(count)
        status_grid.append(row_status)
        row_status = []
    return status_grid


def get_rules(rules):
    count = 0
    active_rules = []
    for rule in rules:
        if rule.lower() == "alive":
            active_rules.append(count)
        count += 1

    return active_rules


def grid_game(grid, k, rules):
    for iteration in range(k):
        status_grid = get_alive_neighbors(grid)
        active_rules = get_rules(rules)

        for row_idx in range(len(grid)):
            for col_idx in range(len(grid[0])):
                if status_grid[row_idx][col_idx] in active_rules:
                    row = grid[row_idx]
                    row[col_idx] = 1
                    grid[row_idx] = row
                else:
                    row = grid[row_idx]
                    row[col_idx] = 0
                    grid[row_idx] = row
    return grid


print(grid_game(grid, k, rules))
