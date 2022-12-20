Preface: I apologize for turning in this assignment late. I do prioritize and care about the material of this class, but I have had multiple interviews over the last 7 days that gobbled up most of my time. Much like a simple reflex agent, my life adheres to a behavior tree: if interviews return prioritize acquiring a job, else return prioritize AI homework. If you would be kind enough not reduce the assignment grade by 20%, I would be extremely gracious. If you chose too, I understand, I shall survive. <br />
<br />
Readme Content: <br />
The contents of the python file illustrate the class hierarchical node structure of a behavior tree. The blackboard contains the required material. To execute the behavior tree blackboard inputs are required as follows: <br />
&nbsp;&nbsp;- Battery level, Spot Cleaning, and General cleaning must be inputed manually to execute the desired command. If you are interested in modifying the inputs, you simply need to modify the blackboard specifications in the fifth line from the bottom <br />
&nbsp;&nbsp;- Dusty Spots are randomized, and the simple environment used to provide an example includes two tiles A and B<br />

The agent class created is a simple reflex agent: <br />
&nbsp;&nbsp;- The vacuum location is randomly placed on A or B, and this could easily be modified if necessary<br />
<br />
The agent has several sequence nodes and all of these nodes ultimately are subsets of a single priority node. Under the umbrella of each sequence node are multiple tasks nodes, condition nodes, as well as decorator and composite material.<br />
<br />
When executed the behavior tree ultimately outputs either DO NOTHING or DONE GENERAL. Print statements prior to the final output illustrate the path of the simple reflex agent through its behavior tree. # Behavior-Trees
