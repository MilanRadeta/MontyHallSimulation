# Monty Hall Simulation - Fifty Fifty

Monty Hall simulation made in Python.  
The goal of developing this project is to explore whether the results of the existing simulation programs are wrongly interpreted.  
What's specific about this simulation is that it's using more than just known two choice strategies (Keep Choice and Switch Choice).  
Also, this simulation uses multiple definitions of success, which will help in analysis of similar results between different strategies and definitions.  

## What is the Monty Hall problem?

Contestant's got 3 closed doors. Behind one of them is a reward.  
Contestant's chooses one door. After that one of the remaining doors which certainly doesn't have the reward is opened.  
Contestant is offered to choose again.  
The question is will switching the choice increase the advantage of choosing the door with a reward or is it 50/50 chance?

"Suppose you're on a game show, and you're given the choice of three doors: Behind one door is a car; behind the others, goats. You pick a door, say No. 1, and the host, who knows what's behind the doors, opens another door, say No. 3, which has a goat. He then says to you, "Do you want to pick door No. 2?" Is it to your advantage to switch your choice?"

For more info, check the references below or ask Google.

## Why another Monty Hall simulation?

I was bored. I couldn't sleep. And the reason I couldn't sleep was that I was not satisfied with the answer that "switching to another door will increase your chances". The existing simulation programs are interpreted as that if you keep switching your choice, you'll get the reward in 2/3 of the time.  

I'm one of those 50/50 guys. And I think I figured it out. So I decided to share my opinion, analysis and results to prove that 50/50 is the right answer and/or make a fool of myself.

## Hypothesis - Choice vs The Illusion of Choice

Since the host opens one of remaining doors, a new independent situation occurs when contestant is offered to make the choice again.  
Therefore, during the second choice, he only has two options, thus making the chances to win the reward 50/50.  

The "Keep the same door strategy" makes sense to give 1/3 chance to win the reward.  
It doesn't matter if host is gonna show you one of the remaining doors.  
It's the same situation if you were only given one choice, just at the beginning of the game and that's it  
Basically, 1/3 is the answer to the following question: "What's the chance for each door to have a reward behind it?"

The "Switching the door strategy" makes sense to give 2/3 chance, but not to win the reward.  
The 2/3 indicates the chance that the door you chose initially DOESN'T contain the reward.  
So, in contrast to previous strategy, 2/3 is the answer to the following question: "What's the chance for each door to NOT have a reward behind it?"  

Therefore, I've created more than these two "strategies" in this simulation and specified different definitions of a successful choice.

## Hypothesis - Always Switch or Switch Once?

What happens when the number of doors is increased? According to existing simulation programs and explanations, the chance increases even more if contestant switches choices.  
That means that for N doors, the chance to win the reward by switching is (N-1)/N, meaning pretty close to 100% for large N.  

However, in case of N > 3, there are two ways to opening the remaining doors:
1) after opening each door, offer contestant another choice
2) open all doors except the chosen door and one that may or may not have the reward and then offer the contestant the second choice

That being said, if we stick to 1), the contestant can:
a) switch the choice each time
b) keep the choice until there are only 2 doors left

Keeping the illusion of choice in mind:
* 1) is the same as a)
* 2) is the same as b)

In egde case of N = 3, all 4 ways are the same: 1), 2), a), b).  
But the edge case exists and because of that the existing simulation results might have been misinterpreted.

## Simulation Program - Overview

Simulations are run for each combination of:
* choice strategy (CS)
* total number of doors (N)
* total number of simulation/games (G)

Simulator keeps score of each combination of:
* choice strategy (CS)
* definition of success (DoS).  
* total number of doors (N)
* total number of simulation/games (G)

At the creation of each game, a random door is selected to hold a reward.  
At the start of each game, a random door is selected for the first choice.  
While there are more than 2 closed doors, one of the closed doors is opened, excluding the chosen one.  
After opening each door, a new door is chosen according to the CS.  
At the end of the game, the two remaining doors are opened.  
The Game Result (Success or Failure) is calculated for each DoS.  
Simulator updates the score according to the new Game Results.

For each combination of N and G, a table is printed into the console:  
* columns represent the used CSs.  
* rows represent the used DoSs.  
* cells contain the winning percentage for specific CS and DoS

At the end of simulation program, scores are plotted and saved in a PDF.

## Choice Strategies

There are four choice strategies:
* Random
* Keep
* Switch
* Switch Once

### Random

Random Choice Strategy actually *simulates the contestant's second choice*.  
The door chosen in that moment *may or may not be* the same as the previously chosen door.  
The results calculated using this strategy actually indicate there's a 50% chance to win.  

### Keep

Keep Choice Strategy *never changes the chosen door*.  
The results calculated using this strategy indicate there's a 1/N chance to win.  
*That chance is the same as if the contestant was never given the second choice.*  
And as far as the simulation is "concerned", those two situations are not different.  
Therefore, only the *illusion of choice* is present.

### Switch 

Switch Choice Strategy *always changes the chosen door*.  

In case of N > 3, after opening each door without the reward, contestant switches the doors.  
Therefore, where N is number of all doors and X is number of opened doors, the contestant subsequently chooses one of N-X-1 doors.  
This differs from the first choice, where the contestant can choose any door.  

Like Random Choice Strategy, the next door chosen *may or may not* belong in the group of previously chosen doors.  
Unline Random Choice Strategy and like Switch Once Strategy, the next door must not be the same as the last selected door.  

This strategy differs from Switch Once strategy for N > 3, but works the same for egde case of N = 3.  

There's no illusion of choice in this strategy, since contestant must randomly choose between the remaining doors.
We can't say that the contestant can switch back and forth between two doors, since it's possible for that one of those two doors open during the game.

The results for this strategy are quite unique and I haven't seen them in other simulations. 

#### True Switch results

The results for Switch Strategy and Reward Door DoS tend to 60% chance.  
Don't take my word for it, but I have a theory that that chance can be calculated the following way:  
`( (N-1) / N + (2/N) / N ) / 2`
where (N-1) and 2 are max and min different doors selected during the game, respectively.
I might test this theory later on and post the results.

### Switch Once

Switch Once Strategy *always changes the chosen door, but only when there are two doors remaining*.
The results calculated using this strategy indicate there's a (N-1)/N chance to win.  
*That chance is the same as if the contestant was never given the second choice.*  
And as far as the simulation is "concerned", those two situations are not different.  
Therefore, only the *illusion of choice* is present.  

This strategy differs from Switch strategy for N > 3, but works the same for egde case of N = 3.  

## Definitions of Success

In order to confirm the correlation between chance values, the existence of illusion of choice some strategies, I had to perceive the goal of the game from different perspective to find the same hidden chance values.  

Therefore, I created 4 DoS:
* CarDoor
* GoatDoor
* InitCarDoor
* InitGoatDoor

Some of these DoSs might seem counter-intuitive and illogical, but so do the chances of winning the game by switching the doors.

### Car Door

This is the standard, most intuitive and logical DoS.  
It represents the contestant's wish to choose the door with the reward (car) at the end of the game.  

### Goat Door

This is the opposite of the Reward Door DoS and one of the more counter-intuitive ones.
It represents the contestant's wish to choose the door which doesn't have the reward at the end of the game.
Imagine a contestant which actually wants a goat.

### InitCarDoor

This is similar to Car Door DoS but it only cares for the first chosen door.
It represents the contestant's wish to choose the door with the reward (car) at the beginning of the game, but not at the end.
Imagine a contestant that will be happy to know that he did it right on the first try.
Like InitGoatDoor, the chance for success is the same regardless of the strategy.
The chance for success is the same as if the user only had one choice and wanted to get the car: 1/N
You'll notice in the results there's a link between this DoS and Keep CS.

### InitGoatDoor

This is similar to Goat Door DoS but it only cares for the first chosen door.
It represents the contestant's wish to choose the door which doesn't have the reward at the beginning of the game, but not at the end.
Imagine a contestant that will be happy to know that the first chosen door didn't have the reward.
Like InitCarDoor, the chance for success is the same regardless of the strategy.
The chance for success is the same as if the user only had one choice and wanted to get the goat: (N-1)/N
You'll notice in the results there's a link between this DoS and Switch CS.

## Results

I tested the simulation with all three strategies, multiple doors and with different number of simulations.  
Below are three data frames (RANDOM, KEEP and SWITCH).  
Column headers indicate the number of doors (3, 5, 10).  
Row headers indicate the number of simulations/tries.

As you can see, the RANDOM strategy, with greate number of tries, tends to result in 50% chance of winning.  
The KEEP strategy is keeping the same chance from the beginning. As I already said, it doesn't matter if contestant is offered another choice if he/she's not going to use it.  
The SWITCH strategy is interesting because it keeps the 2/3 chance even with multiple doors. However, the contestant switches each time after a new door opens.

### ChoiceStrategy.RANDOM
<table>
  <tr>
    <td></td>
    <th>3</th>
    <th>5</th>
    <th>10</th>
  </tr>
  <tr>
    <th>10</th><td>50.0%</td><td>20.0%</td><td>40.0%</td>
  </tr>
  <tr>
    <th>100</th><td>50.0%</td><td>46.0%</td><td>51.0%</td>
  </tr>
  <tr>
    <th>1000</th><td> 50.3%</td><td>50.5%</td><td>53.8%</td>
  </tr>
  <tr>
    <th>10000</th><td>50.96%</td><td>49.91%</td><td>49.7%</td>
  </tr>
  <tr>
    <th>100000</th><td>49.83%</td><td>50.18%</td><td>49.86%</td>
  </tr>
</table>


### ChoiceStrategy.KEEP
<table>
  <tr>
    <td></td>
    <th>3</th>
    <th>5</th>
    <th>10</th>
  </tr>
  <tr>
    <th>10     </th><td>  20.0%</td><td>   10.0%</td><td>  10.0%</td>
  </tr>
  <tr>
    <th>100    </th><td>  31.0%</td><td>   22.0%</td><td>   8.0%</td>
  </tr>
  <tr>
    <th>1000   </th><td>  34.4%</td><td>   21.0%</td><td>   9.9%</td>
  </tr>
  <tr>
    <th>10000  </th><td>  33.06%</td><td>  20.36%</td><td>  9.78%</td>
  </tr>
  <tr>
    <th>100000 </th><td>  33.17%</td><td>  20.06%</td><td>  9.98%</td>
  </tr>
</table>

### ChoiceStrategy.SWITCH
<table>
  <tr>
    <td></td>
    <th>3</th>
    <th>5</th>
    <th>10</th>
  </tr>
  <tr>
    <th>10      </th><td> 40.0%  </td><td> 60.0%</td><td>   70.0%</td>
  </tr>
  <tr>
    <th>100     </th><td> 77.0%  </td><td> 
    
    
    
    
    
    .0%</td><td>   55.0%</td>
  </tr>
  <tr>
    <th>1000    </th><td> 67.7%  </td><td> 62.5%</td><td>   63.7%</td>
  </tr>
  <tr>
    <th>10000   </th><td> 66.7%  </td><td>62.93%</td><td>  63.01%</td>
  </tr>
  <tr>
    <th>100000  </th><td>66.43%  </td><td>63.36%</td><td>  63.08%</td>
  </tr>
</table>

## Endnote

As I already said in the beginning: I was bored and I couldn't sleep, so it's quite possible I'm not right.  
But it has been bugging me for quite a while.  
And I wanted to share this Eureka moment.

## References

https://www.montyhallproblem.com/  
https://statisticsbyjim.com/fun/monty-hall-problem/  
https://betterexplained.com/articles/understanding-the-monty-hall-problem/  
https://brilliant.org/wiki/monty-hall-problem/  
https://en.wikipedia.org/wiki/Monty_Hall_problem  
https://www.mathwarehouse.com/monty-hall-simulation-online/  
