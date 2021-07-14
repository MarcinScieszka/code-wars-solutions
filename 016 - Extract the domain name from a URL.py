"""
Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. 

For example:
domain_name("http://github.com/carbonfive/raygun") == "github"
domain_name("http://www.zombie-bites.com") == "zombie-bites"
domain_name("https://www.cnet.com") == "cnet"
"""

import re

def domain_name(url):
    # split URL by dot and double slash
    url_parts = re.split("\.|//", url)

    # most common URL cases: https://www. or https:// or http://www. or http:// or www.

    for url_part in url_parts:
        if url_part not in ['www', 'http:', 'https:']:
            return url_part


print(domain_name("https://github.com/") == "github")
print(domain_name("https://www.abc.de") == "abc")
print(domain_name("http://www.zombie-bites.com") == "zombie-bites")
print(domain_name("http://google.com") == "google")
print(domain_name("www.formula1.com") == "formula1")
print(domain_name("sport.pl") == "sport")
