## Map with volcanoes andd population information (2005) 

I was playing with folium library.

This is simple script that shows 2 layers on the map:
1. first layer with circles that marks world volcanoes. 
	- Layer can be switched on/off in right corner, like other layers also. Make it active only this layer
	- When you hover over it with the mouse it shows the name
	- When you click on the circle it shows elevation.
	- Colors are showing different elevation between volcanoes.

2. second layer with countries and population.
	- Layer can be switched on/off in right corner.
	- Colors are showing different population between countries.



## Installation

Requires Python 3. I have used 3.8 while making it.

1. Clone the repository (going to a terminal and run `git clone https://github.com/analukic84/volcanoes_and_population_map.git`.
2. Create a virtual environment for the repository
3. Install folium and pandas third libraries
4. When you run an app.py, script will make a file "map_world_volcanoes.html"
4. Run the .html file and enjoy.
