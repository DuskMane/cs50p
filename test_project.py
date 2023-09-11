from project import expand,observe,game,quit,data
import pytest
from unittest.mock import patch

def test_expand():
    test_words = ['What', 'Why', 'Cat', 'Dog']
    test_translations = ['Co', 'Dlaczego', 'Kot', 'Pies']

    # Testing the test words
    for i in range(len(test_words)):
        with patch('builtins.input', side_effect=[test_words[i], '']):

            with patch('builtins.print') as mock_print:
                expand()

                assert test_words[i] in data

                mock_print.assert_called_with(f'{test_words[i]} -> {test_translations[i]}')

def test_observe():
    with patch('builtins.print') as mock_print, patch('builtins.input', return_value=''):
        observe()

        expected_output = '\n'.join(f'{i} -> {data[i]}' for i in list(data.keys()))
        test_len = 0
        # To check if the printed lines exist in expected output
        for call in mock_print.call_args_list:
            printed_line = call[0][0]
            test_len += 1
            assert printed_line in expected_output
        assert test_len == int(expected_output.count('\n'))+1

def test_game():
    input_values = ['999999', '0', '']

    expected_output = [
        f"Invalid input, please enter a NUMBER which is not larger than the number of words in your dictionary ({len(list(data.keys()))}), or enter 0 to go back to the main menu.",
        "Your score is 0/0"
    ]

    with patch('builtins.input', side_effect=input_values), patch('builtins.print') as mock_print:
        game()

        test_len = 0
        for call in mock_print.call_args_list:
            printed_line = call[0][0]
            test_len += 1
            assert printed_line in expected_output
        assert test_len == 2

def test_quit():
    # Quit function should sys.exit with given string printed
    with pytest.raises(SystemExit) as info:
        quit()
    assert str(info.value) == "Good work! Hope to see you soon!"

if __name__ == '__main__':
    pytest.main()