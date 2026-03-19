from gendiff.formatters.bool_format import bool_format_value


def plain(diff_data):
    result = []
    if diff_data == []:
        return 'Nothing was changed.'
    for item in diff_data:
        if item['type'] == 'changed':
            result.append(f"Property '{item['key']}' was updated. "
                        f"From {bool_format_value(item['old_value'])} to \
{bool_format_value(item['new_value'])}")
        elif item['type'] == 'removed':
            result.append(f"Property '{item['key']}' was removed")
        elif item['type'] == 'added':
            result.append(f"Property '{item['key']}' was added \
with value: {bool_format_value(item['value'])}")
    plain_diff = f'{'\n'.join(result)}'
    return plain_diff