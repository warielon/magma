# Traveling salesman problem

Given ![LaTeX: n](https://common.informs.org/cgi-bin/mathtex.cgi?n) points and a cost matrix, ![LaTeX: [c_{ij}],](https://common.informs.org/cgi-bin/mathtex.cgi?%5Bc_%7Bij%7D%5D%2C) a *tour* is a permutation of the ![LaTeX: n](https://common.informs.org/cgi-bin/mathtex.cgi?n) points. The points can be cities, and the permutation the visitation of each city exactly once, then returning to the first city (called *home*). The cost of a tour, ![LaTeX: <i_1, i_2, \dots, i_{n-1}, i_n, i_1>,](https://common.informs.org/cgi-bin/mathtex.cgi?%3Ci_1%2C%20i_2%2C%20%5Cdots%2C%20i_%7Bn-1%7D%2C%20i_n%2C%20i_1%3E%2C) is the sum of its costs:

![LaTeX: 
c_{i_1 i_2} + c_{i_2 i_3} + \dots + c_{i_{n-1} i_n} + c_{i_n i_1},](https://common.informs.org/cgi-bin/mathtex.cgi?%0Ac_%7Bi_1%20i_2%7D%20%2B%20c_%7Bi_2%20i_3%7D%20%2B%20%5Cdots%20%2B%20c_%7Bi_%7Bn-1%7D%20i_n%7D%20%2B%20c_%7Bi_n%20i_1%7D%2C%0A)

where ![LaTeX: (i_1, i_2, \dots, i_n)](https://common.informs.org/cgi-bin/mathtex.cgi?%28i_1%2C%20i_2%2C%20%5Cdots%2C%20i_n%29) is a permutation of ![LaTeX: \{1,\dots,n\}.](https://common.informs.org/cgi-bin/mathtex.cgi?%5C%7B1%2C%5Cdots%2Cn%5C%7D.) The TSP is to find a tour of minimum total cost. The two common [integer programming](http://glossary.computing.society.informs.org/ver2/mpgwiki/index.php?title=Traveling_salesman_problem&1=Integer_program "http://glossary.computing.society.informs.org/ver2/mpgwiki/index.php?title=Traveling_salesman_problem&1=Integer_program") formulations are:

ILP: ![LaTeX: \min \left\{ \sum_{ij} c_{ij} x_{ij} : x \in P, \, x_ij \in \{0, 1\} \right\}](https://common.informs.org/cgi-bin/mathtex.cgi?%5Cmin%20%5Cleft%5C%7B%20%5Csum_%7Bij%7D%20c_%7Bij%7D%20x_%7Bij%7D%20%3A%20x%20%5Cin%20P%2C%20%5C%2C%20x_ij%20%5Cin%20%5C%7B0%2C%201%5C%7D%20%5Cright%5C%7D)

*Subtour elimination constraints:* ![LaTeX: \sum_{i,j \in V} x_{ij} \le |V| - 1 \mbox{ for } \empty \ne V \subset \{1, \dots , n \} (V \ne \{ 1, \dots, n \} ),](https://common.informs.org/cgi-bin/mathtex.cgi?%5Csum_%7Bi%2Cj%20%5Cin%20V%7D%20x_%7Bij%7D%20%5Cle%20%7CV%7C%20-%201%20%5Cmbox%7B%20for%20%7D%20%5Cempty%20%5Cne%20V%20%5Csubset%20%5C%7B1%2C%20%5Cdots%20%2C%20n%20%5C%7D%20%28V%20%5Cne%20%5C%7B%201%2C%20%5Cdots%2C%20n%20%5C%7D%20%29%2C)

where ![LaTeX: 
x_{ij} = \begin{cases}
1 & \mbox{ if city } j \mbox{ follows city } i \mbox{ in the tour} \\
0 & \mbox{ otherwise}
\end{cases}](https://common.informs.org/cgi-bin/mathtex.cgi?%0Ax_%7Bij%7D%20%3D%20%5Cbegin%7Bcases%7D%0A1%20%26%20%5Cmbox%7B%20if%20city%20%7D%20j%20%5Cmbox%7B%20follows%20city%20%7D%20i%20%5Cmbox%7B%20in%20the%20tour%7D%20%5C%5C%0A0%20%26%20%5Cmbox%7B%20otherwise%7D%0A%5Cend%7Bcases%7D%0A)

[QAP](http://glossary.computing.society.informs.org/ver2/mpgwiki/index.php?title=Traveling_salesman_problem&1=Assignment_problem "http://glossary.computing.society.informs.org/ver2/mpgwiki/index.php?title=Traveling_salesman_problem&1=Assignment_problem"): ![LaTeX: 
\min \left\{ \sum_{ij} c_{ij} \left( \sum_{k=1}^{n-1} x_{ik} x_{j \, k+1} + x_{i n} x_{j 1} \right) : x \in P, \, x_{i j} \in \{0 , 1\}
\right\} ,](https://common.informs.org/cgi-bin/mathtex.cgi?%0A%5Cmin%20%5Cleft%5C%7B%20%5Csum_%7Bij%7D%20c_%7Bij%7D%20%5Cleft%28%20%5Csum_%7Bk%3D1%7D%5E%7Bn-1%7D%20x_%7Bik%7D%20x_%7Bj%20%5C%2C%20k%2B1%7D%20%2B%20x_%7Bi%20n%7D%20x_%7Bj%201%7D%20%5Cright%29%20%3A%20x%20%5Cin%20P%2C%20%5C%2C%20x_%7Bi%20j%7D%20%5Cin%20%5C%7B0%20%2C%201%5C%7D%0A%5Cright%5C%7D%20%2C%0A)

where ![LaTeX: 
x_{(i, j)} = \begin{cases}
1 & \mbox{ if city } j \mbox{ follows city } i \mbox{ in the tour} \\
0 & \mbox{ otherwise}
\end{cases}](https://common.informs.org/cgi-bin/mathtex.cgi?%0Ax_%7B%28i%2C%20j%29%7D%20%3D%20%5Cbegin%7Bcases%7D%0A1%20%26%20%5Cmbox%7B%20if%20city%20%7D%20j%20%5Cmbox%7B%20follows%20city%20%7D%20i%20%5Cmbox%7B%20in%20the%20tour%7D%20%5C%5C%0A0%20%26%20%5Cmbox%7B%20otherwise%7D%0A%5Cend%7Bcases%7D%0A)

In each formulation, ![LaTeX: P](https://common.informs.org/cgi-bin/mathtex.cgi?P) is the [assignment polytope](http://glossary.computing.society.informs.org/ver2/mpgwiki/index.php?title=Traveling_salesman_problem&1=Assignment_polytope "http://glossary.computing.society.informs.org/ver2/mpgwiki/index.php?title=Traveling_salesman_problem&1=Assignment_polytope"). The *subtour elimination constraints* in ILP eliminate assignments that create cycles, such as shown in the following figure:
