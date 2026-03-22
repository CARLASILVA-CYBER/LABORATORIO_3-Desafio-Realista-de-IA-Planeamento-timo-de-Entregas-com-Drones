def is_valid(assignment, var, value):
    for v in assignment:
        if assignment[v] == value:
            return False
    return True

def backtracking(variables, domains, assignment={}):
    if len(assignment) == len(variables):
        return assignment

    var = variables[len(assignment)]

    for value in domains:
        if is_valid(assignment, var, value):
            assignment[var] = value
            result = backtracking(variables, domains, assignment)

            if result:
                return result

            del assignment[var]

    return None

variables = ["Math", "AI", "Networks"]
domains = ["Morning", "Afternoon", "Evening"]

solution = backtracking(variables, domains)
print(solution)
