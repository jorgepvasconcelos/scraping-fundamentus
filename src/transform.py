import copy


def tranform_percentage_in_float(value: str) -> float:
    value = value.replace("%", '')
    # value = value.replace(",", '.')
    # return float(value)
    return tranform_in_float(value)


def tranform_in_float(value: str) -> float:
    if value.count(',') == 1 and value.count('.') == 0:
        "84,98"
        value = value.replace(",", '.')
        return float(value)

    if value.count('.') == 1 and value.count(',') == 0:
        "106.461"
        return float(value)

    if value.count('.') == 1 and value.count(',') == 1:
        "23.998,00"
        value = value.replace(".", "", )
        value = value.replace(",", ".", )
        return float(value)

    if value.count('.') > 1 and value.count(',') == 0:
        "927.491.000"
        dot_qtd = value.count(".")
        value = value.replace(".", "", dot_qtd - 1)
        return float(value)

    if value.count('.') > 1 and value.count(',') == 1:
        "3.584.650,00"
        value = value.replace(".", "")
        value = value.replace(",", ".")
        return float(value)

    if value.count('.') == 0 and value.count(',') == 0:
        return float(value)


def transform_values(data_list: list[dict]) -> list[dict]:
    data_trasnformed = copy.copy(data_list)
    not_number_column = ['CODIGO', 'SEGMENTO']

    for index, data in enumerate(data_list):
        for key, value in data.items():
            if "%" in key:
                data_trasnformed[index][key] = tranform_percentage_in_float(value)
                continue
            if not key in not_number_column:
                data_trasnformed[index][key] = tranform_in_float(value)
                continue

    return data_trasnformed
