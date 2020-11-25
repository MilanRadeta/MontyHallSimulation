# Monty Hall Simulation - Fifty Fifty

Just another Monty Hall simulation made in Python.
It supports two existing strategies "Keep the same door" and "Switch to another door".
However, I've also added another strategy which actually resembles the contestant to choose the door again at random.

## What is Monty Hall problem?

You've got 3 doors. One has the reward.
You choose one door. One of the remaining doors is opened and shown there is no reward behind it.
You get the chance to change your answer after that. But does it matter in the end?

"Suppose you're on a game show, and you're given the choice of three doors: Behind one door is a car; behind the others, goats. You pick a door, say No. 1, and the host, who knows what's behind the doors, opens another door, say No. 3, which has a goat. He then says to you, "Do you want to pick door No. 2?" Is it to your advantage to switch your choice?"

For more info, check the references below. Or just Google it.

## Why another Monty Hall simulation?

I was bored.
I couldn't sleep.
And the reason I couldn't sleep was that I was not satisfied with the answer that "switching to another door will increase your chances".
I'm one of those 50-50 guys.
And then, I figured it out... I think.
So I decided to share my opinion and results to prove that 50/50 is the right answer.
That and/or to make a fool of myself.

## Hypothesis/Discussion/Thoughts/Analysis

Since the host opens one of remaining doors, a new independent situation occurs when contestant is offered to make the choice again.
Therefore, during the second choice, he only has two options, thus making the chances to win the reward 50-50.
And I've got the results below with the RANDOM choice strategy to back this up.

The "Keep the same door strategy" makes sense to give 1/3 chance to win the reward.
It doesn't matter if host is gonna show you one of the remaining doors.
It's the same situation if you were only given one choice, just at the beginning of the game and that's it
Basically, 1/3 is the answer to the following question: "What's the chance for each door to have a reward behind it?"

The "Switching the door strategy" makes sense to give 2/3 chance, but not to win the reward.
The 2/3 indicates the chance that the door you chose initially DOESN'T contain the reward.
So, in contrast to previous strategy, 2/3 is the answer to the following question: "What's the chance for each door to NOT have a reward behind it?"
It didn't make sense to me to transport the winning chances from one door to another.

Available online simulations rocked my foundations quite a bit when I saw the results being 1/3 and 2/3.
They really made me question my sanity and knowledge.
But, as I said, then I figured out that the simulations only cover two strategies: ALWAYS Keep and ALWAYS Switch.
They didn't cover SOMETIMES Keep and SOMETIMES Switch.
That said, the results are correct, just not for the question "Will switching increase my chances?".
The question that should be asked for those answers to be correct "What are the chances for one door to hold the reward and what are the chances for one door to NOT hold the reward at the beginning of the game?"
Imagine that the contestant wasn't asked to choose the door that he/she thinks holds the reward, but opposite: "Choose the door that doesn't hold the reward."
Then the results make sense. By always switching the door, you always choose the first door like it doesn't have the reward. And the chance for that actually is 2/3

## Results

I tested the simulation with all three strategies, multiple doors and with different number of simulations.
Below are three data frames (RANDOM, KEEP and SWITCH).
Column headers indicate the number of doors (3, 5, 10).
Row headers indicate the number of simulations/tries.

As you can see, the RANDOM strategy, with greate number of tries, tends to result in 50% chance of winning.
The KEEP strategy is keeping the same chance from the beginning. As I already said, it doesn't matter if contestant is offered another choice if he/she's not going to use it.
The SWITCH strategy is interesting because it keeps the 2/3 chance even with multiple doors. However, the contestant switches each time after a new door opens.

### ChoiceStrategy.RANDOM
            3       5       10
10       50.0%   20.0%   40.0%
100      50.0%   46.0%   51.0%
1000     50.3%   50.5%   53.8%
10000   50.96%  49.91%   49.7%
100000  49.83%  50.18%  49.86%


### ChoiceStrategy.KEEP
            3       5      10
10       20.0%   10.0%  10.0%
100      31.0%   22.0%   8.0%
1000     34.4%   21.0%   9.9%
10000   33.06%  20.36%  9.78%
100000  33.17%  20.06%  9.98%


### ChoiceStrategy.SWITCH
            3       5       10
10       40.0%   60.0%   70.0%
100      77.0%   66.0%   55.0%
1000     67.7%   62.5%   63.7%
10000    66.7%  62.93%  63.01%
100000  66.43%  63.36%  63.08%

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
