def bool_format_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    return value