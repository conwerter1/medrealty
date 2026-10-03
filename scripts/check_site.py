from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlparse
from html import unescape
import re
import xml.etree.ElementTree as ET

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
    featured = re.findall(r'<h3>\s*<a[^>]+href="/(?:en/)?posts/\d+\.html"[^>]*>(.*?)</a>\s*</h3>', page, re.S)
    assert featured, f'No featured article headlines in {name}'
    for raw_title in featured:
        title = unescape(re.sub(r'<[^>]+>', '', raw_title)).strip()
        assert len(title) <= 160, f'Featured headline too long in {name}: {len(title)} chars'
assert issue_ids[0] == issue_ids[1], f'RU/EN issue mismatch: {issue_ids}'
for name in (f'posts/{issue_ids[0]}.html', f'en/posts/{issue_ids[0]}.html'):
    assert (ROOT / name).is_file(), f'Missing latest article: {name}'

indexed_pages = set()
for node in ET.parse(ROOT / 'sitemap.xml').findall('{*}url/{*}loc'):
    path = urlparse(node.text).path.lstrip('/')
    indexed_pages.add(ROOT / (path + 'index.html' if path.endswith('/') or not path else path))

for p in ROOT.rglob('*.html'):
    text = p.read_text(encoding='utf-8')
    MetaParser().feed(text)
    # Search-engine ownership verification files are not content pages.
    if p not in indexed_pages:
        continue
    counter_ids = re.findall(r"\bym\(\s*(\d+)\s*,\s*['\"]init['\"]", text)
    assert counter_ids == ['109342254'], f'Missing, conflicting or duplicate Metrika counter: {p.relative_to(ROOT)}'
    assert 'mc.yandex.ru/metrika/tag.js' in text, f'Missing Metrika loader: {p.relative_to(ROOT)}'
print(f'Site entry points, issue {issue_ids[0]} and social preview assets: OK')
