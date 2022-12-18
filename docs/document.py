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
print(variable_value)
