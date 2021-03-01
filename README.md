# The Monty Hall Problem

The Monty Hall Problem is a classic probability puzzle that people often find unintuitive. The basic premise is taken from the game show “Let’s Make a Deal” and the problem get’s its name from the show’s host, Monty Hall. At the end of the show, the grand prize (car) was hidden behind one of three doors. The other two doors concealed much less desirable prizes called “zonks.” For the Monty Hall Problem, the zonks are typically said to be goats. 

![llama, not goat](https://github.com/amitschelen/Monty-Hall/blob/main/2009lmadzonkgoat.jpg?raw=true)

(llama, not a goat.  Photo from Wikipedia: https://en.wikipedia.org/wiki/Let%27s_Make_a_Deal#/media/File:2009lmadzonkgoat.jpg)

## Probabilities
So…three doors…one prize…two zonks.  Contestants first pick one of the three doors. This has a 1/3 probability of concealing the prize. But the twist is that the host then opens one of the other doors. The other door is always a zonk and never the door that was already picked. The contestant is then given the opportunity to stick with their original selection or switch to the remaining unopened door. This is where things get interesting. Many people incorrectly judge the probability associated with switching doors. Some people reason that that the car is behind one of the doors, so there’s a 50/50 chance either way so it doesn’t matter. Some people think that it’s still a 1/3 probability that the car is behind either door. But neither of these are correct.

The correct answer is that the contestant should always switch because the probability of getting the car by switching is actually 2/3. So a contestant would double their chance of winning by switching. Why? Here’s a link to a video that explains it better than I can. https://www.youtube.com/watch?v=mhlc7peGlGg  But the gist is that if a goat was originally selected (which would happen 2/3 of the time), then the door the host opened was definitely a goat. So if the contestant switches in that situation, they will definitely switch to the car. That means if you pick a goat first, you’ll always get the car by switching. And that happens 2/3 of the time.

I was curious how the Monty Hall problem worked with more than three doors. It seemed easiest to run through it with python and see what happened. While I was at it, I made a functional version of the game. In the game, players have the option to switch or not. But in the model, the door is always switched since that is the probability I wanted to explore. Is the probability of winning by switching always twice as high? I didn't think so. Or maybe it isn't affect with more than three doors since the wrinkle of being guaranteed to swich to the car when you initially pick a goat is unique to three doors? That didn't seem right either. It seems like opening a door should always do *something*.

## Results
For **n** doors, the probability of getting the prize without switching is easy. That's just **1/n**. The results of the model show that the formula for getting the prize by switching is always **(n-1)/n(n-2)**. I interpret this as the product of two events; First you pick a door with a zonk (if you pick the car first then switch, you definitely lose) which has **(n-1)/n** probability (**n-1** zonks out of **n** doors). Then you switch to the car and that has **1/(n-2)** probability (**1** car out of the **n-2** remaining available doors). This gives the following probabilities of winning the car for 3, 4, and 5 doors. Explore the model to find probabilities for more doors.

3 doors - Don’t switch:   1/3   Switch:   2/3

4 doors – Don’t switch:   1/4   Switch:   3/8

5 doors – Don’t switch:   1/5   Switch:   4/15
