with open('README-TEMPLATE.md') as f:
    lines = f.readlines()

variable_name = 'repo'
variable_value = None

for line in lines:
    if line.startswith(f'[{variable_name}]'):
        variable_value = line.split(':')[-1].strip()
        break

print(variable_value)
