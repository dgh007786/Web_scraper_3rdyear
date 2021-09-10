from web_scraper import WebScraper

# Used websites as for running a scraper in loop with various simialr keywords - so the content won't be repeated
used_websites = []
ws = WebScraper(verbose=True)

# Query which will be used as an input to google search
search_query = 'total cases of COVID-19 in india'
parsed_query = ws.parse_query(search_query)

# Gets links and parses them, removing stopsites and stop extensions
google_links = ws.get_google_links_for_single_query(parsed_query)
parsed_google_links = ws.parse_google_links(google_links, used_websites)

# Extracts the content from every link retrieved
google_links_content, website_titles = ws.get_content_from_google_links(parsed_google_links)
assert len(google_links_content) == len(website_titles) == len(parsed_google_links)

print('Extracted the textual content from {} websites on the query topic.'.format(len(website_titles)))
used_websites += parsed_google_links