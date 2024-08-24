import requests
from bs4 import BeautifulSoup

# Step 1: Send a request to the website
url = "https://fast.com/"
response = requests.get(url)

# Step 2: Check if the request was successful
if response.status_code == 200:
    # Step 3: Parse the HTML content
    soup = BeautifulSoup(response.content, 'lxml')

    # Step 4: Get the page source as a string
    # page_source = soup.prettify()
    # print(page_source)

    # This just get the first paragraph
    span_tag = soup.find('span')
    # print(f"p_tag: {span_tag}\n\n")

    # To fetch all paragraphs
    spans = soup.find_all('span')
    # print(spans)
    for span in spans:
        """ Get all spans! """
        # print(span.get_text(), end="\n\n")

    # Get all spans element with specific class
    a_with_class = soup.find_all('a', class_="test-config-btn")
    for i, a in enumerate(a_with_class, start=1):
        print(f"{i}. {a.text}")

    # Find the id of div and iterate into it to get text of child web elements
    div_element = soup.find('div', id="help-content")
    spans = div_element.find_all('span')
    # all_span_text = [print(span.text + "\n") for span in spans]
    
    # Accesses the parent tag of the current tag
    child_div = soup.find('div', class_="your-speed-message")
    new_tag = child_div.find('div', id="your-speed-message")
    new_tag.decompose() # <- Removes all the content inside the div with id[your-speed-message]
    parent_tag = child_div.parent
    print(f"Parent tag: {parent_tag}")

    # Accesses the children of a tag. 'tag.children' returns an iterator over the children.
    children_tag = child_div.children
    # print(f"Children tag: {children_tag}")


else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")