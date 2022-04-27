import numpy as np
import matplotlib.pyplot as plt


# ### RENAME from mini_project.m to (your_project_short_name).m
# Comments describing mini-project ~ 100-200 words
# This program would be able to calculate the distance between the earth
# and the sun at 4 different points around the orbital axis as it goes
# around the sun. It is done by using as input of kepler 3rd law and
# equation of motion. More specifically finding the distance(m) at 4
# different seasons within a one-year span. We already know two positions distance
# and will find a function to help calculate at 2-4 other points. The earth travels
# around the sun in an orbital function.

def get_apsides():
    import pandas as pd

    url = 'https://en.wikipedia.org/wiki/Earth%27s_orbit'
    dataframes = pd.read_html(url)
    earth_data = dataframes[0].transpose()
    earth_data.columns = earth_data.iloc[0]
    earth_data = earth_data.drop([0])
    perihelion = float(earth_data['perihelion'].iloc[0].split()[0].split('×')[0]) * 1.e9
    aphelion = float(earth_data['aphelion'].iloc[0].split()[0].split('×')[0]) * 1.e9
    return aphelion, perihelion


def calculate_elipse_semi_axes(apsides):
    semi_major_axis = np.mean(apsides)
    focal_length = 0.5 * np.diff(apsides)
    semi_minor_axis = np.sqrt(semi_major_axis ** 2 - focal_length ** 2)
    semi_axes = [semi_major_axis, semi_minor_axis]
    return semi_axes


def plot_ellipse(semi_axes):
    thetas = np.linspace(0, 2. * np.pi)
    xs = semi_axes[0] * np.cos(thetas)
    ys = semi_axes[1] * np.sin(thetas)
    plt.plot(xs, ys)
    plt.xlim(1.35 * semi_axes[0] * np.array([-1, 1]))
    plt.ylim(1.35 * semi_axes[1] * np.array([-1, 1]))
    plt.xlabel('x (m)')
    plt.ylabel('y (m)')


def plot_position(position):
    point_size = 7 ** 2
    plt.scatter(position[0], position[1], point_size)


def plot_sun(apsides):
    focal_length = 0.5 * np.diff(apsides)
    sun_size = 6 * 8 ** 2
    plt.scatter(focal_length, 0, sun_size, c='yellow')


def plot_label_postions(axes):
    angles = [0, np.pi / 2, np.pi, 3 * np.pi / 2]
    labels = ["January", "March", "July", "September"]
    for index in range(len(angles)):
        position = [axes[0] * np.cos(angles[index]), axes[1] * np.sin(angles[index])]
        plot_position(position)
        shift = 0.05 * np.max(np.abs(position))
        plt.text(position[0] + shift, position[1] + shift, labels[index], c='blue', ha='left', va='bottom')


# Simulation parameters
# These are values particular to the simulation
# that do not change later in the script
# rp = apoapsis

# ra = periapsis
# Computed parameters (from simulation parameters)
#	These are values that do not change later in the script
#	and are calculated from formulas using the simulation parameters
# Values: rp = 1 and ra=2 For the np.meantime

# d = distance
# Function calls and simple calculations for:
#	data read-in
#	simulation solution 
#	visualization
# The two points at which the code would read would be aphelion(152,100 km) and Perihelion(147,300 km). Moving in an orbital motion around the sun to find 2
# more points.

# Data read in would be the distances mentioned previosuly.

# Finding c, a, and b in which c^2=sqrt(a^2 + b^2)


# Function definitions for simulation solution & visualization
#	Each function contains help text: https://www.mathworks.com/help/matlab/matlab_prog/add-help-for-your-program.html
# Focal Distance c = (1/2)*(ra - rp)

# semi major axis a = (1/2)*(ra + rp)

# Graph

# url = 'https://nssdc.gsfc.nasa.gov/planetary/factsheet/'; 
# #data = webread(url); https://www.nasa.gov/audience/foreducators/k-4/features/F_Measuring_the_Distance_Student_Pages.html
# whos data


if __name__ == '__main__':
    apsides = np.array(get_apsides())
    axes = calculate_elipse_semi_axes(apsides)
    plot_ellipse(axes)
    plot_sun(apsides)
    plot_label_postions(axes)
    plt.show()
