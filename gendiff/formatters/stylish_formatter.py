from gendiff.formatters.bool_format import bool_format_value


def stylish(diff_data):
    result = []
    if diff_data == []:
        return '{}'
    for item in diff_data:
        if item['type'] == 'unchanged':
            result.append(f'  {item['key']}: \
{bool_format_value(item['value'])}')
        elif item['type'] == 'changed':
            result.append(f'- {item['key']}: \
{bool_format_value(item['old_value'])}')
            result.append(f'+ {item['key']}: \
{bool_format_value(item['new_value'])}')
        elif item['type'] == 'removed':
            result.append(f'- {item['key']}: \
{bool_format_value(item['value'])}')
        elif item['type'] == 'added':
            result.append(f'+ {item['key']}: \
{bool_format_value(item['value'])}')
    stylish_diff = f'{{\n  {'\n  '.join(result)}\n}}'
    return stylish_diff
