import re

def extract_and_remove_styles(html_file_path, css_file_path):

    with open(html_file_path, 'r') as file:
        html_content = file.read()


    styles = re.findall(r'<style.*?>(.*?)<\/style>', html_content, re.DOTALL)


    combined_styles = "\n".join(styles)


    with open(css_file_path, 'w') as css_file:
        css_file.write(combined_styles.strip())


    cleaned_html_content = re.sub(r'<style.*?>.*?<\/style>', '', html_content, flags=re.DOTALL)


    with open(html_file_path, 'w') as file:
        file.write(cleaned_html_content.strip())

# Usage
html_file_path = 'index.html'
css_file_path = 'style.css'

extract_and_remove_styles(html_file_path, css_file_path)
