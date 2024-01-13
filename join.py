from selection import selection


# cartesian product
def cartesianProduct(
    table1Name: str, table1: dict, table2Name: str, table2: dict
) -> dict:
    # create result dict
    cartesianTable = {}
    # get each table's clolumn number
    n1 = len(table1[list(table1.keys())[0]])
    n2 = len(table2[list(table2.keys())[0]])

    # create each cloumn
    for key, value in table1.items():
        cartesianTable[table1Name + "." + key] = []
        for i in range(n1):
            for j in range(n2):
                cartesianTable[table1Name + "." + key].append(value[i])

    for key, value in table2.items():
        cartesianTable[table2Name + "." + key] = []
        for i in range(n1):
            for j in range(n2):
                cartesianTable[table2Name + "." + key].append(value[j])

    return cartesianTable


# join
def join(
    table1Name: str,
    table1: dict,
    table2Name: str,
    table2: dict,
    method: str,
    condition: str,
) -> dict:
    # get the cartesianTable
    cartesianTable = cartesianProduct(table1Name, table1, table2Name, table2)
    # select
    if method == "join":
        table = selection(cartesianTable, condition)
    elif method == "ljoin":
        # get inner join reslut
        innerJoin = selection(cartesianTable, condition)
        table = leftJoin(table1Name, table1, table2Name, table2, innerJoin)
    elif method == "rjoin":
        # get inner join reslut
        innerJoin = selection(cartesianTable, condition)
        table = leftJoin(table2Name, table2, table1Name, table1, innerJoin)
    elif method == "fjoin":
        # get inner join reslut
        innerJoin = selection(cartesianTable, condition)
        # ljoin
        innerJoin = leftJoin(table1Name, table1, table2Name, table2, innerJoin)
        table = leftJoin(table2Name, table2, table1Name, table1, innerJoin)

    return table


def leftJoin(
    table1Name: str, table1: dict, table2Name: str, table2: dict, innerJoin: dict
) -> dict:
    # check the absence column
    differentNumber = 0
    for key in list(table1.keys()):
        # find the difference
        difference = [
            item
            for item in table1[key]
            if item not in innerJoin[table1Name + "." + key]
        ]
        differentNumber = len(difference)
        if differentNumber == 0:
            return innerJoin
        innerJoin[table1Name + "." + key].extend(difference)

    # add content to left table
    for key in list(table2.keys()):
        for i in range(differentNumber):
            innerJoin[table2Name + "." + key].append(None)

    return innerJoin
