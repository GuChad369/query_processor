from parseRelation import parseRelation
from prettytable import PrettyTable
from parseQuery import parseQuery


# read the input
def readMultilineInput(stop_word="END"):
    print("Enter the relation. Type 'END' on a new line when you're done:")
    lines = []
    while True:
        line = input()
        if line == stop_word:
            break
        lines.append(line)
    return "\n".join(lines)


# print the table
def print_table(table_name, table_data):
    print()
    table = PrettyTable()
    table.title = table_name
    table.field_names = list(table_data.keys())
    rows = zip(*table_data.values())
    for row in rows:
        table.add_row(row)
    print(table)


tables = {}

while not tables:
    # get the user input of the relation
    relations = readMultilineInput()
    # create tables
    tables = parseRelation(relations)
    if not tables:
        print("Wrong format!")


# print the relations
print("You have created the following tables:")
for name, contents in tables.items():
    print_table(name, contents)

while True:
    print("Please enter your query in required format: 0 - exit")
    query = input()

    # exit the system
    if query == "0":
        exit()

    # do query
    try:
        res = parseQuery(tables, query)
        res = {"Result": res}
        # print the result
        for name, contents in res.items():
            print_table(name, contents)
    except:
        print("Please enter the right format!")
