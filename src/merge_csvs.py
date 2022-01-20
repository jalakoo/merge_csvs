import argparse
import os
import pandas as pd
import glob
import csv


def merge_csvs(input_folder, output_filepath, should_log):
    if should_log:
        print(f'merge_csvs: merge_csvs: input_folder: {input_folder}')
    all_files = glob.glob(input_folder + "/*.csv")
    file_dataframes = (pd.read_csv(file, sep=",", keep_default_na=False)
                       for file in all_files)
    merged_files = pd.concat(file_dataframes)
    merged_files.to_csv(output_filepath, index=False,
                        encoding="utf-8", quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
    if (should_log):
        print('merge_csvs.py: merge_csvs complete')

# Validate path argument


def dir_path(string):
    if os.path.isdir(string):
        return string
    else:
        raise NotADirectoryError(string)


# def file_path(string):
#     if os.path.exists(string):
#         return string
#     else:
#         raise TypeError(string)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    working_path = os.getcwd()
    default_input_path = os.path.dirname(working_path + "/input/")
    default_output_path = working_path + "/output/joined.csv"
    parser.add_argument(
        "-i", '--input', help='Folder path of csv files to process', type=dir_path, default=default_input_path)
    parser.add_argument(
        "-o", '--output', help='Filepath of joined csv file', type=str, default=default_output_path)
    parser.add_argument(
        "-v", '--verbose', help='Log function outputs', type=bool, default=False)
    args = parser.parse_args()
    merge_csvs(args.input, args.output, args.verbose)
