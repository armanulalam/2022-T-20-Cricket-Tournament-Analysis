import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()  


driver.get('https://stats.espncricinfo.com/ci/engine/records/team/match_results.html?id=14450;type=tournament')

# all_rows = WebDriverWait(driver, 200).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'table.engineTable > tbody > tr.data1')))
# links = ["https://www.espncricinfo.com" + row.find_element_by_css_selector('td:nth-child(7) a').get_attribute('href') for row in all_rows]
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


batting_summary = []
for link in link_list:
    driver.get(link)

    match = [div for div in driver.find_elements(By.CSS_SELECTOR,'div') if div.find_element(By.CSS_SELECTOR,'span').text == "Match Details"]
    team1 = match[0].find_elements(By.CSS_SELECTOR,'span')[0].text.replace(" Innings", "")
    team2 = match[0].find_elements(By.CSS_SELECTOR,'span')[1].text.replace(" Innings", "")
    match_info = team1 + ' Vs ' + team2

    tables = driver.find_elements_by_css_selector('div > table.ci-scorecard-table')
    first_inning_rows = [row for row in tables[0].find_elements(By.CSS_SELECTOR,'tbody > tr') if len(row.find_elements(By.CSS_SELECTOR,"td")) >= 8]
    second_inning_rows = [row for row in tables[1].find_elements(By.CSS_SELECTOR,'tbody > tr') if len(row.find_elements(By.CSS_SELECTOR,"td")) >= 8]

    for index, row in enumerate(first_inning_rows):
        tds = row.find_elements_by_css_selector('td')
        batting_summary.append({
            "match": match_info,
            "teamInnings": team1,
            "battingPos": index+1,
            "batsmanName": tds[0].find_element(By.CSS_SELECTOR,'a').text.replace(' ', ''),
            "dismissal": tds[1].find_element(By.CSS_SELECTOR,'span').text,
            "runs": tds[2].find_element(By.CSS_SELECTOR,'strong').text, 
            "balls": tds[3].text,
            "4s": tds[5].text,
            "6s": tds[6].text,
            "SR": tds[7].text
        })

    for index, row in enumerate(second_inning_rows):
        tds = row.find_elements(By.CSS_SELECTOR,'td')
        batting_summary.append({
            "match": match_info,
            "teamInnings": team2,
            "battingPos": index+1,
            "batsmanName": tds[0].find_element(By.CSS_SELECTOR,'a').text.replace(' ', ''),
            "dismissal": tds[1].find_element(By.CSS_SELECTOR,'span').text,
            "runs": tds[2].find_element(By.CSS_SELECTOR,'strong').text, 
            "balls": tds[3].text,
            "4s": tds[5].text,
            "6s": tds[6].text,
            "SR": tds[7].text
        })

print(batting_summary)


df = pd.DataFrame(batting_summary)
df.to_csv('batsman_summary.csv',index=False)