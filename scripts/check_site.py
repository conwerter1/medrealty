from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlparse
import re

ROOT = Path(__file__).resolve().parents[1]

class MetaParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'meta' and a.get('property', a.get('name')) in ('og:image', 'twitter:image'):
            url = urlparse(a.get('content', ''))
            if url.netloc in ('', 'medrealty.ru', 'www.medrealty.ru'):
                assert (ROOT / url.path.lstrip('/')).is_file(), f'Missing preview: {url.path}'

for name in ('index.html', 'en/index.html', 'articles.html', 'en/articles.html',
             'robots.txt', 'sitemap.xml', 'CNAME', 'og.png'):
    assert (ROOT / name).is_file(), f'Missing required file: {name}'

# A partially generated or copied deployment can have a current homepage but
# no corresponding article in one language. Keep the latest issue atomic.
issue_ids = []
for name in ('index.html', 'en/index.html'):
    page = (ROOT / name).read_text(encoding='utf-8')
    match = re.search(r'(?:Выпуск|Issue)\s*(?:№|No\.)?\s*<strong>\s*(?:№|No\.)?\s*(\d+)\s*</strong>', page)
    assert match, f'No issue number in {name}'
    issue_ids.append(int(match.group(1)))
assert issue_ids[0] == issue_ids[1], f'RU/EN issue mismatch: {issue_ids}'
for name in (f'posts/{issue_ids[0]}.html', f'en/posts/{issue_ids[0]}.html'):
    assert (ROOT / name).is_file(), f'Missing latest article: {name}'

for p in ROOT.rglob('*.html'):
    MetaParser().feed(p.read_text(encoding='utf-8'))
print(f'Site entry points, issue {issue_ids[0]} and social preview assets: OK')
