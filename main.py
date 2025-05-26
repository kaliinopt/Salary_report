import argparse
from file_reader import parse_csv_file

def pars_args():
    parser = argparse.ArgumentParser(description="Employee report is generating from csv")

    parser.add_argument('files', metavar='FILE', type=str, nargs='+', help='Input files')

    parser.add_argument('--report', type=str, required=True, help='payout')

    return parser.parse_args()


def main():
    args = pars_args()

    try:
        pass
        
    except Exception as e:
        print(e)
        exit(1)


if __name__ == "__main__":
    main()