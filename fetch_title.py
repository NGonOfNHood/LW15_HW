def fetch_title():
    url = _url.get()
    try:
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        title = soup.title.string if soup.title else "No title found"
        sb(f"Title: {title}")
    except requests.RequestException as err:
        sb(str(err))