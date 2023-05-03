def transform(legacy_data):
    """
    Your task is to change the data format of letters and their point values in the game.

    Currently, letters are stored in groups based on their score, in a one-to-many mapping.

    1 point: "A", "E", "I", "O", "U", "L", "N", "R", "S", "T",
    2 points: "D", "G",
    3 points: "B", "C", "M", "P",
    4 points: "F", "H", "V", "W", "Y",
    5 points: "K",
    8 points: "J", "X",
    10 points: "Q", "Z",
    This needs to be changed to store each individual letter with its score in a one-to-one mapping.

    "a" is worth 1 point.
    "b" is worth 3 points.
    "c" is worth 3 points.
    "d" is worth 2 points.
    etc.
    As part of this change, the team has also decided to change the letters to be lower-case rather than upper-case.
    """
    data = {}
    for item, list_values in legacy_data.items():
        for value in list_values:
            data[value.lower()] = item

    return data

if __name__ == "__main__":
    print(transform({
            1: ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],
            2: ["D", "G"],
            3: ["B", "C", "M", "P"],
            4: ["F", "H", "V", "W", "Y"],
            5: ["K"],
            8: ["J", "X"],
            10: ["Q", "Z"],
        }))