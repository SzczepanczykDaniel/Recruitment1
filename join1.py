import pandas as pd
import argparse

parser = argparse.ArgumentParser(description='Join 2 .csv files')
parser.add_argument('--join', action='store_true', help='if you want to run program you have to start with this command')
parser.add_argument('file_path1',
                    type=str,
                    help="Insert path of the first file")
parser.add_argument('file_path2',
                    type=str,
                    help="Insert path of the second file")
parser.add_argument('column_name',
                    type=str,
                    help="Chose column name which you want to join")
parser.add_argument('-j', '--join_type',
                    type=str,
                    choices={'inner', 'left', 'right'},
                    required=False,
                    help="Chose inner, left or right joining type, if you not chose any type of joining,"
                         " files by default it will join as inner")

args = parser.parse_args()
print(args)
print(args.join)


def main():
    file_path1 = args.file_path1
    file_path2 = args.file_path2
    join_type = args.join_type
    column_name = args.column_name

    def path1_error_handling(file_path):
        if not file_path.endswith('.csv'):
            file_path0 = input('Invalid file 1 type, please insert path to the csv file: ')
            path1_error_handling(file_path0)

        else:
            try:
                global data1
                data1 = pd.read_csv(file_path)


            except FileNotFoundError:
                print('Invalid file path!')
                file_path = input('Insert correct file 1 path: ')
                path1_error_handling(file_path)
            else:

                data1 = pd.read_csv(file_path)

    def path2_error_handling(file_path):
        if not file_path.endswith('.csv'):
            file_path0 = input('Invalid file 2 type, please insert path to the csv file: ')
            path2_error_handling(file_path0)

        else:
            try:
                global data2
                data2 = pd.read_csv(file_path)

            except FileNotFoundError:
                print('Invalid file path!')
                file_path = input('Insert correct file 2 path: ')
                path2_error_handling(file_path)
            else:
                data2 = pd.read_csv(file_path)

    path1_error_handling(file_path1)
    path2_error_handling(file_path2)

    columns = []
    columns1 = data1.columns
    columns2 = data2.columns
    columns = columns1.intersection(columns2)

    def correct_column_name(column_name0):
        if column_name0 not in columns:
            column_name0 = input('enter correct column name: ')
            correct_column_name(column_name0)
        else:
            return column_name0

    column_name = correct_column_name(column_name)
    default_join_type = 'inner'

    if not join_type:
        join_type = default_join_type

    output = pd.merge(data1, data2, on=column_name, how=join_type)
    print(output)


if __name__ == '__main__':

    if args.join:
        main()
    else:
        print('You forgot about join command')
        exit()
