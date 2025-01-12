import json
import csv
import logging
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import psycopg2
import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('max_colwidth', None)

logging.basicConfig(level=logging.INFO)


def connect_to_db():
    connection = psycopg2.connect(
        host=os.environ.get("DATABASE_HOST", "localhost"),
        database="movies_db",
        user="postgres",
        password="modric19"
    )
    return connection



def initialize_webdriver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("window-size=1920x1080")
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
    chrome_options.add_argument(f"user-agent={user_agent}")

    driver = webdriver.Chrome(options=chrome_options)
    return driver
def extract_top_movie_links(num=1):
    URL = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
    driver.get(URL)

    wait = WebDriverWait(driver, 30)
    wait.until(EC.presence_of_all_elements_located(
        (By.CSS_SELECTOR, "li.ipc-metadata-list-summary-item a.ipc-title-link-wrapper")))

    links = driver.find_elements(By.CSS_SELECTOR, "li.ipc-metadata-list-summary-item a.ipc-title-link-wrapper")[:num]
    return [link.get_attribute("href") for link in links]


def extract_movie_details(url, driver):
    driver.get(url)

    def extract_multiple_elements(selector):
        try:
            return [el.text for el in driver.find_elements(By.CSS_SELECTOR, selector)]
        except:
            return []

    try:
        title = driver.find_element(By.CSS_SELECTOR, "h1").text
    except:
        title = "N/A"

    try:
        year = driver.find_element(By.CSS_SELECTOR,
                                   "a.ipc-link.ipc-link--baseAlt.ipc-link--inherit-color[href*='releaseinfo']").text
    except:
        year = "N/A"

    try:
        rating_value = driver.find_element(By.CSS_SELECTOR,
                                           "span.ipc-rating-star.ipc-rating-star--base.ipc-rating-star--imdb").text.split()[
            0]
    except:
        rating_value = "N/A"

    genres = extract_multiple_elements(".ipc-chip-list .ipc-chip")
    director = extract_multiple_elements("a.ipc-metadata-list-item__list-content-item[href*='?ref_=tt_ov_dr']")
    writers = extract_multiple_elements("a.ipc-metadata-list-item__list-content-item[href*='?ref_=tt_ov_wr']")
    stars = extract_multiple_elements("a.ipc-metadata-list-item__list-content-item[href*='?ref_=tt_ov_st']")

    return {
        "title": title,
        "year": year,
        "rating": rating_value,
        "genres": genres,
        "director": director,
        "writers": writers,
        "stars": stars
    }

def save_to_json(data, filename="output.json"):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def save_to_csv(data, filename="output.csv"):
    keys = data[0].keys()
    with open(filename, 'w', newline='', encoding='utf-8') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(data)

def check_and_create_table(connection):
    cursor = connection.cursor()
    cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS movies (
            id SERIAL PRIMARY KEY,
            title TEXT,
            year TEXT,
            rating TEXT,
            genres TEXT[],
            director TEXT[],
            writers TEXT[],
            stars TEXT[]
        )
    ''')
    connection.commit()
    cursor.close()


def insert_into_table(connection, movie_data):
    cursor = connection.cursor()

    for movie in movie_data:
        cursor.execute('''
            INSERT INTO movies (title, year, rating, genres, director, writers, stars)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        ''', (movie["title"], movie["year"], movie["rating"], movie["genres"], movie["director"], movie["writers"],
              movie["stars"]))

    connection.commit()
    cursor.close()


def visualize_data_with_pandas(connection):

    df = pd.read_sql('SELECT * FROM movies', connection)
    print(df.head(10))

def take_screenshot(driver, filename="screenshot.png"):
    driver.save_screenshot(filename)


if __name__ == "__main__":
    logging.info("Iniciando WebDriver...")
    driver = initialize_webdriver()
    logging.info("WebDriver iniciado.")

    logging.info("Extraindo links dos filmes...")
    top_movie_links = extract_top_movie_links(2)
    logging.info(f"Links extraídos: {top_movie_links}")

    all_movie_details = []

    for link in top_movie_links:
        logging.info(f"Extraindo detalhes do filme: {link}")
        movie_details = extract_movie_details(link, driver)
        all_movie_details.append(movie_details)
        logging.info(movie_details)

        screenshot_filename = movie_details["title"].replace(" ", "_") + ".png"
        take_screenshot(driver, screenshot_filename)

    save_to_json(all_movie_details, "filmes.json")
    save_to_csv(all_movie_details, "filmes.csv")

    driver.close()

    connection = connect_to_db()
    check_and_create_table(connection)
    insert_into_table(connection, all_movie_details)


    visualize_data_with_pandas(connection)

    connection.close()
    logging.info("Dados inseridos no banco de dados com sucesso!")
