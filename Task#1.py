# Написать метод domain_name, который вернет домен из url адреса:
"""
url = "http://github.com/carbonfive/raygun" -> domain name = "github"
url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
url = "https://www.cnet.com"                -> domain name = "cnet"
"""


def domain_name(url):
    str = url.split(".")
    if "www" in str[0]:
        return str[1]
    else:
        _, name = str[0].split("://")
        return name


assert domain_name("http://google.com") == "google"
assert domain_name("http://google.co.jp") == "google"
assert domain_name("www.xakep.ru") == "xakep"
assert domain_name("https://youtube.com") == "youtube"