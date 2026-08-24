# Crawl4AI Scraper – Turn the Web into AI-Ready Content

**Extract clean Markdown and structured data from any website in seconds**: this Apify Actor uses [Crawl4AI](https://github.com/unclecode/crawl4ai) and Playwright to turn real web pages into content ready for RAG pipelines, AI agents, chatbots and LLMs — no scraping code required.

## Why use this Actor

- 🧠 **AI-ready output**: clean Markdown, stripped of menus/ads/HTML noise, ideal for RAG indexing and LLM prompts
- ⚡ **Fast and scalable**: built on Playwright, handles JavaScript-heavy sites too
- 🔌 **Zero configuration**: just a list of URLs, the Actor does the rest
- 🔁 **Easy to integrate**: output lands in an Apify Dataset, ready for n8n, Make, LangChain, LlamaIndex or any automation pipeline

## Use cases

- Build a knowledge base for an AI agent or company chatbot
- Feed RAG (Retrieval-Augmented Generation) pipelines with fresh web content
- Turn competitor or partner website content into structured data for analysis
- Prepare training/fine-tuning datasets from public web pages

## Input

| Field | Type | Description |
|---|---|---|
| `startUrls` | array | List of URLs to crawl |
| `maxPages` | integer | Maximum number of URLs processed in this run (default: 1) |

Example:
```json
{
  "startUrls": [{ "url": "https://example.com" }],
  "maxPages": 1
}
```

## Output

Each crawled URL produces one Dataset item with:
- `url`: the crawled URL
- `success`: crawl outcome
- `markdown`: the page content converted to clean, AI-ready Markdown

## Technology

Built on [Crawl4AI](https://github.com/unclecode/crawl4ai), the open-source LLM-friendly crawler with 50k+ GitHub stars, and the [Apify Python SDK](https://docs.apify.com/sdk/python/).

---

**Keywords**: web scraping, web crawler, Markdown converter, LLM-ready data, RAG, AI agents, data extraction, Apify Actor, Playwright scraper, AI-ready content.
