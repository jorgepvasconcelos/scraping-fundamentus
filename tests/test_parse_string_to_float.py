from src.transform import parse_string_to_float


def test_parse_string_to_float_with_1_comma():
    input_value = "84,98"
    expected_output = 84.98

    func_return = parse_string_to_float(input_value)

    assert func_return == expected_output


def test_parse_string_to_float_with_1_dot():
    input_value = "106.461"
    expected_output = 106461

    func_return = parse_string_to_float(input_value)

    assert func_return == expected_output


def test_parse_string_to_float_with_1_dot_and_1_comma():
    input_value = "23.998,00"
    expected_output = 23998.00

    func_return = parse_string_to_float(input_value)

    assert func_return == expected_output


def test_parse_string_to_float_with_more_than_1_dot_and_0_comma_case_1():
    input_value = "927.491.000"
    expected_output = 927491000

    func_return = parse_string_to_float(input_value)

    assert func_return == expected_output


def test_parse_string_to_float_with_more_than_1_dot_and_0_comma_case_2():
    input_value = "2.923.290"
    expected_output = 2923290

    func_return = parse_string_to_float(input_value)

    assert func_return == expected_output


def test_parse_string_to_float_with_more_than_1_dot_and_1_comma():
    input_value = "3.584.650,00"
    expected_output = 3584650.00

    func_return = parse_string_to_float(input_value)

    assert func_return == expected_output


def test_parse_string_to_float_with_0_dot_and_0_comma():
    input_value = "10"
    expected_output = 10

    func_return = parse_string_to_float(input_value)

    assert func_return == expected_output
