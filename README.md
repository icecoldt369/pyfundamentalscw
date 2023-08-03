Basic Voting Rules with respect to the following conditions:

<break><break>
Dictatorship:
An agent is selected, and the winner is the alternative that this agent ranks first. For example, if the preference ordering of the selected agent is , then the winner is alternative
.

 
Plurality:
The winner is the alternative that appears the most times in the first position of the agents' preference orderings. In the case of a tie, use a tie-breaking rule to select a single winner.



Veto:
Every agent assigns 0 points to the alternative that they rank in the last place of their preference orderings, and 1 point to every other alternative. The winner is the alternative with the most number of points. In the case of a tie, use a tie-breaking rule to select a single winner.



Borda:
Every agent assigns a score of to the their least-preferred alternative (the one at the bottom of the preference ranking), a score of to the second least-preferred alternative, ... , and a score of to their favourite alternative. In other words, the alternative ranked at position receives a score of . The winner is the alternative with the highest score. In the case of a tie, use a tie-breaking rule to select a single winner.



Harmonic:
Every agent assigns a score of to the their least-preferred alternative (the one at the bottom of the preference ranking), a score of to the second least-preferred alternative, ... , and a score of to their favourite alternative. In other words, the alternative ranked at position receives a score of . The winner is the alternative with the highest score. In the case of a tie, use a tie-breaking rule to select a single winner.

Single Transferable Vote (STV):
The voting rule works in rounds. In each round, the alternatives that appear the least frequently in the first position of agents' rankings are removed, and the process is repeated. When the final set of alternatives is removed (one or possibly more), then this last set is the set of possible winners. If there are more than one, a tie-breaking rule is used to select a single winner.


Tie-Breaking Rules:
are removed. In the third round,
is removed, and
is the
 We will consider the following three tie-breaking rules. Here, we assume that the alternatives are represented by integers.
max: Among the possible winning alternatives, select the one with the highest number. min: Among the possible winning alternatives, select the one with the lowest number. agent : Among the possible winning alternatives, select the one that agent ranks the highest in his/her preference ordering.
