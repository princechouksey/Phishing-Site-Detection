from bs4 import BeautifulSoup

def parse_html_for_dom_elements(html_content: str) -> dict:
    """
    Extracts key DOM elements like forms, links, and scripts from raw HTML content.

    Returns:
        dict with keys: 'forms', 'links', 'scripts'
    """
    soup = BeautifulSoup(html_content, "html.parser")

    # Extract forms
    forms = []
    for form in soup.find_all("form"):
        form_info = {
            "action": form.get("action"),
            "method": form.get("method"),
            "inputs": [
                {"name": inp.get("name"), "type": inp.get("type")}
                for inp in form.find_all("input")
            ]
        }
        forms.append(form_info)

    # Extract links
    links = [a.get("href") for a in soup.find_all("a", href=True)]

    # Extract scripts
    scripts = [script.get("src") for script in soup.find_all("script") if script.get("src")]

    return {
        "forms": forms,
        "links": links,
        "scripts": scripts
    }
