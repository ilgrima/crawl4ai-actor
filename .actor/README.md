# Crawl4AI Scraper – Turn the Web into AI-Ready Content

**Extract clean Markdown and structured data from any website in seconds**: Crawl4AI Scraper converts real web pages into content ready for RAG pipelines, AI agents, chatbots and LLMs — no scraping code required. Just paste a list of URLs and get clean Markdown, ready for indexing or prompting.

## Why use this Actor

- 🧠 **AI-ready output**: clean Markdown, stripped of menus, ads and HTML noise — ready for RAG and LLM prompts
- ⚡ **Fast and scalable**: Playwright-based crawler, handles JavaScript-heavy sites and Single Page Applications
- 🔌 **Zero configuration**: paste the URLs, hit start, get the data — no scraping expertise required
- 🔁 **Integrates anywhere**: output lands in an Apify Dataset, exportable to JSON/CSV/Excel or connectable via API to n8n, Make, LangChain, LlamaIndex and any automation pipeline

## Use cases

- **Knowledge base for AI agents**: feed your company chatbot or assistant with always up-to-date web content
- **RAG pipelines (Retrieval-Augmented Generation)**: prepare clean documents ready for vector indexing
- **Competitive analysis**: turn competitor or partner website content into structured data
- **Training/fine-tuning datasets**: collect clean text content from public web pages

## How it works

1. Provide one or more `startUrls`
2. The Actor opens each page with a real browser (Playwright), strips out HTML noise and converts the content into clean Markdown
3. Each crawled page becomes a Dataset item, ready to download or connect to other tools

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

## FAQ

**Do I need to know how to code to use it?**
No. Just fill in the input with the URLs to crawl and start the run from the Apify Console.

**How is this different from a classic HTML scraper?**
Unlike a scraper that returns raw HTML you have to clean up yourself, this Actor delivers clean Markdown directly, designed to be read by an LLM or indexed in a RAG system.

**Does it work on sites with JavaScript-rendered content?**
Yes, crawling happens through a real browser (Playwright), so it handles dynamic pages and Single Page Applications too.

## Technology

Built on [Crawl4AI](https://github.com/unclecode/crawl4ai), the open-source LLM-friendly crawler with 50k+ GitHub stars, and the [Apify Python SDK](https://docs.apify.com/sdk/python/).

---

**Keywords**: web scraping, web crawler, Markdown converter, LLM-ready data, RAG, AI agents, data extraction, Apify Actor, Playwright scraper, AI-ready content.
