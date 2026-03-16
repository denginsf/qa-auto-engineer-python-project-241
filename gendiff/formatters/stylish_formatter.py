def stylish(diff_data):
    result = []
    if diff_data == []:
        return '{}'
    for item in diff_data:
        if item['status'] == 'unchanged':
            result.append(f'  {item['key']}: {item['value']}')
        elif item['status'] == 'changed':
            result.append(f'- {item['key']}: {item['old_value']}')
            result.append(f'+ {item['key']}: {item['new_value']}')
        elif item['status'] == 'removed':
            result.append(f'- {item['key']}: {item['value']}')
        elif item['status'] == 'added':
            result.append(f'+ {item['key']}: {item['value']}')
    stylish_diff = f'{{\n  {'\n  '.join(result)}\n}}'
    return stylish_diff
