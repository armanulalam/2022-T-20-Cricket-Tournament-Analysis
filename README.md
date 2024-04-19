# 2022-T-20-Cricket-Tournament-Analysis

## Problem Statement
The goal of this project is to scrape [this website](https://www.espncricinfo.com/records/tournament/team-match-results/icc-men-s-t20-world-cup-2022-23-14450) to collect the data to analysis 2022 T-20 Cricket World Cup. Then, I used the scraped data to analyze the following question based on the analysis of the Tableau Dashboard:
1. Top 10 batsman of the tournament based on the run scores.
2. Top 10 bowler of the tournament based on the taken wickets.
3. Top 5 batsman of the tournament based on the run scores and taken wickets. 
4. To find out the Player of The Tournament based on the batting and bowling performance including strike rate and economy rate.
5. To find out the best 11 players squad of the tournament based on their performance.

You can look the dashboard at a glance [here](https://public.tableau.com/app/profile/armanul.alam/viz/DataAnalysisTableauProject/Dashboard1?publish=yes).

## My interesting findings from the [Dashboard](https://public.tableau.com/app/profile/armanul.alam/viz/DataAnalysisTableauProject/Dashboard1?publish=yes)

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

Top 10 Sixers:
1. Sikandar Raza (11)
2. Kusal Mendis (10)
3. Alex Hales (10)
4. Suryakumar Yadav (9)
5. Rilee Rossouw (9)
6. Marcus Stoinis (9)
7. Andy Balbirnie (9)
8. Virat Kohli (8)
9. Pathum Nissanka (8)
10. Max O'Dowd (8)

Top 10 Four takers:
1. Suryakumar Yadav (26)
2. Virat Kohli (25)
3. Jos Buttler (24)
4. Max O'Dowd (22)
5. Najmul Hossain Shanto (20)
6. Lorcan Tucker (19)
7. Glenn Phillips (19)
8. Alex Hales (19)
9. Kusal Mendis (17)
10. Sikandar Raza (16)

Top 10 Hard-hitter Batsman: (I considered Strike Rates and those batsman who faced at least 30 balls in the tournament)
1. Suryakumar Yadav (182.6)
2. Glenn Maxwell (161.2)
3. Marcus Stoinis (159.2)
4. Mohammad Haris (152.2)
5. Dawid Malan (151.5)
6. Finn Allen (150.5)
7. Glenn Phillips (143.7)
8. Rahmanullah Gurbaz (134.7)
9. Litton Das (131.1)
10. Gareth Delany (131.0)

Best Maiden taker bowler:
Bhuvneshwar Kumar<\br>
3 Overs maiden

Top 10 Death Over Bowlers: (I considered lowest Avg. Economy bowlers and those who did at least 10 overs in the tournament)
1. Jason Holder (4.67)
2. Zahoor Khan (4.75)
3. Bernard Scholtz (5.083)
4. Anrich Nortje (5.27)
5. Mustafizur Rahman (5.60)
6. Mark Watt (5.83)
7. Sean Williams (6.093)
8. Shaheen Shah Afridi (6.094)
9. AdilRashid (6.125)
10. Naseem Shah (6.19)

Top 10 6s consumed Bowlers:
1. Wanindu Hasaranga (8)
2. Ravichandran Ashwin (8)
3. Maheesh Theekshana (8)
4. Richard Ngarava (7)
5. Logan van Beek (7)
6. Barry McCarthy (7)
7. Kagiso Rabada (6)
8. Josh Hazlewood (6)
9. Gareth Delany (6)
10. Chris Woakes (6)

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
4. Run the batsmans_scraper.py and bowlers_scraper.py to scrape the necessary data from the website or Download the two files named bowler_summary_updated.csv and batsman_summary_updated.csv
   ```bash
   python batsmans_scraper.py
   ```
   ```bash
   python bowlers_scraper.py
   ```
5. Run 2022 T-20 Cricket Data Analysis.ipynb file in jupyter notebook to preprocess,manipulate and transform the dataset.
6. You will get the two new csv files named new_batsman_updated_summary.csv and new_bowler_updated_summary.csv
7. Analysis the data through Tableau Public Dashboard based on the new_batsman_updated_summary.csv and new_bowler_updated_summary.csv


