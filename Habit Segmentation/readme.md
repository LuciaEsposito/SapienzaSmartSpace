## Prerequisites
- Install ProM process mining tool (https://www.promtools.org/doku.php?id=gettingstarted:installation)

- Python v3.7+

## Description
The code used in this project is divided in three folders:
- **segmentation**:
  - contains the file _temporal_segmentation.py_ that is used to divide the input event log in intervals of 15 minutes; it creates a new folder "minutes" in which it generates all
    the 96 csv files, each one representing a temporal interval of 15 minutes and named accordingly to the specific time interval; for example, a file named "00_00-00_15.csv"
    contains all events of the input log which start and end in the time slot between 00:00:00 and 00:15:00.
- **discretization algorithm**: 
contains the code to run the actual discretization algorithm; the two files _ProM_CLI.bat_, and _script_inductive_miner.txt_ are used to run ProM tools from command line interface
(CLI), so they are automatically used by _discretization_algorithm.py_.
  - _ProM_CLI.bat_ is the batch running ProM, to which the _discretization_algorithm.py_ code passes the script to execute (_script_inductive_miner.txt_), and two other parameters that are used by the script;
  - _script_inductive_miner.txt_ is written in a Java-like language; it takes in input a csv file, converts it into a xes file, extracts the correspondent Petri net model by calling
  the Inductive Miner process discovery algorithm, and returns the value of structuredness and the number of arcs and nodes of the obtained Petri net;
  - _discretization_algorithm.py_ contains the actual bottom-up discretization algorithm to obtain the final habits; for each csv file interval that is in the folder "minutes",
  it merges this file with its successive one (the last interval in the folder is merged with the first one), and for each merged file, it computes the "structuredness" and
  "simplicity" by calling _ProM_CLI.bat_; we define the minimun number of discretized intervals that we want in the output and the maximum threshold to decide if it is more
  convenient to merge intervals or to stop; the resulting discretized intervals are the files remaining, at the end of the algorithm, inside the folder "minutes", and each one
  represents a habit. 
- **activities**:
contains many files to actually make a comparison between the habits that we found with the discretization algorithm and the activities that have been already labeled in our
original dataset. 
  - _heat_map_mapping.py_ and _heat_map_generate.py_ are used to generate the heat map of the activities, considering the number of times each activity occurs in a specific
  temporal slot of 15 minutes;
  - _activities.py_ is used to generate a csv file containing all events in the event log that are associated to a specific activity;
  - _activities_more_frequent_interval.py_ is used to find which are the temporal intervals in which an activity occurs more frequently, i.e., the ones in which the
  activity occurs a number of times higher than a fixed threshold;
  - _activities_habit_mapping.py_ is used to extract the habit events that are related to a specific activity.


## How to run
1. Run _temporal_segmentation.py_ to segment the input event log into 96 intervals of 15 minutes; the segmented csv files will be stored in the new directory "minutes"
2. Run _discretization_algorithm.py_ to obtain the resulting habits intervals in the directory "minutes"
3. To analyze the resulting habits intervals:
	 1. run _heat_map_mapping.py_ to create arrays mapping each activity to the 15-minutes intervals in which it occurs
	 2. run _heat_map_generate.py_ to generate the heat map, using the arrays obtained from the previous code
	 3. for each activity that is labeled in the dataset, run _activities.py_ to generate a csv file containing all events of the input event log that are associated to that activity
	 4. run _activities_more_frequent_interval.py_ to determine the temporal intervals in which an activity occurs more frequently
	 5. for each habit found with the discretization algorithm, run _activities_habit_mapping.py_ to filter the habit on each activity and check the number of events that they
	 have  in common; then we can mine the obtained log to compare the Petri net of the habit containing only a specific activity, with the Petri net of the habit itself and check
   if in the Petri net of the habit we can recognize a specific occurrance of an activity; we can also directly use the output percentages to check how many events of the habits
   represent a specific occurrance of an activity
