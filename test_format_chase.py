from format_chase import format_chase


def test_format_chase_simple():

        test_input_file = 'test_csv_files/simple_input.csv'

        format_chase(test_input_file, 'test_csv_files/output-from-running-test.csv')

        with open('test_csv_files/simple_output.csv', 'r') as test_output_file, open('test_csv_files/output-from-running-test.csv', 'r') as output_file:
            test_output = test_output_file.read()
            output = output_file.read()
            assert output == test_output



def test_format_chase():

        test_input_file = 'test_csv_files/example_input.csv'

        format_chase(test_input_file, 'test_csv_files/output-from-running-test.csv')

        with open('test_csv_files/example_output.csv', 'r') as test_output_file, open('test_csv_files/output-from-running-test.csv', 'r') as output_file:
            test_output = test_output_file.read()
            output = output_file.read()
            assert output == test_output

