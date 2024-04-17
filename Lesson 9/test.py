with open('./log.txt', 'r') as f:
    read = [(idx, line[0:5]) if line != '\n' else (idx, '')
            for idx, line in enumerate(f.readlines())]

between_set = set()
values = {'T-047',
          'T-048',
          'T-049',
          'T-050',
          'T-051',
          'T-052',
          'T-053',
          'T-054',
          'T-055',
          'T-056',
          'T-057',
          'T-058',
}

expected_matches = 3

complete_set = set(list(values) + ['T-044', 'T-045'])
matches = 0
start = 0
end = 0
for row, tag in read:
    if tag == 'T-044':
        between_set.clear()
        between_set.add(tag)
        start = row
    elif tag == 'T-045' and between_set:
        between_set.add(tag)
        end = row
        diff = between_set.difference(complete_set)
        if not diff:
            print(f'Exact match found at {start} and {end}')
            matches += 1
        start = 0
        end = 0
        between_set.clear()
    elif tag in values:
        between_set.add(tag)

assert (matches == expected_matches), f"Expected {expected_matches} matches, but got {matches}"
print('Exact matches found!')

# Т-044 (стартов, съдържащ "START" на реда) и Т-045 (краен, съдържащ "END" на реда):
# T-046, T-047, T-048, T-049, T-050, T-051, T-052, T-053, T-054, T-055, T-056, T-057 и Т-058
