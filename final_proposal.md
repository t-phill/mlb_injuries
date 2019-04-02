# Final Proposal

**Purpose**: Begin to organize actual capstone project.

**Format**: Since you will want a public repo at the end of the project, you should create a git repo, 
and your project proposal will be the README.md file in it.

**Length**: Each of the numbered points should have at a few complete sentences to address them. 

**Include the following**:

1. What are you trying to do?  Articulate your objectives using absolutely no jargon (i.e. as if
you were explaining to a salesperson, executive, or recruiter).

Similar to traditional forms of mechanical failure, I am attempting to predict injuries in Major League Baseball(MLB)
pitchers. While the introduction of the human element makes the problem more difficult, I believe there will be signals
in the data which can be modeled. 

Specifically I'll be looking at statcast data, spin rates, arm location, days of rest, etc.,  on a pitch-by-pitch, game-by-game basis. 

2. How has this problem been solved before? If you feel like you are addressing a novel
issue, what similar problems have been solved, and how are you borrowing from those?

I don't believe the problem of injuries or mechanical failure can be fully solved or predicted. Attempts are made in industries such as manufacturing and oil/gas where you are dealing with mechanical products and physical systems.  Unfortunately, no two people are the same or created in the same factory. No pitcher or person has a good estimate for how many times they've thrown a ball in their lifetime.

Although the issue has been previously addressed, there can always be improvements in order to help prevent costly injuries. Without question, there are ongoing efforts to predict injuries within every MLB organization/front office.   

3. What is new about your approach, why do you think it will be successful?

Part of the approach I plan to take is examining play-by-play and game-by-game statcast data. While seemingly unexciting, publicly
available injury prediction projects often include a season-by-season perspective. 

Additionally, the transition from pitchF/x to statcast marks a change in not only the way baseball data is recorded but also
the data itself. Most injury analytics projects utilized pitchF/x data (2006 to ~2017 in some places).

I think I will have success looking at statcast xyz positional data and release points. From there I'll attempt to draw conclusions about pitching mechanics and meaningful changes in mechanics on a pitch-by-pitch basis could signify injury, tightness, or tiredness. 

4. Who cares?  If you're successful, what will the impact be?

Players care. No player wants to get injured, an event usually preceding unfavorable trades, lower value contracts/extensions,
painful rehabilitation, and time away from the sport. 

Teams care. According to initial data exploration, the amount of money paid to injured pitchers while on the disabled list during the 2018 season is $371,849,373. This is a nontrivial amount of money paid by MLB teams to players that are unable to play. 

Additionally, if a team is able to predict that a player is close to potential injury, they would intervene with extra rest
or other preventative measures or ultimately trade the pitcher before their status as an uninjured player changes. 

It is standard procedure to require players to pass a physical examination with team doctors before a trade is finalized. To summarize, it's an intense and microscopic process that teams and players take very seriously. 

5. How will you present your work?  
  * Web app - where will you host it, what kind of information will you present?
  * Visualization - what final visuals are you aiming to produce?
  * Presentation - slides, interpretive dance?

  I plan to host the finished product hosted in a web app. It should be interactive where a player/team could input certain stats or situations and get a prediction or rating of injury risk. Potentially a recommendation wether to intervene or not. 

6. What are your data sources? What is the size of your dataset, and what is your storage format?

Data sources are StatCast data, brooks baseball, baseball-reference, spottrac. There is a large amount of data, mostly clean, readily available. 


7. What are potential problems with your capstone, and what have you done to mitigate these problems?

One potential issue is class imbalance. There were ~799 pitchers that pitched in the MLB in the 2018 season and ~300 pitchers that spent time on the disabled list. I'll address this issue with various sampling techniques. 

Regarding statcast data and release points, it may be difficult to differentiate changes in pitching mechanics due to coaching or personal adjustments from those that are appearing due to injury or fatigue. 

Additionally, injury details aren't always disclosed or are specifically pitching related. I'll attempt to examine roster/disabled list manipulation to make sure I'm not labeling a pitcher as injured when they were only placed on the DL in order to free up a roster spot. 

8. What is the next thing you need to work on?
  * Getting the data, not just some, likely all?
  * Understanding the data?
  * Building a minimum viable product?
  * Gauging how much signal might be in the data?


I need to examine pitch-by-pitch data for the 2018 season to see how large the dataset is. I need to collect game summary statistics for each pitcher in each appearance during the 2018 season so I can create a 'days of rest' feature. I'll need to determine if the project needs to be done through AWS. 

**Submission**: Once you are satisfied with your submission, push it to github, and send the repo URL to your
instructors via slack.
