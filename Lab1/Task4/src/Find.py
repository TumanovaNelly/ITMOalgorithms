def find(lst: list, value) -> list:
    indexes = []
    for i in range(len(lst)):
        if lst[i] == value:
            indexes.append(i + 1)
    
    if not indexes:
        indexes.append(-1)
    return indexes