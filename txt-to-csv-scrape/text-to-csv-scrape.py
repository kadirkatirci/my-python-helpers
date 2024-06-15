from bs4 import BeautifulSoup
import csv

def html_to_csv(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, 'html.parser')

    titles = soup.find_all('h1')
    contents = []

    for i in range(len(titles)):
        if i < len(titles) - 1:
            content = str(titles[i].next_sibling)
            sibling = titles[i].next_sibling
            while sibling and sibling != titles[i + 1]:
                sibling = sibling.next_sibling
                if sibling:
                    content += str(sibling)
        else:
            content = str(titles[i].next_sibling)
            sibling = titles[i].next_sibling
            while sibling:
                sibling = sibling.next_sibling
                if sibling:
                    content += str(sibling)
        contents.append(content.strip())

    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['title', 'content'])
        for title, content in zip(titles, contents):
            writer.writerow([title.get_text().strip(), content])

# Example usage
html_to_csv('input.txt', 'output.csv')
