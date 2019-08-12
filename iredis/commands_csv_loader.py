import csv
import copy

# FIXME path
t = {}
first_line = True
with open("command_syntax.csv") as command_syntax:
    csvreader = csv.reader(command_syntax)
    for line in csvreader:
        if first_line:
            first_line=False
            continue
        group, command, syntax = line
        t.setdefault(syntax, []).append(command)

original_commands = copy.deepcopy(t)

for syntax in t.keys():
    commands = t[syntax]
    lower_commands = [command.lower() for command in commands]
    commands += lower_commands
    re_commands = [command.replace(" ", "\s+") for command in commands]
    t[syntax] = "|".join(re_commands)
