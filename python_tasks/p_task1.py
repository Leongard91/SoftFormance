raw_input = input('Enter number of rows and columns (x,y): ')
inp_list = raw_input.split(',')
if len(inp_list) > 2:
    print('Only comma separated two digits are acceptable!')
try: x, y = int(inp_list[0].strip()), int(inp_list[1].strip())
except: print('Only comma separated two digits are acceptable!')

output = []
count = 1
for row in range(x):
    new_row = []
    for col in range(y):
        new_row.append(count)
        count += 1
    output.append(new_row)
print(output)