# Crawl4AI Scraper – Trasforma il Web in Contenuto Pronto per l'IA

**Estrai Markdown pulito e dati strutturati da qualsiasi sito web in pochi secondi**: questo Actor Apify usa [Crawl4AI](https://github.com/unclecode/crawl4ai) e Playwright per convertire pagine web reali in contenuto pronto all'uso per pipeline RAG, agenti AI, chatbot e modelli LLM — senza scrivere una riga di codice di scraping.

## Perché usare questo Actor

- 🧠 **Output AI-ready**: Markdown pulito, senza menu/pubblicità/rumore HTML, ideale per indicizzazione RAG e prompt LLM
- ⚡ **Veloce e scalabile**: basato su Playwright, gestisce anche siti JavaScript-heavy
- 🔌 **Zero configurazione**: basta una lista di URL, il resto lo fa l'Actor
- 🔁 **Integrabile**: output in Dataset Apify, pronto per n8n, Make, LangChain, LlamaIndex o qualsiasi pipeline di automazione

## Casi d'uso

- Costruire una knowledge base per un agente AI o chatbot aziendale
- Alimentare pipeline RAG (Retrieval-Augmented Generation) con contenuto web aggiornato
- Trasformare contenuti di siti concorrenti o partner in formato strutturato per analisi
- Preparare dataset di training/fine-tuning a partire da pagine web pubbliche

## Input

| Campo | Tipo | Descrizione |
|---|---|---|
| `startUrls` | array | Elenco di URL da crawlare |
| `maxPages` | integer | Numero massimo di URL processati nel run (default: 1) |

Esempio:
```json
{
  "startUrls": [{ "url": "https://example.com" }],
  "maxPages": 1
}
```

## Output

Ogni URL crawlato produce un item nel Dataset con:
- `url`: l'URL crawlato
- `success`: esito del crawling
- `markdown`: contenuto della pagina convertito in Markdown pulito, pronto per l'IA

## Tecnologia

Basato su [Crawl4AI](https://github.com/unclecode/crawl4ai), il crawler open-source LLM-friendly con oltre 50k stelle su GitHub, e sull'[Apify SDK per Python](https://docs.apify.com/sdk/python/).

---

**Keyword**: web scraping, web crawler, Markdown converter, dati pronti per LLM, RAG, agenti AI, data extraction, Apify Actor, Playwright scraper, contenuto pronto per l'IA.
