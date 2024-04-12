# 2022-T-20-Cricket-Tournament-Analysis

## Problem Statement
The goal of this project is to scrape [this website](https://www.espncricinfo.com/records/tournament/team-match-results/icc-men-s-t20-world-cup-2022-23-14450) to collect the data to analysis 2022 T-20 Cricket World Cup. Then, I used the scraped data to analyze the following question based on the analysis of the Tableau Dashboard:
1. Top 10 batsman of the tournament based on the run scores.
2. Top 10 bowler of the tournament based on the taken wickets.
3. Top 5 batsman of the tournament based on the run scores and taken wickets. 
4. To find out the Player of The Tournament based on the batting and bowling performance including strike rate and economy rate.
5. To find out the best 11 players squad of the tournament based on their performance.

You can look the dashboard at a glance [here](https://public.tableau.com/app/profile/armanul.alam/viz/DataAnalysisProject-T20CricketWorldCup/Dashboard1?publish=yes).

## My interesting findings from the [Dashboard](https://public.tableau.com/app/profile/armanul.alam/viz/DataAnalysisProject-T20CricketWorldCup/Dashboard1?publish=yes)

Top 10 Batsman of the tournament as per my analysis:
1. Virat Kohli 
2. Max O'Dowd
3. Suryakumar Yadav
4. Jos Buttler
5. Kusal Mendis
6. Sikandar Raza
7. Pathum Nissanka
8. Alex Hales
9. Lorcan Tucker
10. Glenn Philips

Top 10 Bowlers of the tournament as per my analysis:
1. Wanindu Hasaranga de Silva
2. Sam Curran
3. Bas de Leede
4. Blessing Muzarabani
5. Shaheen Shah Afridi
6. Shadab Khan
7. Paul Van Meekeren
8. Josh Little
9. Anrich Nortje
10. Sikandar Raza

Top 5 All-rounders of the tournament as per my analysis:
1. Sikandar Raza
2. Hardik Pandya
3. Dhananjaya de Silva
4. Ben Stokes
5. Bas de Leede

Player of the tournament as per my analysis: </br>
Sikandar Raza </br>
Taken Runs - 219 </br>
Strike Rate - 110.5 </br>
Taken Wickets - 10 </br>
Economy - 6.89 </br>

Best 11 players squad based on the performance of the tournament as per my analysis (I consider strike rate and economy rate to choose players as well):
1. Virat Kohli
2. Suryakumar Yadav
3. Kusal Mendis
4. Jos Buttler (c & wk)
5. Glenn Philips
6. Sikandar Raza
7. Hardik Pandya
8. Wanindu Hasaranga de Silva
9. Sam Curran
10. Shaheen Shah Afridi  
11. Shadab Khan

## Build from the source
1. Clone the repo
   ```bash
   git clone https://github.com/armanulalam/2022-T-20-Cricket-Tournament-Analysis.git
   ```
2. Initialize and activate virtual environment
   ```bash
   virtualenv --no-site-packages  venv
   source venv/bin/activate
   ```
3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```


