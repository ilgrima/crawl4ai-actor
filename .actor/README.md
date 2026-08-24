# Crawl4AI Scraper – Trasforma il Web in Contenuto Pronto per l'IA

**Estrai Markdown pulito e dati strutturati da qualsiasi sito web in pochi secondi**: Crawl4AI Scraper converte pagine web reali in contenuto pronto all'uso per pipeline RAG, agenti AI, chatbot e modelli LLM — senza scrivere una riga di codice di scraping. Basta incollare una lista di URL e ottieni Markdown pulito, pronto per l'indicizzazione o il prompt.

## Perché usare questo Actor

- 🧠 **Output AI-ready**: Markdown pulito, senza menu, pubblicità o rumore HTML — pronto per RAG e prompt LLM
- ⚡ **Veloce e scalabile**: crawler basato su Playwright, gestisce anche siti JavaScript-heavy e Single Page Application
- 🔌 **Zero configurazione**: incolla gli URL, avvia, ottieni i dati — nessuna competenza di scraping richiesta
- 🔁 **Integrabile ovunque**: output in Dataset Apify, esportabile in JSON/CSV/Excel o collegabile via API a n8n, Make, LangChain, LlamaIndex e qualsiasi pipeline di automazione

## Casi d'uso

- **Knowledge base per agenti AI**: alimenta il tuo chatbot o assistente aziendale con contenuti web sempre aggiornati
- **Pipeline RAG (Retrieval-Augmented Generation)**: prepara documenti puliti pronti per l'indicizzazione vettoriale
- **Analisi competitiva**: trasforma i contenuti di siti concorrenti o partner in dati strutturati
- **Dataset per training/fine-tuning**: raccogli contenuto testuale pulito da pagine web pubbliche

## Come funziona

1. Fornisci una o più `startUrls`
2. L'Actor apre ogni pagina con un browser reale (Playwright), rimuove il rumore HTML e converte il contenuto in Markdown pulito
3. Ogni pagina crawlata diventa un item nel Dataset di output, pronto per essere scaricato o collegato ad altri strumenti

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

## Domande frequenti

**Serve sapere programmare per usarlo?**
No. Basta compilare l'input con gli URL da crawlare e avviare il run dalla Console Apify.

**Che differenza c'è con uno scraper HTML classico?**
A differenza di uno scraper che restituisce HTML grezzo da ripulire manualmente, questo Actor consegna direttamente Markdown pulito, pensato per essere letto da un LLM o indicizzato in un sistema RAG.

**Funziona anche su siti con contenuti caricati via JavaScript?**
Sì, il crawling avviene tramite un browser reale (Playwright), quindi gestisce anche pagine dinamiche e Single Page Application.

## Tecnologia

Basato su [Crawl4AI](https://github.com/unclecode/crawl4ai), il crawler open-source LLM-friendly con oltre 50k stelle su GitHub, e sull'[Apify SDK per Python](https://docs.apify.com/sdk/python/).

---

**Keyword**: web scraping, web crawler, Markdown converter, dati pronti per LLM, RAG, agenti AI, data extraction, Apify Actor, Playwright scraper, contenuto pronto per l'IA.
