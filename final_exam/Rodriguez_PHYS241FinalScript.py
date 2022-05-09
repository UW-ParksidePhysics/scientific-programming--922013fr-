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
    return symbol, structure, acronym


file_name = "Cu.Fm-3m.GGA-PBE.volumes_energies.dat"
symbol, structure, acronym = parse_file_name(file_name)
array = two_column_text_read("Cu.Fm-3m.GGA-PBE.volumes_energies.dat")
statistics = bivariate_statistics(array)
quadratic_coefficients = quadratic_fit(array)
print(quadratic_coefficients)

min_x = statistics[2]
max_x = statistics[3]

undo_array = zip(*array)
array_2 = list(undo_array)
fit_eos_curve, fit_parameters = fit_eos(array[0], array[1], quadratic_coefficients, eos='birch-murrain',
                                        number_of_points=50)
bulk_modulus = fit_parameters[1]
equilibrium_volume = fit_parameters[3]


def annotate_graph(symbol, structure):
    ax.annotate(symbol, xy=(130, 0.001))

    ax.annotate(r'$ {}\overline{{{}}} {}$'.format(structure[0:2],
                                                  structure[3],
                                                  structure[1]),
                xy=(115, 0))

    ax.annotate('K_0={:.6f}GPa'.format(bulk_modulus_gpa),
                xy=(115, 0.001))

    ax.annotate('V_0={:.3f}A^3/atom'.format(eq_vol),
                xy=(115, -0.001))
    plt.axvline(eq_vol - array_2[0][array_2[1].index(min(array_2[1]))] * 0.01, color="black", linestyle='-')

    plt.text(91, -0.0025, "created by Francisco Rodriguez May/09/2022")
    plt.title("{} Equation of State for {} in DFT {}".format('birch-murrain', symbol, acronym))
    return ax, plt


fig = plt.figure()
ax = fig.add_subplot(111)


volumes = linspace(min(array_2[0]), max(array_2[0]), len(fit_eos_curve))
line1, = ax.plot(array_2[0], array_2[1], 'o')
line2, = ax.plot(volumes, fit_eos_curve, color="blue")

x_min = (min(array_2[0]) - (min(array_2[0]) * 0.10))
x_max = (max(array_2[0]) + (max(array_2[0]) * 0.10))
y_min = (-0.003)
y_max = 0.003

plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xlabel(r'$V$ (Å$^3$/atom)')
plt.ylabel(r'$E$ (eV/atom)')
bulk_modulus_gpa = convert_units(bulk_modulus, "rb/cb")
eq_vol = array_2[0][array_2[1].index(min(array_2[1]))]
annotate_graph(symbol, structure)

fit_curve = fit_curve_array(quadratic_coefficients, min_x, max_x, number_of_points=100)
scatter_plot, curve_plot = plot_data_with_fit(array, fit_curve, data_format="bo", fit_format="k")

if display_graph:
    plt.show()
elif not display_graph:
    plt.savefig("Cu.Fm-3m.GGA-PBE.volumes_energies.dat")

