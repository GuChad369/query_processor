# projection operation
def projection(table: dict, condition: str) -> dict:
    # parse condition
    parts = [element.strip() for element in condition.split(",")]

    table = {key: table[key] for key in parts}

    return table
