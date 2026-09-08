from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]

class MetaParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'meta' and a.get('property', a.get('name')) in ('og:image', 'twitter:image'):
            url = urlparse(a.get('content', ''))
            if url.netloc in ('', 'medrealty.ru', 'www.medrealty.ru'):
                assert (ROOT / url.path.lstrip('/')).is_file(), f'Missing preview: {url.path}'

for name in ('index.html', 'en/index.html', 'robots.txt', 'sitemap.xml', 'CNAME', 'og.png'):
    assert (ROOT / name).is_file(), f'Missing required file: {name}'
for p in ROOT.rglob('*.html'):
    MetaParser().feed(p.read_text(encoding='utf-8'))
print('Site entry points and social preview assets: OK')
