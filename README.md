# Homework 4 - Using Python to generate data
For this homework, we are going to use Python tools to run a simulation on an intersection. We will then make a modification and write a final proposal paper for how we would advise changing the intersection.

## Important figures to use:
- Every year it costs $24,000 to maintain a lane-mile of road.
  - A lane-mile is one mile of a lane, so multi-lane road will multiple this figure.
- The cost of building a new lane is between $3 million and $5 million
  - If you add a lane to a road, this is the initial construction cost.
- The cost of a traffic light is initially $250,000 - $500,000 and has an annual cost in maintenance and electricity of $8,000.

## IntersectionSimulator.py
This is a very rough (I wrote it) simulation of an intersection. You will be able to adjust a number of the variables and should have a rough understanding of how the process works.
### Traffic counts
- Pick an intersection in Omaha and look it up in the Omaha_Traffic_Counts.pdf document.
- Input the count for North, South, East, and West traffic.
  - The numbers are cut in half because each car is counted twice.
  - The reason is that the number of people turning can be calculated.
  - Our simulation ignores people turning.

### Number of lanes
- Adjust the number of lanes.
  - If you are using a stop sign, it must be 2 lanes in each direction (EW/NS).
  - Lanes must be an even number.
    - We cannot add an extra South lane without an additional North lane too.

### Traffic control device
- Either a "Light" or a "Sign".
- Lights can have different length lights North-South and East-West.
  - We don't have yellow lights.
  - All the times are in seconds.

### Depart rate
- Once a car gets to the intersection, how long does it take them to leave?
  - This is a bigger issue for stop sign intersections.
  - It should have some value for lights too but the value should be low.

### Output File
- After you run a simulation, your data will be stored as a CSV file.
- You may want to run many simulations and save the data in different files.
- All existing data will be replaced if you use the same data file twice.

### Your data
- After making changes, you should look at the data.
  - Open in Excel
  - Make a graph in Python
  - Examine it in Atom
**What is in the data?**
- Car Number: All cars have a unique number
- Arrive: What time did they arrive - measured in seconds from midnight
- Depart: When did they leave - measured in seconds from midnight
- Wait: Difference in the arrive time and the depart time, measured in seconds.
- Direction: What direction was the car going?
**What am I looking at?**
- Look for failed intersections
  - Do some cars wait for more than 10 minutes at a light?
- Some of this is okay, our simulation is not perfect.
- You can explain some of the outlying data in your report.

## Analyzing your data
Once you've run your simulation or multiple simulations you should do some analysis using other python tools. This analysis should be included in your final report.  
Example analysis:
- Create a graph of the wait time.
- Find the average wait time.
- Find the max wait time.
- Calculate the difference between max traffic and average traffic.

## DataVisualization.py
I used this file to do some analysis of the data I collected. One of the things I did was to group the traffic by hour.
- You might want to group by half-hour or every ten minutes.

## Final Report
Use the data about the cost of building, or maintaining a road to make a justification on why you would change an intersection.
Your final report should include:
- Your recommended change to the intersection
  - Add lanes
  - Reduce lanes
  - Change Control Device
- The data you generated
  - Graphs & charts generated by Python
  - Other data analysis
- The cost/benefit analysis.
  - How much will this cost to build?
  - Will there be any ongoing costs/savings?
  - What is the difference in wait times?
  - What is the value on people's time?
- What are the underlying assumptions of your model?
  - What values did you use for your model?
  - What can our model not fully explore?

The paper should be at least 3 pages in length, including your graphs and sample data. You should also be convincing and methodical with your reasoning.

## Important things I have not discussed
- Intersections are not stand-alone objects
  - Their roads have other intersections
- Traffic is a complex system
  - If one route is too slow, people will choose other routes.
  - Similarly, if a route becomes faster, more people will choose it.
  - Congestion is the principle reason people don't drive at peak hours.
  - Our model has the same number of cars at the intersection.
- This model is complicated but it is not complex.


## Resources
- [Average Percentage of Travel by Hour](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4380130/)
- [Omaha Traffic Counts](https://publicworks.cityofomaha.org/images/October_21_2019.pdf)
- [Cost of road maintenance](https://t4america.org/wp-content/uploads/2019/05/Repair-Priorities-2019.pdf)
- [Cost of building roads](https://blog.midwestind.com/cost-of-building-road/)
- [Cost of traffic lights](https://www.wsdot.wa.gov/Operations/Traffic/signals.htm)

| Hour | US default |
| --- | --- |
| 0 | 0.0081 |
| 1	| 0.0052 |
| 3	| 0.0057 |
| 2	| 0.0047 |
| 5	| 0.0230 |
| 6	| 0.0489 |
| 4	| 0.0099 |
| 7	| 0.0679 |
| 8	| 0.0629 |
| 9 | 0.0531 |
| 10 | 0.0509 |
| 11 | 0.0538 |
| 12 | 0.0560 |
| 13 | 0.0574 |
| 14 | 0.0635 |
| 15 | 0.0733 |
| 16 | 0.0804 |
| 17 | 0.0775 |
| 18 | 0.0579 |
| 19 | 0.0437 |
| 20 | 0.0338 |
| 21 | 0.0280 |
| 22 | 0.0205 |
| 23 | 0.0138 |