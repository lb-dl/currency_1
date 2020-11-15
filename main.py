from fake_useragent import UserAgent

from time import sleep


def populate_table_jobs(data):
    conn = sqlite3.connect('workua.db')
    c = conn.cursor()
    c.execute(
        "CREATE TABLE IF NOT EXISTS jobs ('ID' INT PRIMARY KEY NOT NULL, 'JOB_TITLE' TEXT, 'COMPANY' TEXT,'COMPANY_DESCRIPTION' TEXT, 'JOB_DETAILS' TEXT);"
    )

    c.execute(
        "INSERT INTO jobs VALUES(?, ?, ?, ?)",
        [data['job_title'], data['company'],data['company_description'],data['job_details'], ]
    )
    conn.commit()
    conn.close()




def parse_details(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    try:
        job_title = soup.find('h1', {'id': 'h1-name'}).text
    except:
        job_title = 'Read job_details'
    try:
        company = soup.find('img', class_="logo-job").get('alt')
    except:
        company = 'Read company description'

    job_details_html = soup.find('div', {'id': 'job-description'})
    try:
        company_description = job_details_html.find('p').text
    except:
        company_description = ''

    job_details = []
    job_details_list = job_details_html.findAll(lambda tag: tag.name == 'ul' or tag.name == 'ol')
    if not job_details_list:
        job_detail = job_details_html.find('p').find_next_sibling().text
        job_details.append(job_detail)
    else:
        for job_detail in job_details_list:
            job_detail = job_detail.text
            job_detail = ' '.join(job_detail.split('\n'))
            job_details.append(job_detail)

    data = {
            'job_title': job_title,
            'company': company,
            'company_description': company_description,
            'job_details': job_details,
            }

    write_to_json(data)
    populate_table_jobs(data)


def remove_results():
    try:
        os.remove('.results.txt')
    except FileNotFoundError:
        pass


def random_sleep():
    sleep(random.randint(1, 5))


def write_to_file(**kwargs):
    with open('./results.txt', 'a') as file:
        row = ', '.join(
            f'{key}: {value}' for key, value in kwargs.items()
        )
        file.write(row + '\n')

def write(_format='file', **kwargs):
    if _format == 'file':
        write_to_file(**kwargs)


def write_to_csv(data):
    with open('workua.csv', 'a') as file:
        writer = csv.writer(file)

        writer.writerow(
            (data['company_description'],
             data['job_details'])
        )

def write_to_json(data):
    with open('workua.json', 'a') as outfile:
        json.dump(data, outfile, ensure_ascii=False, indent=4)


def main():
    counter = 80
    ua = UserAgent()
    headers = {
        'User-Agent': ua.random,
    }

    while True:
        counter += 1
        print(f'page:{counter}')
        random_sleep()

        query_params = {'page': counter}
        url = f'https://www.work.ua/jobs/'
        response = requests.get(url, params=query_params, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        job_list = soup.find('div', {'id': 'pjax-job-list'})

        if job_list is None:
            break

        if counter == 83:
            break

        job_set = job_list.find_all('h2')
        for job in job_set:
            a_tag = job.find('a', href=True)
            href = a_tag['href'].split('/')[2]
            title = a_tag['title']
            content = a_tag.text


            parse_details(url+href)

            write(
                href=href,
                title=title,
                content=content,
            )


if __name__ == '__main__':
    main()
