import undetected_chromedriver as uc
from bs4 import BeautifulSoup
import io
import sqlite3

def create_table(conn):
    """Create a new table called 'products' with fields for type, title, price, and description."""
    conn.execute('''CREATE TABLE products (
                        type TEXT,
                        title TEXT,
                        price TEXT,
                        description TEXT
                    )''')

def insert_data(conn, data):
    """Insert data into the 'products' table."""
    conn.execute('INSERT INTO products VALUES (?,?,?,?)', data)

if __name__ == '__main__':
    # Connect to database
    conn = sqlite3.connect('products.db')

    # Create table if it doesn't already exist
    create_table(conn)

    # Set up headless browser
    driver = uc.Chrome()
    driver.get('https://www.beautylish.com/new-arrivals')
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    # Extract data from webpage and insert into database
    tags = soup.find_all('h2', {'class': 'section_divider'})
    for tag in tags:
        type = tag.find('a').text.strip()
        print('\n' + '-' * 30 + type + '-' * 30 + '\n')
        ul_tag = tag.find_next_sibling('ul', {'class': 'sherpaList'})
        if ul_tag:
            li_tags = ul_tag.find_all('li')
            for li_tag in li_tags:
                span_tags = li_tag.find_all(lambda tag: tag.name == 'span' and tag.get('class') == ['offerCard_caption'])
                for span_tag in span_tags:
                    title = span_tag.find('p', {'class': 'offerCard_title'}).text
                    description = span_tag.find('p', {'class': 'offerCard_description'}).text
                    price = span_tag.find('span').text
                    print(title + '\t\t' + description + '\t\t\t\t' + price)
                    # Insert data to the database
                    data = (type, title, price, description)
                    insert_data(conn, data)

    conn.commit()
    conn.close()

    # Save webpage HTML to file
    fname = "beautylish.html"
    with io.open(fname, "w", encoding="utf-8") as f:
        f.write(html)
        