# ScholarGraph AI Backend

The backend is a FastAPI service for turning paper metadata and abstracts into structured research intelligence.

## Current prototype endpoints

| Endpoint | Method | Purpose |
|---|---|---|
| `/` | GET | Health and project metadata |
| `/analyze/paper` | POST | Analyze one paper and return themes, gap signals, and research questions |
| `/graph/sample` | GET | Return a sample knowledge graph for frontend visualization |
| `/matrix/sample` | GET | Return a sample literature review matrix |

## Run locally

```bash
cd backend
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open the API docs:

```text
http://localhost:8000/docs
```

## Design notes

The current implementation uses deterministic rule-based logic so the repository is runnable without external API keys. Future versions can connect this service to local language models, embeddings, vector databases, citation databases, and graph stores.
