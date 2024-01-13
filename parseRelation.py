# parse input realtions
def parseRelation(relations: str) -> dict:
    # Splitting the data
    parts = relations.split("}")
    # initialize table
    tables = {}
    # get the table
    for part in parts[:-1]:
        part = part + "}"
        # get the "Student"
        equalIndex = part.find("=")
        tableName = part[:equalIndex].strip()
        # add into the tables
        tables[tableName] = {}

        # get the data between { }
        lines = part.strip().split("\n")[1:-1]
        lines = [line for line in lines if line != ""]

        # create column of the table
        headers = [header.strip() for header in lines[0].split(",")]
        for i in range(len(headers)):
            tables[tableName][headers[i]] = []
            # get each column data
            for line in lines[1:]:
                values = line.strip().split(",")
                values = [value.strip().strip("'") for value in values]
                if values[i] == "NULL":
                    tables[tableName][headers[i]].append(None)
                else:
                    if isStringFloat(values[i]):
                        tables[tableName][headers[i]].append(float(values[i]))
                    else:
                        tables[tableName][headers[i]].append(values[i])
    return tables


# check if is float
def isStringFloat(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
