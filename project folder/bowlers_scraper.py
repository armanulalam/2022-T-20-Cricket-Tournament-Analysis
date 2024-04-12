import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()  


url = 'https://stats.espncricinfo.com/ci/engine/records/team/match_results.html?id=14450;type=tournament'
driver.get(url)

# all_rows = soup.select('table.engineTable > tbody > tr.data1')
# links = ["https://www.espncricinfo.com" + row.select('td')[6].find('a')['href'] for row in all_rows]
link_list = []
rows = driver.find_elements(By.CLASS_NAME, 'ds-table')

for idx, row in enumerate(rows):
    match_links = row.find_elements(By.XPATH, '//a[contains(@href, "full-scorecard")]')
    for link in match_links:
        if link.get_attribute('href') not in link_list:
            link_list.append(link.get_attribute('href'))
    
for item in link_list:
        new_url = item
        driver.get(new_url)
        new_rows = driver.find_elements(By.CLASS_NAME, "ci-scorecard-table")


bowling_summary = []
for link in link_list:
    driver.get(link)
    

    match = [div for div in driver.find_elements(By.CSS_SELECTOR,'div') if div.find_element(By.CSS_SELECTOR,'span').text == "Match Details"]
    team1 = match[0].find_next_siblings()[0].find('span').text.replace(" Innings", "")
    team2 = match[0].find_next_siblings()[1].find('span').text.replace(" Innings", "")
    match_info = team1 + ' Vs ' + team2

    tables = driver.find_elements(By.CSS_SELECTOR, 'div > table.ds-table')
    first_inning_rows = [row for row in tables[1].select('tbody > tr') if len(row.find_all("td")) >= 11]
    second_innings_rows = [row for row in tables[3].select('tbody > tr') if len(row.find_all("td")) >= 11]

    for rows, team in zip([first_inning_rows, second_innings_rows], [team2, team1]):
        for row in rows:
            tds = row.find_all('td')
            bowling_summary.append({
                "match": match_info,
                "bowlingTeam": team,
                "bowlerName": tds[0].find('a').text.replace(' ', ''),
                "overs": tds[1].text,
                "maiden": tds[2].text,
                "runs": tds[3].text,
                "wickets": tds[4].text,
                "economy": tds[5].text,
                "0s": tds[6].text,
                "4s": tds[7].text,
                "6s": tds[8].text,
                "wides": tds[9].text,
                "noBalls": tds[10].text
            })

driver.quit()

df = pd.DataFrame(bowling_summary)
df.to_csv('bowlers_summary.csv',index=False)
