def json_format(diff_data):
    result = {}
    if not diff_data:
        return {}
    for i in diff_data:
        if i['type'] == 'changed':
            result[i['key']] = {'diff': 'changed', 'old_value': i['old_value'], 
            'new_value': i['new_value']}
        elif i['type'] == 'added':
            result[i['key']] = {'diff': 'added', 'value': i['value']}
        elif i['type'] == 'removed':
            result[i['key']] = {'diff': 'removed', 'value': i['value']}
        elif i['type'] == 'unchanged':
            result[i['key']] = i['value']
        else:
            child_diff = i['children']
            child = json_format(child_diff)
            result[i['key']] = child
    return result