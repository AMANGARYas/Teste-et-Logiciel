def suit_arithm(sequence):
    if len(sequence) < 2:
        return True 
    common_difference = sequence[1] - sequence[0]

    for i in range(2, len(sequence)):
        if sequence[i] - sequence[i - 1] != common_difference:
            return False

    return True
