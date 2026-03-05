def generate_diff(file1, file2):
    result = []
    for key, value in file1.items():
        if key in file2.keys() and file2[key] == value:
            result.append(f'  {key}: {value}')
        elif key in file2.keys() and file2[key] != value:
            result.append(f'- {key}: {value}')
            result.append(f'+ {key}: {file2[key]}')
        elif key not in file2.keys():
            result.append(f'- {key}: {value}')
    for key2, value2 in file2.items():
        if key2 not in file1.keys():
            result.append(f'+ {key2}: {file2[key2]}')
    diff = f'{{\n  {'\n  '.join(result)}\n}}'
    print(diff)
    return diff