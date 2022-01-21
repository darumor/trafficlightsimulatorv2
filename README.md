# Traffic Lights Simulator - README

    https://github.com/darumor/trafficlightsimulatorv2

## General
This is a side project on which I've worked on and off for a couple of years now. The idea was to create 
a simple traffic lights simulator for fun and to learn some python and maybe create a nice animation of it.
Even an IoT version that would control real life (toy) lights was among the ideas. The underlying idea was to
investigate, how a traffic lights controller works and could it be optimized.

Along the way things changed, and I may have created a monster. 

## Discoveries
As I have worked on this project I have had to come up solutions for various problems
* How to describe a crossing to a computer programme?
  * This solution uses a directed graph that describes the possible routes 
* What is it, that we should optimize?
  * This solution tries to maximize total throughput and minimize total waiting time
  * Other thing to consider are minimizing and equalizing individual waiting time and preventing starvation
* How to make decision on which lights should be green and which should be red?
  * The traffic lights controller makes the decision based on single comparable value per light which is determined by non-linear
regression model getting input information from sensors around the graph describing the crossing
  * sensors may provide information e.g. about waiting times at red lights and line lengths at various spots 
* How to get sample data for building the regression model?
  * For input, I created a traffic generator that creates random traffic
  * For output, I can use the simulator itself to get the values I want to optimize
* How to optimize the regression models coefficients automatically?
  * I built a genetic algorithm that starts with random coefficients and a number of variations to create models.
  * The models are analyzed and the best solutions are selected for cross breeding to create next generations
  * This is repeated over multiple generations with a small possibility of mutations in the models
* What if I already have datasets for traffic and model coefficients?
  * I created providers that can read input data from files and save generated random data sets in files
* How should the traffic be moved along the graph?
  * The path for individual cars is determined by a pathfinder algorithm, based on the entry and exit nodes of the car
* What kind of signals should the sensors provide and how they should be updated?
  * Signal can be anything, but the sensor has to know how to determine one's value
* What kind of traffic should be taken into account?
  * The MVP solution only handles basic cars
* What if there are many crossings?
  * They can all be described in a single graph file
* How to simulate cars, lines, and traffic movement?
* What and how to visualize the process?
  

## Todo
* moving the cars around according to the lights
  * green light nodes tell the first cars in their lines to move on.
* updating sensor values
  * each sensor type determines its values according to the nodes they are connected
  * one node has only one sensor that may expose a signal of various length
* visualization
  * thinking of using pyplot to plot
  * the comparator values of lights
  * line lengths
  * waiting times
* pulling strings together
  * lots of parts
  * not all responsibilities are clear

  
## Random thoughts
* Crossings and traffic lights are no trivial problems