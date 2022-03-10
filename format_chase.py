import sys
import csv
import argparse

def format_chase(input_file_name: str, output_file_name: str):
    """

    Input format will be:
    Transaction Date,Post Date,Description,Category,Type,Amount,Memo

    Output format will be:
    "Date","Payee","Memo","Outflow","Inflow"
    """

    with open(input_file_name, 'r') as chase_format, open(output_file_name, 'w') as ynab_format:
        reader = csv.DictReader(chase_format)
        fieldnames = ["Date","Payee","Memo","Outflow","Inflow"]
        writer = csv.DictWriter(ynab_format, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            print(row)
            if row['Type'] == 'Payment':
                outflow = ''
                inflow = row['Amount']
            else:
                outflow = row['Amount'][1:] # strip off '-' sign
                inflow = ''

            out_row = {
                'Date': row['Transaction Date'],
                'Payee': row['Description'],
                'Memo': '',
                'Outflow': outflow,
                'Inflow': inflow
            }
            writer.writerow(out_row)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file_name", help="path to the input csv file.")
    parser.add_argument("output_file_name", help="path to write the output csv file to.")
    args = parser.parse_args()
    input_file_name = args.input_file_name
    output_file_name = args.output_file_name

    format_chase(input_file_name, output_file_name)

    return 0

if __name__ == '__main__':
    sys.exit(main())
