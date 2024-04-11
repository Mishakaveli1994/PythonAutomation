import re

from collections import deque 

# string = """T100 A
# T100 C
# T100 C
# T100 C
# T100 C
# T200 Start
# T100 C
# T250 SomethingElse
# T300 End
# T500 Random"""

# start = 'T200 Start'
# end = 'T300 End'

# split_string = string.split('\n')
# print(split_string)
# idx_start = split_string.index(start)
# idx_end = split_string.index(end)
# print(idx_start)
# print(idx_end)
# print(split_string[idx_start:idx_end+1])


# find_start_end = re.compile(r'(T200 Start(\n|.+)+?T300 End)')

# match = find_start_end.findall(string)
# full_match = match[0][0]

# print(full_match)

string = """T100 A
T100 C
T100 C
T100 C
T100 C
T200 Start
T250 SomethingElse
T300 End
T100 C
T100 C
T200 Start
T250 SomethingElse
T300 End
T200 Start
T250 SomethingElse
T300 End
T500 Random"""

# start_end_deque = deque()

# for line in string.split('\n'):
#     if line.startswith('T200'):
#         start_end_deque.appendleft(line)
#         continue
#     elif line.startswith('T300'):
#         start_end_deque.appendleft(line)
#         continue

#     if start_end_deque:
#         last_elem = start_end_deque.popleft()
#         start_end_deque.appendleft(last_elem)
#         if not last_elem.startswith('T300'):
#             start_end_deque.appendleft(line)

# print(start_end_deque)

start = 'T200'
end = 'T300'

group_list = []

group = []
for line in string.split('\n'):
    if line.startswith(start):
        group.append(line)
        continue
    elif line.startswith(end):
        group.append(line)
        group_list.append(group)
        group = []
        continue

    if group:
        group.append(line)

for group in group_list:
    print(group)