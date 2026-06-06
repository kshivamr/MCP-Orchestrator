# 🤖 MCP Orchestrator

A multi-tool AI agent that coordinates **Playwright**, **Airbnb**, **DuckDuckGo**, and **Enuygun** through the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) — enabling automated travel research, web browsing, and price comparison in a single unified workflow.

---

## ✨ What It Does

MCP Orchestrator acts as a central brain that delegates tasks across four specialized tools, letting an AI agent browse the web, search for flights, find accommodations, and gather information — all without switching contexts.

| Tool | Role |
|---|---|
| 🎭 **Playwright** | Headless browser automation — interact with any website |
| 🏠 **Airbnb** | Search and retrieve accommodation listings |
| 🦆 **DuckDuckGo** | Privacy-first web search for general information |
| ✈️ **Enuygun** | Turkish flight & travel price comparison |

---

## 🏗️ Architecture

```
User / LLM
     │
     ▼
MCP Orchestrator
     │
     ├──▶ Playwright    (browser automation)
     ├──▶ Airbnb        (accommodation search)
     ├──▶ DuckDuckGo    (web search)
     └──▶ Enuygun       (flight search)
```

The orchestrator exposes a unified MCP interface. The connected LLM (e.g. Claude) decides which tool to invoke based on the task, and the orchestrator routes calls accordingly.

---

## 🚀 Getting Started

### Prerequisites

- Node.js 18+
- npm or yarn
- A running MCP-compatible client (e.g. Claude Desktop, Claude Code)

### Installation

```bash
git clone https://github.com/yourusername/mcp-orchestrator.git
cd mcp-orchestrator
npm install
```

### Install Playwright Browsers

```bash
npx playwright install
```

### Configuration

Copy the example config and fill in your settings:

```bash
cp config.example.json config.json
```

```json
{
  "tools": {
    "playwright": { "enabled": true },
    "airbnb": { "enabled": true },
    "duckduckgo": { "enabled": true },
    "enuygun": { "enabled": true }
  }
}
```

### Run

```bash
npm start
```

---

## 🔧 Usage with Claude Desktop

Add this to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "mcp-orchestrator": {
      "command": "node",
      "args": ["/path/to/mcp-orchestrator/index.js"]
    }
  }
}
```

Once connected, Claude can use natural language to trigger any of the four tools automatically.

**Example prompts:**

- *"Find me flights from Istanbul to Berlin next Friday on Enuygun."*
- *"Search Airbnb for a 2-bedroom apartment in Barcelona for 5 nights."*
- *"Use DuckDuckGo to find the latest travel restrictions for Japan."*
- *"Open this URL with Playwright and extract the pricing table."*

---

## 🛠️ Tool Details

### 🎭 Playwright
Automates Chromium/Firefox/WebKit browsers. Use it to navigate pages, fill forms, click buttons, take screenshots, and extract content from dynamic JavaScript-heavy sites.

### 🏠 Airbnb
Searches Airbnb listings by location, dates, and guest count. Returns listing names, prices, ratings, and URLs.

### 🦆 DuckDuckGo
Runs privacy-respecting web searches and returns structured results — titles, URLs, and snippets — without tracking.

### ✈️ Enuygun
Queries [Enuygun.com](https://www.enuygun.com) for domestic and international flight prices, schedules, and availability.

---

## 📁 Project Structure

```
mcp-orchestrator/
├── index.js          # MCP server entry point
├── tools/
│   ├── playwright.js
│   ├── airbnb.js
│   ├── duckduckgo.js
│   └── enuygun.js
├── config.example.json
├── package.json
└── README.md
```

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you'd like to change.

1. Fork the repo
2. Create your feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

---

## 📄 License

MIT — see [LICENSE](LICENSE) for details.

---

## 🙏 Acknowledgements

Built on top of the [Model Context Protocol](https://modelcontextprotocol.io/) by Anthropic. Inspired by the idea that AI agents should have real, composable tools — not just text.