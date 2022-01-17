def part1(file_name = 'day 3.txt'):
    with open(file_name, 'r') as f:
        lines = f.readlines()
        diagnostics = [entry.strip() for entry in lines]

    gamma, epsilon = '', ''
    for i in range(len(diagnostics[0])):
        all_entries_at_pos = [entry[i] for entry in diagnostics]
        if all_entries_at_pos.count('0') > len(diagnostics) / 2:
            gamma += '0'
            epsilon += '1'
        else:
            gamma += '1'
            epsilon += '0'
    print('gamma :', gamma, ":", int(gamma, base=2))
    print('epsilon :', epsilon, ":", int(epsilon, base=2))
    print('Conso Electrique :', int(gamma, base=2) * int(epsilon, base=2))

print(part1())