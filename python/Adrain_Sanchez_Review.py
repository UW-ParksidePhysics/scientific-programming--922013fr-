# Initial velocity (v0) = 2 m/s
# Initial height   (h0) = 5 m
# Gravity          (g)  = 9.81 m/s
# Height of pulley (H)  = 10 m
# Radius of pulley (R)  = 1 m
# Length of rope   (L)  = 15 m
# Masses           (m1) = 2 kg
#                  (m2) = 5 kg

from numpy import *
from matplotlib import *
import matplotlib.pyplot as plt

m1 = 2
m2 = 5
g = -9.81
v0 = 2
a = ((m2 - m1) * g) / (m1 + m2)
t = linspace(0, 10)


def height(time):
    h = v0 * time + 0.5 * a * time ** 2
    return h


heights = height(t)
print(heights)

plt.plot(t, heights)

% Does the code run without error? If any error occurs, can you suggest a potential fix?
% The code runs without any error when tested on Matlab. 
% How understandable is the output of the code? Point out any parts you do not understand.
% I am not fully understanding the code because there is no description in the .py file but based on the output of 
the code it looks like they are trying to plot time vs height. 
% How readable is the code itself? Say where formatting or commenting would make the code more readable
% The formatting and code itself is readable and is well organized. 
% How clearly do the code comments describe the problem it is trying to solve? Identify places that would benefit from a clearer comment.
% Very good parameters are labeled and organized. Improved  
% How clearly do the variable names relate to the concepts they concretize? Point out any variables you don't recognize, and/or suggest better names.
% All variable names seem to have very good labeling and understanding as to what they are and especially since they 
are common variables like m for mass, v for velocity, and g for gravity. 
% How well does the range of variables capture the problem described? Identify extraneous regions that could be left out or important 
regions that should be included.
% Important regions that should be included should be a good description of what the code is actually doing in regards to a 
pulley being involved. Something that was left out was the computed parameters if there is any in sense of potentially maximum
weight or gravity being 9.8 since gravity is gravity. 
% How clearly do the visualizations show the solutions to the problem? Say if there is extraneous whitespace or the co-domain 
or domain of the data should be changed or any other ways the visualizations could be more effective
% The visualizations are pretty clear in regards to showing the solution to the problem.
