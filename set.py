def set(method: str, table1: dict, table2: dict) -> dict:
    table = {}
    if method == "+":
        table = union(table1, table2)
    elif method == "^":
        table = intersection(table1, table2)
    elif method == "-":
        table = minus(table1, table2)

    return table


def intersection(table1: dict, table2: dict) -> dict:
    # make sure table1 is smaller
    if len(list(table1.keys())) > len(list(table2.keys())):
        table = table2
        table2 = table1
        table1 = table
    res = findSameRow(table1, table2)
    # get the needed column
    table = {key: [value[i] for i in res] for key, value in table1.items()}
    return table


def union(table1: dict, table2: dict) -> dict:
    table2 = minus(table2, table1)
    # Performing a union of the two tables
    table = {key: table1[key] + table2[key] for key in table1}
    return table


def minus(table1: dict, table2: dict) -> dict:
    sameRow = findSameRow(table1, table2)
    # Get the needed columns that are not in res
    table = {
        key: [value[i] for i in range(len(value)) if i not in sameRow]
        for key, value in table1.items()
    }

    return table


def findSameRow(table1: dict, table2: dict) -> list:
    column = len(list(table1.keys()))
    res = []
    # check first column
    key1 = list(table1.keys())[0]
    for i in range(len(table1[key1])):
        if table1[key1][i] == table2[key1][i]:
            res.append(i)

    # check other column
    for i in range(1, column):
        key = list(table1.keys())[i]
        error = []
        for item in res:
            if table1[key][item] != table2[key][item]:
                error.append(item)
        for item in error:
            if item in res:
                res.remove(item)
    return res
