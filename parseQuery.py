import re
from selection import selection
from projection import projection
from join import join
from set import set


def select_parse_query(query_string):
    # Define the pattern using regular expressions
    pattern = r"^\s*select\s+\[([^\]]+)\]\s+\((.*?)\)\s*$"

    # Match the pattern against the input string
    match = re.match(pattern, query_string)

    # Check if there is a match
    if match:
        # Extract variables from the matched groups
        condition = match.group(1)
        table = match.group(2)

        return condition, table
    else:
        return None


def project_parse_query(query_string):
    # Define the pattern using regular expressions
    pattern = r"^\s*project\s+\[([^\]]+)\]\s+\((.*?)\)\s*$"

    # Match the pattern against the input string
    match = re.match(pattern, query_string)

    # Check if there is a match
    if match:
        # Extract variables from the matched groups
        condition = match.group(1)
        table = match.group(2)

        return condition, table
    else:
        return None


def join_parse_query(query_string):
    # Define the pattern using regular expressions
    pattern = r"^\s*join\s+\[([^\]]+)\]\s+\((.*?)\)\s*$"

    # Match the pattern against the input string
    match = re.match(pattern, query_string)

    # Check if there is a match
    if match:
        # Extract variables from the matched groups
        condition = match.group(1)
        table = match.group(2)

        return condition, table
    else:
        return None


def ljoin_parse_query(query_string):
    # Define the pattern using regular expressions
    pattern = r"^\s*ljoin\s+\[([^\]]+)\]\s+\((.*?)\)\s*$"

    # Match the pattern against the input string
    match = re.match(pattern, query_string)

    # Check if there is a match
    if match:
        # Extract variables from the matched groups
        condition = match.group(1)
        table = match.group(2)

        return condition, table
    else:
        return None


def rjoin_parse_query(query_string):
    # Define the pattern using regular expressions
    pattern = r"^\s*rjoin\s+\[([^\]]+)\]\s+\((.*?)\)\s*$"

    # Match the pattern against the input string
    match = re.match(pattern, query_string)

    # Check if there is a match
    if match:
        # Extract variables from the matched groups
        condition = match.group(1)
        table = match.group(2)

        return condition, table
    else:
        return None


def fjoin_parse_query(query_string):
    # Define the pattern using regular expressions
    pattern = r"^\s*fjoin\s+\[([^\]]+)\]\s+\((.*?)\)\s*$"

    # Match the pattern against the input string
    match = re.match(pattern, query_string)

    # Check if there is a match
    if match:
        # Extract variables from the matched groups
        condition = match.group(1)
        table = match.group(2)

        return condition, table
    else:
        return None


def set_parse_query(query_string):
    result = parse_complex_string(query_string)
    if result:
        parts, operator = result
        table1 = remove_outermost_parentheses(parts[0])
        table2 = remove_outermost_parentheses(parts[1])
        return table1, operator, table2
    else:
        return None


def parse_complex_string(s):
    parts = []
    operator = None
    balance = 0
    current_part = ""

    for char in s:
        if char in "()":
            balance += 1 if char == "(" else -1
            current_part += char
        elif balance == 0 and char in "+-*/^":
            if not operator:
                operator = char
                parts.append(current_part.strip())
                current_part = ""
            else:
                current_part += char
        else:
            current_part += char

    if current_part:
        parts.append(current_part.strip())

    if len(parts) == 2 and operator:
        return parts, operator
    else:
        return None


def remove_outermost_parentheses(s):
    # Check if the string starts and ends with parentheses
    if s.startswith("(") and s.endswith(")"):
        # Check if the parentheses are correctly paired and enclosing the entire string
        balance = 0
        for i, char in enumerate(s):
            if char == "(":
                balance += 1
            elif char == ")":
                balance -= 1

            # If balance is zero before the end of the string, it means the outer parentheses are not enclosing the entire string
            if balance == 0 and i < len(s) - 1:
                return s  # Return the original string

        # If the loop completes without returning, it means the outer parentheses are correctly paired and can be removed
        return s[1:-1]
    else:
        return s  # Return the original string if it does not start and end with parentheses


def is_two_single_words(s):
    # Regular expression to match two words separated by a comma, ignoring spaces
    pattern = r"^\s*\w+\s*,\s*\w+\s*$"

    # Use re.match to check if the string matches the pattern
    return bool(re.match(pattern, s))


def distribute(tables, method, condition, table):
    if method == "select":
        if table.isalpha():
            return selection(tables[table], condition)
        else:
            return selection(parseQuery(tables, table), condition)

    if method == "project":
        if table.isalpha():
            return projection(tables[table], condition)
        else:
            return projection(parseQuery(tables, table), condition)
    if method in ["join", "ljoin", "rjoin", "fjoin"]:
        parsed = [part.strip() for part in table.split(",")]
        return join(
            parsed[0],
            tables[parsed[0]],
            parsed[1],
            tables[parsed[1]],
            method,
            condition,
        )
    if method in ["+", "^", "-"]:
        table1 = condition
        table2 = table
        if table1.isalpha() and table2.isalpha():
            return set(method, tables[table1], tables[table2])
        elif table1.isalpha():
            return set(method, tables[table1], parseQuery(table2))
        elif table2.isalpha():
            return set(method, parseQuery(tables, table1), tables[table2])
        else:
            return set(method, parseQuery(tables, table1), parseQuery(tables, table2))

    return {}


def parseQuery(tables, query_string):
    try:
        condition, table = select_parse_query(query_string)
        return distribute(tables, "select", condition, table)
    except:
        pass

    try:
        condition, table = project_parse_query(query_string)
        return distribute(tables, "project", condition, table)
    except:
        pass

    try:
        condition, table = join_parse_query(query_string)
        return distribute(tables, "join", condition, table)
    except:
        pass

    try:
        condition, table = ljoin_parse_query(query_string)
        return distribute(tables, "ljoin", condition, table)
    except:
        pass

    try:
        condition, table = rjoin_parse_query(query_string)
        return distribute(tables, "rjoin", condition, table)
    except:
        pass

    try:
        condition, table = fjoin_parse_query(query_string)
        return distribute(tables, "fjoin", condition, table)
    except:
        pass

    try:
        table1, operation, table2 = set_parse_query(query_string)
        return distribute(tables, operation, table1, table2)
    except:
        pass

    return None
