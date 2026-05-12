from name_function import get_formatted_name

def test_name_func():
    format_name = get_formatted_name('janis', 'Jo', 'Joplin')
    assert format_name == 'Janis Jo Joplin'

def test_name_else_func():
    formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
    assert formatted_name == 'Wolfgang Mozart Amadeus'
    

