def format_money(value: float) -> str:
    is_int = isinstance(value, int)
    is_float_int = isinstance(value, float) and value.is_integer()

    if is_int or is_float_int:
        return str(int(value))

    value_str = f"{value: .2f}".lstrip()
    return value_str.rstrip("0").rstrip(".")
