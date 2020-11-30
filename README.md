# Monty Hall Simulation

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

I was bored. I couldn't sleep. And the reason I couldn't sleep was that I was not satisfied with the answer that "switching to another door will increase your chances" and the existing explanationsy.  

I was one of those 50/50 guys. And I thought I figured it out. So I decided to share my opinion, analysis and results to prove that 50/50 is the right answer and/or make a fool of myself. I did the latter, learnt something and now am just giving another look at the problem and its solution.

## Hypothesis - Choice vs the Illusion of (Second) Choice (IoC)

Since the host opens one of remaining doors, the are two ways of looking at the new situation when the contestant is offered to make the choice again:
* it's a new independent situation, where choice does not take into account the chances of previous situation, and making the chances to win the reward 50/50, if the contestant again randomly decides between the doors (for instance, by flipping a coin)
* it's the same situation as before, but the contestant is playing ahead and is choosing between 1 door and all of the remaining doors, not 1 of 3 doors

The "Keep the same door strategy" says there's a 1/3 chance to win the reward.  
It doesn't matter if host is gonna show you one of the remaining doors.  
It's the same situation if you were only given one choice, just at the beginning of the game and that's it  
Basically, 1/3 is the answer to the following question: "What's the chance for each door to have a reward behind it?"

The "Switching the door strategy" says there's a 2/3 chance to win the reward.  
It doesn't matter if host is gonna show you one of the remaining doors, you'll always switch.  
The 2/3 also indicates the chance that the door you chose initially DOESN'T contain the reward.  
So, in contrast to previous strategy, 2/3 is the answer to the following question: "What's the chance for each door to NOT have a reward behind it?"  
It also indicates the chance that the reward is somewhere in the whole group of remaining doors. So when you switch, you're actually choosing the whole other group of doors, not just one door. It's just that in that group only one door is left closed when you decided to switch and this explanation works when the total number of doors is 3.  

I came up with a term of Illusion of Second Choice, because as far as the computer simulation is concerned, you're not actually making a second new choice in Keep and Switch strategies. You're playing ahead.  

Therefore, I've created more than these two "strategies" in this simulation and specified different definitions of a successful choice.

## Hypothesis - Always Switch or Switch Once?

What happens when the number of doors is increased? According to existing simulation programs and explanations, the chance increases even more if contestant switches choices.  
That means that for N doors, the chance to win the reward by switching is (N-1)/N, meaning pretty close to 100% for large N.  

However, in case of N > 3, there are two ways to opening the remaining doors:  
a) after opening each door, offer contestant another choice  
b) open all doors except the chosen door and one that may or may not have the reward and then offer the contestant the second choice  

That being said, if we stick to 1), the contestant can:  
c) switch the choice each time  
c) keep the choice until there are only 2 doors left  

Keeping the illusion of choice in mind:  
a) is the same as c)  
b) is the same as d)  

In egde case of N = 3, all 4 ways are the same: a, b, c and d

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

There's no IoC in this strategy, since contestant must randomly choose between the remaining doors.
We can't say that the contestant can switch back and forth between two doors, since it's possible for that one of those two doors open during the game.  

The results for Switch Strategy and Reward Door DoS tend to 2/3 chance.  
This is because that in case of using this strategy, the result is not dependent on N, and is actually reverting back to edge case of N = 3.
Further analysis of this strategy will be done in the future.

### Switch Once

Switch Once Strategy *always changes the chosen door, but only when there are two doors remaining*.
The results calculated using this strategy indicate there's a (N-1)/N chance to win.  
*That chance is the same as if the contestant was never given the second choice.*  
And as far as the simulation is "concerned", those two situations are not different.  
Therefore, only the *illusion of choice* is present.  

This strategy differs from Switch strategy for N > 3, but works the same for egde case of N = 3.  

## Definitions of Success

In order to confirm the correlation between chance values, the existence of IoC in some strategies, I had to perceive the goal of the game from different perspective to find the same hidden chance values.  

Therefore, I created 4 DoS:
* CarDoor
* GoatDoor
* InitCarDoor
* InitGoatDoor

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

## Results and Analysis

I ran the simulation for all CSs and DoSs, N=(3,5,10) and G=10^k where k = [3, 5].

The reason why I chose N=(3,5,10) is because of the readable percentages:  
* N = 3,  1/N ~= 0.3, (N-1) ~= 0.6
* N = 5,  1/N = 0.2,  (N-1) = 0.8
* N = 10, 1/N = 0.1,  (N-1) = 0.9

The results are plotted in `outputs/output.pdf`.

An excerpt from the pdf is shown in the image below.

![Excerpt](/outputs/excerpt.PNG)

### Key takeaways:
#### Last Chosen Door - CarDoor and GoatDoor
##### Random CS
50% chance of success in terms of CarDoor DoS.
Actually involves two choices, where the second choice is independent of the previous one.  
The results actually confirm that the chances are 50/50.  
These results do not vary when changing the number of doors.
##### Switch and Switch Once
For the edge case of N = 3, the values are the same, since the strategy is performed in the same way.  
For N > 3 the results differ, but the Switch strategy reverts back to situation where N = 3 in the end.  
##### Keep and Switch Once
The two strategies are complementary.  
Aligns with 1/N vs 2/N theory.  
Shows standard simulation results.
##### Switch
For N > 3 the chance of success is 2/3 in terms of CarDoor DoS.  
Number of doors don't seem to affect the change in values.
#### Initially Chosen Door
1/N chance of success in terms of CarDoor DoS.  
The results are the same regardless of the strategy.  
Takes into account only the first choice.  
##### Relationship with Keep and Switch Once strategy with Car and Goat Door DoSs
The values are the same, relationship is obvious.  
Questions whether the second choice matters - the illusion of choice.  
Because of the IoC, to computer this is the same as if it was asked: "What's the chance of finding the goat on the first try?"  
If there's a high chance of that, if offered to switch contestant would like to avoid the goat.

## Endnote

As I already said in the beginning: I was bored and I couldn't sleep, and I was aware at the time that I might had gone on a fool's errand.
But it had been bugging me for quite a while and I wanted to share the eureka moment when I found the connection between different CSs and DoSs.  
So I'm showing you the code, the data, relations and looks at the same problem from different perspectives.  

In the future, I might add a couple of other CSs and DoSs and calculate the results.  
You are welcome to create issues for me if you have any advice, wishes, observations that might need addressing.  
~~But I think the main goal has been achieved and I've shown that the chance is 50/50, after all. :)~~  
The chance is 50/50, if you randomly choose between the remaining two doors in the second choice.  
When you play ahead, you basically have one choice, and that's between 1/3 or 2/3 chance of winning the door.  
And you should switch. :D

## Additional simulations

I ran additional simulations for G = 10^4 and N = 3 and N = 5 with some different choice strategies used for:
* picking the first door
* repositioning the reward
* opening the doors

In these simulations I only used the CarDoor and GoatDoor DoSs.

### Initial Choice

I've created two new CSs:
* FirstDoor
** shows that the sequence of the doors does not matter
** simulation results are the same as with default init CS - Random
* NoDoor
** gives 1/(N-1) chance for Keep and (N-2)/(N-1) chance for SwitchOnce strategy
** for N = 3, Switch strategy gives 1/2 chance, while for N > 3 it again reverts to N = 3 with default initial CS

![Excerpt](/outputs/initChoiceExcerpt.PNG)

### Repositioning the reward

Alongside the default *RandomClosedOrReward* positioning CS, I've also used *RandomClosed* CS.  
*RandomClosedOrReward* doesn't reposition the reward and it has been used as default opening CS for other simulations. It returns the reward door or a random door if the reward door is not already set.  
*RandomClosed* may reset the reward door after each opening.  
For N = 3 the simulation results are the same between the 2 CSs and prove that if the reward is repositioned each turn, it doesn't affect the chances, since the contestant doesn't know the reward position either way.  
However, for N > 3 it reverts back to N = 3.

![Excerpt](/outputs/positioningExcerpt.PNG)

### Opening the doors

Alongside the default *RandomNonChosenEmptyClosed* opening CS, I've also used *RandomNonChosenClosed* and *RandomClosed* CSs.  
*RandomNonChosenEmptyClosed* lets host open the door with no reward that's not chosen by the contestant.
*RandomNonChosenClosed* lets host open any closed door except the one chosen by the contestant. This means the host can also open the door with reward and therefore the contestant can lose immediately after first try. This CS gives all the cases for CarDoor DoS 1/N chance.
*RandomClosed* lets host open any closed door, regardless whether it has the reward or is chosen by contestant. It gives the same 1/N chance as *RandomNonChosenClosed*.

![Excerpt](/outputs/openingExcerpt.PNG)


## References

https://www.montyhallproblem.com/  
https://statisticsbyjim.com/fun/monty-hall-problem/  
https://betterexplained.com/articles/understanding-the-monty-hall-problem/  
https://brilliant.org/wiki/monty-hall-problem/  
https://en.wikipedia.org/wiki/Monty_Hall_problem  
https://www.mathwarehouse.com/monty-hall-simulation-online/  
