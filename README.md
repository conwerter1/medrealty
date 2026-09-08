# MedRealty

Public website for Mediterranean real estate news: https://medrealty.ru/.
Russian pages live at the root; English pages are under `/en/`.

## Structure

- `index.html`, `en/index.html`: home pages.
- `posts/`, `countries/`, `guides/`, `topics/`: content pages.
- `articles.html`, `feed.xml`, `sitemap.xml`: indexes and discovery feeds.
- `robots.txt`: crawler configuration.
- `CNAME`: custom GitHub Pages domain.
- `og.png`: shared 1200×630 social preview image.

## Deployment

GitHub Pages publishes `main` from the repository root. The custom domain is
`medrealty.ru`, with HTTPS enabled. Verify the Pages deployment after merging.
The upstream content generator runs outside this repository; when changing
generated HTML, update that generator as well to avoid losing edits next run.
Keep permanent shared assets such as `og.png` in the repository root.

## Checks

Run `python scripts/check_site.py` before publishing. It verifies local social
preview assets and the required entry points without making network requests.
After deployment, check both language home pages and `/og.png` over HTTPS.
