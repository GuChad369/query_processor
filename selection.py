from parseRelation import isStringFloat


# selection operation
def selection(table: dict, condition: str) -> dict:
    # store the result
    res = []
    # parse condition
    parts = condition.split()
    column = parts[0]
    operator = parts[1]
    value = parts[2]

    # compare two column
    # check if value is the table's column
    if value in list(table.keys()):
        # get column
        column1 = table[column]
        column2 = table[value]
        # operate
        if operator == "=":
            for i in range(len(column1)):
                if column1[i] == column2[i]:
                    res.append(i)
        elif operator == "!=" or operator == "<>":
            for i in range(len(column1)):
                if column1[i] != column2[i]:
                    res.append(i)
        elif operator == ">":
            for i in range(len(column1)):
                if (
                    column1[i] != None
                    and column2[i] != None
                    and column1[i] > column2[i]
                ):
                    res.append(i)
        elif operator == "<":
            for i in range(len(column1)):
                if (
                    column1[i] != None
                    and column2[i] != None
                    and column1[i] < column2[i]
                ):
                    res.append(i)
        elif operator == ">=":
            for i in range(len(column1)):
                if (
                    column1[i] != None
                    and column2[i] != None
                    and column1[i] >= column2[i]
                ):
                    res.append(i)
        elif operator == "<=":
            for i in range(len(column1)):
                if (
                    column1[i] != None
                    and column2[i] != None
                    and column1[i] <= column2[i]
                ):
                    res.append(i)

    # simple operation
    # =, !=, >, <, >=, <=
    else:
        if isStringFloat(value):
            value = float(value)
        # get column
        column = table[column]

        # operate
        if operator == "=":
            for i in range(len(column)):
                if column[i] == value:
                    res.append(i)
        elif operator == "!=" or operator == "<>":
            for i in range(len(column)):
                if column[i] != value:
                    res.append(i)
        elif operator == ">":
            for i in range(len(column)):
                if column[i] != None and column[i] > value:
                    res.append(i)
        elif operator == "<":
            for i in range(len(column)):
                if column[i] != None and column[i] < value:
                    res.append(i)
        elif operator == ">=":
            for i in range(len(column)):
                if column[i] != None and column[i] >= value:
                    res.append(i)
        elif operator == "<=":
            for i in range(len(column)):
                if column[i] != None and column[i] <= value:
                    res.append(i)
    # get the needed column
    table = {key: [value[i] for i in res] for key, value in table.items()}
    return table
