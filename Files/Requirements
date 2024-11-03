Complete
A.  Develop a hash table, without using any additional libraries or classes, that has an insertion function that takes the package ID as input and inserts each of the following data components into the hash table:
•   delivery address, delivery deadline, delivery city, delivery zip code, package weight, delivery status (i.e., at the hub, en route, or delivered), including the delivery time

Complete
B.  Develop a look-up function that takes the package ID as input and returns each of the following corresponding data components:
delivery address, delivery deadline, delivery city, delivery zip code, package weight, delivery status (i.e., at the hub, en route, or delivered), including the delivery time

Complete
C.  Write an original program that will deliver all packages and meet all requirements using the attached supporting documents “Salt Lake City Downtown Map,” “WGUPS Distance Table,” and “WGUPS Package File.”
1.  Create an identifying comment within the first line of a file named “main.py” that includes your student ID.
2.  Include comments in your code to explain both the process and the flow of the program.
Complete
D.  Provide an intuitive interface for the user to view the delivery status (including the delivery time) of any package at any time and the total mileage traveled by all trucks. (The delivery status should report the package as at the hub, en route, or delivered. Delivery status must include the time.)
1. Provide screenshots to show the status of all packages loaded onto each truck at a time between 8:35 a.m. and 9:25 a.m.
Screenshot 1
2.  Provide screenshots to show the status of all packages loaded onto each truck at a time between 9:35 a.m. and 10:25 a.m.
Screenshot 2
3.  Provide screenshots to show the status of all packages loaded onto each truck at a time between 12:03 p.m. and 1:12 p.m.
Screenshot 3
E.  Provide screenshots showing successful completion of the code that includes the total mileage traveled by all trucks.
Screenshot 4

Complete
F.  Justify the package delivery algorithm used in the solution as written in the original program by doing the following:
1.  Describe two or more strengths of the algorithm used in the solution.
Simplicity and efficiency - The nearest neighbor algorithm is pretty easy to understand and implement, it always goes to the nearest destination that has not been visited yet.
Since the truck is always moving to the closest location, the travel time and mileage are minimized.

2.  Verify that the algorithm used in the solution meets all requirements in the scenario.
Packages are all delivered on time, keeping in mind deadlines, and my trucks are utilized with the constraint of only having two drivers. Additionally, the total mileage is kept under 140 Miles.

3.  Identify two other named algorithms that are different from the algorithm implemented in the solution and would meet all requirements in the scenario.
Another algorithm that would do very well in this scenario would be A Star, this algorithm guarantees the shortest path possible, so when it is applied to delivery, it will ensure maximum efficiency.
Nearest insertion would also be a very strong solution for this particular problem, as the route is planned as a whole, rather than just package by package.

a.  Describe how both algorithms identified in part F3 are different from the algorithm used in the solution.
Nearest insertion builds out an entire route for the packages before the truck would leave the hub, and this would likely allow for a shorter overall trip.
Similar to nearest insertion, A Star plans for the entire route, it looks for the shortest possible path considering all of the data it is provided.

Complete
G.  Describe what you would do differently, other than the two algorithms identified in part F3, if you did this project again, including details of the modifications that would be made.
If I were to do this project again, I would attempt automating what packages go on which trucks, and optimize for clusters of packages. I think even with my current algorithm that would significantly decrease overall mileage.
The way I have it currently set up is mostly random, aside from what packages specifically need to be together/delivered at certain times, so I would attempt to make use of my algorithm to determine what groups of packages are in the smallest clusters,
and then assign accordingly.

Complete
H.  Verify that the data structure used in the solution meets all requirements in the scenario.
1.  Identify two other data structures that could meet the same requirements in the scenario.
A self balancing binary search tree would be a good solution
A Graph data structure could also be great for this application.
a.  Describe how each data structure identified in H1 is different from the data structure used in the solution.
In a binary search tree you have slower lookup times, because you aren't using a key to pull something directly from the data structure, you have to go through it and find it. However because stuff is ordered you can easily go through ranges, which is not the case for hash tables.
I think with the right algorithm, such as A Star, a Graph data structure would do exceptionally well here, because they can represent the connections between addresses with their edges and allow for efficient updates mid route
