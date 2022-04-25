%%%% RENAME from mini_project.m to (your_project_short_name).m
% Comments describing mini-project ~ 100-200 words
%This program would be able to calculate the distance between the earth 
%and the sun at 4 different points around the orbital axis as it goes 
%around the sun. It is done by using as input of kepler 3rd law and 
%equation of motion. More specifically finding the distance(m) at 4 
%different seasons within a 1 year span. We already know two positions distance
%and will find a function to help calculate at 2-4 other points. The earth travels
%around the sun in an orbital function. 
% Simulation parameters
%	These are values particular to the simulation 
%	that do not change later in the script
%rp = apoapsis

%ra = periapsis
% Computed parameters (from simulation parameters)
%	These are values that do not change later in the script
%	and are calculated from formulas using the simulation parameters
% Values: rp = 1 and ra=2 For the meantime

%d = distance
% Function calls and simple calculations for:
%	data read-in
%	simulation solution 
%	visualization
%The two points at which the code would read would be aphelion(152,100 km) and Perihelion(147,300 km). Moving in an orbital motion around the sun to find 2 
%more points. 

%Data read in would be the distances mentioned previosuly. 

%Finding c, a, and b in which c^2=sqrt(a^2 + b^2)


% Function definitions for simulation solution & visualization
%	Each function contains help text: https://www.mathworks.com/help/matlab/matlab_prog/add-help-for-your-program.html
%Focal Distance c = (1/2)*(ra - rp)

%semi major axis a = (1/2)*(ra + rp)

%Graph


% 
% url = 'https://nssdc.gsfc.nasa.gov/planetary/factsheet/'; 
% %data = webread(url); https://www.nasa.gov/audience/foreducators/k-4/features/F_Measuring_the_Distance_Student_Pages.html
% whos data

apsides = [152100, 147300].*10^9
axes = calculate_elipse_semi_axes(apsides)
hold on
plot_ellipse(axes)
plot_sun(apsides)
angles = [0,pi/2,pi,3*pi/2]
labels = ["January","March","July","September"]
for index = 1:length(angles)
    position = [axes(1)*cos(angles(index)),axes(2)*sin(angles(index))]
    plot_position(position)
    text(position(1),position(2),labels(index),'fontsize',14)
end
hold off
function semi_axes = calculate_elipse_semi_axes(apsides)
    semi_major_axis = mean(apsides)
    focal_length = 0.5*diff(apsides)
    semi_minor_axis = sqrt(semi_major_axis^2 - focal_length^2)
    semi_axes = [semi_major_axis,semi_minor_axis] 
end 


function ellipse_plot = plot_ellipse(semi_axes)
    thetas = (0:.1:2.*pi);
    xs = semi_axes(1).*cos(thetas);
    ys = semi_axes(2).*sin(thetas);
    plot(xs,ys)
    xlim(1.2*semi_axes(1).*[-1,1])
    ylim(1.2*semi_axes(2).*[-1,1])
    xlabel('x (m)')
    ylabel('y (m)')

end
function scatter_plot = plot_position(position)
    point_size = 7^2
    scatter(position(1),position(2),point_size,'filled')
    
   
end 

function sun = plot_sun(apsides)
     focal_length = 0.5*diff(apsides)
     sun_size = 6*7^2
     scatter(focal_length,0,sun_size,'yellow','filled')
     
end









