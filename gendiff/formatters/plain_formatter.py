def plain(diff_data):
    result = []
    if diff_data == []:
        return 'Nothing was changed.'
    for item in diff_data:
        if item['status'] == 'changed':
            result.append(f"Property '{item['key']}' was updated. "
                        f"From {item['old_value']} to {item['new_value']}")
        elif item['status'] == 'removed':
            result.append(f"Property '{item['key']}' was removed")
        elif item['status'] == 'added':
            result.append(f"Property '{item['key']}' was added. " 
                        f"With value: {item['value']}")
    plain_diff = f'{'\n'.join(result)}'
    return plain_diff