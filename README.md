# MedRealty Landing Page

SEO-страница для @MedRealtyNews. Два языка: RU (корень) и EN (`/en/`).

## Что внутри

- `index.html` — RU
- `en/index.html` — EN
- `sitemap.xml` — для поисковиков
- `robots.txt`

Включено:
- Open Graph + Twitter Card (превью при шеринге)
- Schema.org JSON-LD (Organization + WebSite)
- hreflang для RU/EN
- встроенный Telegram-виджет с последним постом
- мобильная адаптация
- без JS-фреймворков, грузится <100мс

## Деплой на GitHub Pages (рекомендую)

1. Создай GitHub-аккаунт, если ещё нет → https://github.com/signup
2. Создай репозиторий с именем **`<твой_username>.github.io`** (важно — именно с таким именем, это даст домен `https://<username>.github.io/`).
3. Скопируй содержимое папки `landing/` в репозиторий:
   ```bash
   cd C:\Dev\MedRealty\landing
   git init
   git add .
   git commit -m "initial landing"
   git remote add origin git@github.com:<username>/<username>.github.io.git
   git branch -M main
   git push -u origin main
   ```
4. В настройках репозитория → Pages → Source = `main`, folder = `/ (root)`.
5. Через 1-2 минуты страница откроется на `https://<username>.github.io/`.

После деплоя:
- замени в `index.html` и `en/index.html` все `medrealty.github.io` на свой реальный URL (если username другой)
- замени `MedRealtyNews/1` в Telegram-виджете на ID последнего поста (или оставь — виджет всё равно покажет канал)

## Деплой на Cloudflare Pages (альтернатива, без git)

1. Зарегистрируйся на https://pages.cloudflare.com/
2. Create project → Direct upload → перетащи папку `landing/`.
3. Получишь URL вида `https://medrealty-xyz.pages.dev/`.

## Регистрация в поисковиках (бесплатно)

После деплоя зарегистрируй сайт:

- **Google Search Console**: https://search.google.com/search-console → Add property → URL prefix → введи URL → подтверди через `<meta>`-тег (Cloudflare/GitHub дадут добавить) → отправь `sitemap.xml`.
- **Яндекс.Вебмастер**: https://webmaster.yandex.ru/ → добавить сайт → подтвердить → "Файлы Sitemap" → добавить `sitemap.xml`.
- **Bing Webmaster Tools**: https://www.bing.com/webmasters → можно импортировать из Google за 1 клик.

Через 1-2 недели страница начнёт ранжироваться по запросам:
- "недвижимость Кипра канал телеграм"
- "новости недвижимости Турции"
- "телеграм канал ВНЖ Греция"
- "cyprus property news telegram"
- и т.п.

## OG-картинка

Файлы `og.png` и `logo.png` упомянуты в meta-тегах, но не созданы. Сделать 1200×630 PNG с надписью "MedRealty — недвижимость Средиземноморья" и положить рядом с `index.html`. Можно сгенерировать в Canva/Figma за 5 минут.