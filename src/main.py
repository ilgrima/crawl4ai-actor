import asyncio

from apify import Actor
from crawl4ai import AsyncWebCrawler


async def main() -> None:
    async with Actor:
        actor_input = await Actor.get_input() or {}
        start_urls = actor_input.get('startUrls', [])
        max_pages = actor_input.get('maxPages', 1)

        urls = [item['url'] for item in start_urls][:max_pages]
        if not urls:
            Actor.log.warning('Nessun URL fornito in input (startUrls)')
            return

        async with AsyncWebCrawler() as crawler:
            for url in urls:
                Actor.log.info(f'Crawling {url}')
                result = await crawler.arun(url=url)
                await Actor.push_data({
                    'url': url,
                    'success': result.success,
                    'markdown': result.markdown,
                })


if __name__ == '__main__':
    asyncio.run(main())
