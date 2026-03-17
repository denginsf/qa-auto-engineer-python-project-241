def diff_return(file1, file2):
    if file1 is None:
        file1 = {}
    if file2 is None:
        file2 = {}
    diff = []
    all_keys = sorted(set(file1.keys()) | set(file2.keys()))
    for key in all_keys:
        if key not in file2.keys():
            diff.append({'key': key, 'type': 'removed', 'value': file1[key]})
        elif key not in file1.keys():
            diff.append({'key': key, 'type': 'added', 'value': file2[key]})
        else:
            extra_file1 = file1[key]
            extra_file2 = file2[key]
            if isinstance(extra_file1, dict) and isinstance(extra_file2, dict):
                child = diff_return(extra_file1, extra_file2)
                diff.append({'key': key, 'type': 'nested', 'children': child})
            else:
                if extra_file1 == extra_file2:
                    diff.append({'key': key, 'type': 'unchanged',
                    'value': extra_file1})
                elif extra_file1 != extra_file2:
                    diff.append({'key': key, 'type': 'changed', 
                    'old_value': extra_file1, 'new_value': extra_file2})
    return diff
