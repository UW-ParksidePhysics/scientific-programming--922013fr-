from two_column_text_read import two_column_text_read
from bivariate_statistics import bivariate_statistics
from quadratic_fit import quadratic_fit
from fit_curve_array import fit_curve_array
from plot_data_with_fit import plot_data_with_fit
from equations_of_state import fit_eos
from convert_units import convert_units
from numpy import linspace
import matplotlib.pyplot as plt

display_graph = True 

def parse_file_name(file_name):
  to_parse = file_name.split(".")
  symbol = to_parse[0]
  structure = to_parse[1]
  acronym = to_parse[2]
  return symbol, structure, acronym   #1
