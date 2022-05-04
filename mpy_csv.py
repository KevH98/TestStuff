#
# Class to handle CSV files
#


import os
import io
import csv

class Csv:
    """ Class to handle custom CSV interactions """

    @staticmethod
    def csv_to_array(csv_in, encoding="utf-8-sig", remove_point_zero=False, replace_substrings=None):
        """
        Convert csv file or csv string to a 2d array
        csv_in -- str(path to file) or str(csv string)
        remove_point_zero -- bool. convert decimal 71.0 to 71 only #<-- todo : link jira to this discussion
        replace_substrings  -- [['text0', 'text'], ]
        """

        table = []
        table_string = csv_in
        
        # convert file to string
        if os.path.isfile(table_string):
            with open(table_string, "r", encoding=encoding) as f:
                table_string = f.read()
                
        # clean input text if replacement substrings defined 
        if replace_substrings is not None:
            for sub in replace_substrings:
                table_string = table_string.replace(sub[0], sub[1])
                
        # convert string to csv
        f = io.StringIO(table_string)  # csv reader requires file object
        table = [x for x in csv.reader(f)]

        # data = [[c.replace('\ufeff', '') for c in row] for row in reader]
            
        # remove ending ".0" if requested
        if remove_point_zero:
            for row in range(len(table)):
                for col in range(len(table[row])):
                    if table[row][col].endswith(".0"):
                        table[row][col] = table[row][col][:-2]

        return table