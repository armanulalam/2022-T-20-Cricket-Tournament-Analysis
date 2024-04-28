import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

def get_details(row):
    tds = row.find_elements(By.CSS_SELECTOR, 'td')
    summary = {}
    summary['Batsman Name'] = tds[0].find_element(By.CSS_SELECTOR, 'a').text.strip()
    summary['Runs'] = tds[2].find_element(By.CSS_SELECTOR, 'strong').text.strip()
    summary['Balls'] = tds[3].text.strip()
    summary['4s'] = tds[5].text.strip()
    summary['6s'] = tds[6].text.strip()
    summary['Strike Rates'] = tds[7].text.strip()
    return summary

def main():
    driver = webdriver.Chrome()
    link_list = []

    url = 'https://stats.espncricinfo.com/ci/engine/records/team/match_results.html?id=14450;type=tournament'
    driver.get(url)

    rows = driver.find_elements(By.CLASS_NAME, 'ds-table')
    batting_summary = []

    for idx, row in enumerate(rows):
        match_links = row.find_elements(By.XPATH, './/a[contains(@href, "full-scorecard")]')
        for link in match_links:
            if link.get_attribute('href') not in link_list:
                link_list.append(link.get_attribute('href'))

    for match_url in link_list:
        driver.get(match_url)
        tables = driver.find_elements(By.CSS_SELECTOR, 'div > table.ci-scorecard-table')
        if len(tables) >= 2:
            first_inning_rows = [row for row in tables[0].find_elements(By.CSS_SELECTOR, 'tbody > tr') if len(row.find_elements(By.CSS_SELECTOR, "td")) >= 8]
            second_inning_rows = [row for row in tables[1].find_elements(By.CSS_SELECTOR, 'tbody > tr') if len(row.find_elements(By.CSS_SELECTOR, "td")) >= 8]

            for index, row in enumerate(first_inning_rows):
                batting_summary.append(get_details(row))

            for index, row in enumerate(second_inning_rows):
                batting_summary.append(get_details(row))

    df = pd.DataFrame(data=batting_summary)
    df.to_csv('batsman_summary_updated.csv', index=False)
    driver.quit()

if __name__ == '__main__':
    main()
