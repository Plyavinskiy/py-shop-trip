def format_money(value: float) -> str:
    if value.is_integer():
        return str(int(value))

    value_str = f"{value: .2f}".lstrip()
    if value_str.endswith("0"):
        return value_str[:-1]
    return value_str
