# Crawl4AI Actor

Apify Actor che usa [Crawl4AI](https://github.com/unclecode/crawl4ai) per trasformare pagine web in Markdown/JSON puliti, pronti per pipeline LLM e RAG.

## Input

- `startUrls`: elenco di URL da crawlare
- `maxPages`: numero massimo di URL processati nel run (default: 1)

## Output

Ogni URL crawlato produce un item nel Dataset con `url`, `success` e `markdown`.
