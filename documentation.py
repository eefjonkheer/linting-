import pandas as pd


"""
Read an Excel file and return the headers 

Args: 
   a, string, the path to an Excel file
   print_columns, boolean, print the column headers during the retrieval (default is False)
   
Returns: 
 column_headers, a list with the column headers

"""
def x(a, print_columns=False):
   b = pd.read_excel(a)
   column_headers = list(b.columns.values)
   if print_columns:
       print("\n".join(column_headers))
   return column_headers
