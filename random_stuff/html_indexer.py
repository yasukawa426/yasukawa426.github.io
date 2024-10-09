import os
import datetime
import sys

# Recursively generate HTML list items for directory structure.
# path is the path we are listing. you should call using the root you want to analyze.
# number is the number of pages (.html) we currently are counting. Used when being called recursevely.
def generate_html_list(path, number=0):
    page_number = number

    html = "<ul>\n"
    for item in sorted(os.listdir(path)):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            # Remover "_" and make each word capitalized.
            formated_item = item.replace("_", " ").title()

            html += f"<li><strong>{formated_item}:</strong></li>\n"  # Directory

            results = generate_html_list(
                item_path, page_number
            )  # Get the result from calling the method

            # update html
            html += results[0]

            # update number of pages.
            page_number = results[1]
        else:
            # is a html file
            if item.endswith(".html"):
                # so we increase the number of pages.
                page_number += 1

                # Remove "_", make each word capitalized, and turns ".Html" into ".html"
                formated_item = item.replace("_", " ").replace(".html", "").title()

                html += f'<li><a href="{item_path}">{formated_item}</a></li>\n'  # File
    html += "</ul>\n"

    # returns a tuple with the html and number of pages
    return html, page_number


if __name__ == "__main__":
    start_time = datetime.datetime.now()

    HTML_PATH = "./html"

    # incresing recursio limit
    # sys.setrecursionlimit(5000)
    
    html, pages = generate_html_list(HTML_PATH)
    html = f"<p>Number of available pages: {pages}</p> \n{html}"

    print(f"Pages: {pages}")

    file = open("indexes.txt", "w")
    file.write(html)
    file.close()

    end_time = datetime.datetime.now()
    elapsed_time = end_time - start_time

    print(f"Indexed in: {elapsed_time.total_seconds() * 1000}ms")
