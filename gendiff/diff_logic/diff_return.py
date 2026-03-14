def diff_return(file1, file2):
    if file1 is None:
        file1 = {}
    if file2 is None:
        file2 = {}
    diff = []
    if file1 == {} and file2 == {}:
        return []
    for key, value in file1.items():
        if key in file2.keys() and file2[key] == value:
            diff.append({'key': key, 'status': 'unchanged', 'value': value})
        elif key in file2.keys() and file2[key] != value:
            diff.append({'key': key, 'status': 'changed', 'old_value': value,
            'new_value': file2[key]})
        elif key not in file2.keys():
            diff.append({'key': key, 'status': 'removed', 'value': value})
    for key2, value2 in file2.items():
        if key2 not in file1.keys():
            diff.append({'key': key2, 'status': 'added', 'value': value2})
    return diff
