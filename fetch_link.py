def fetch_links():
    url = _url.get()
    try:
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        base_url = url.split("//")[-1].split("/")[0]  # Extract base URL part

        external_links = []
        for link in soup.find_all('a', href=True):
            link_url = link['href']
            if link_url.startswith("http") and base_url not in link_url:
                external_links.append(link_url)

        _images.set(tuple(external_links))  # Display links in listbox
        sb(f'External links found: {len(external_links)}')
    except requests.RequestException as err:
        sb(str(err))