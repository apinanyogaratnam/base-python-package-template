with open('README-TEMPLATE.md') as f:
    lines = f.readlines()

variable_name = 'repo'
variable_value = next(
    (
        line.split(':')[-1].strip()
        for line in lines
        if line.startswith(f'[{variable_name}]')
    ),
    None,
)

ignore_line = f'[{variable_name}]: {variable_name}'

for line in lines:
    if ignore_line in line:
        continue

    if f'[{variable_name}]' in line:
        line = line.replace(f'[{variable_name}]', variable_value)

with open('test.txt', 'w') as f:
    for line in lines:
        f.write(line)
