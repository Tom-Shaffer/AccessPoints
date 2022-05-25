# AccessPoints
Given a 2D boolean matrix of connections, which dictates a list of access points, this program calculates the minimum number of connections necessary 
to connect all access points. The indexes of the matrix demonstrate a valid connection. I.E. if [0][1] is True, and [1][0] is True, 
then we know that access point 1 and access point 0 are connected. If [2][2] is true as well, then access point 1 and 0 are connected, 
and 2 is alone, therefore 1 connection is necessary to connect all access points.

This project comes with unit tests to get the 2 main scenarios, when there are no connections necessary and when some are necessary to complete the network.
