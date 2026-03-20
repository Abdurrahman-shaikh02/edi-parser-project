```
edi-parser-project/
│
├── backend/
│   ├── app/
│   │   ├── main.py              # FastAPI entry point
│   │   ├── api/                 # Routes
│   │   │   ├── upload.py
│   │   │   ├── parse.py
│   │   │   ├── validate.py
│   │   │   ├── ai_chat.py
│   │   │
│   │   ├── parser/              # Core parsing logic
│   │   │   ├── tokenizer.py     # Split into segments/elements
│   │   │   ├── segment.py       # Segment representation
│   │   │   ├── loop_builder.py  # Build hierarchical loops
│   │   │   ├── edi_parser.py    # Main parser logic
│   │   │
│   │   ├── validator/           # Validation engine
│   │   │   ├── rules/           # Rule definitions (JSON/YAML)
│   │   │   │   ├── base_rules.json
│   │   │   │   ├── rules_837.json
│   │   │   │   ├── rules_835.json
│   │   │   │   ├── rules_834.json
│   │   │   │
│   │   │   ├── rule_engine.py   # Applies rules
│   │   │   ├── validators.py    # NPI, date, etc.
│   │   │   ├── error_model.py   # Error structure
│   │   │
│   │   ├── services/            # Business logic
│   │   │   ├── file_service.py
│   │   │   ├── detection.py     # 837/835/834 detection
│   │   │   ├── summary.py       # 835 / 834 summaries
│   │   │   ├── fix_engine.py    # Auto-fix suggestions
│   │   │
│   │   ├── ai/                  # AI integration
│   │   │   ├── llm_client.py
│   │   │   ├── prompt_builder.py
│   │   │   ├── context_builder.py
│   │   │
│   │   ├── models/              # Pydantic models
│   │   │   ├── edi_models.py
│   │   │   ├── response_models.py
│   │   │
│   │   ├── utils/
│   │   │   ├── constants.py
│   │   │   ├── helpers.py
│   │
│   ├── tests/
│   │   ├── test_parser.py
│   │   ├── test_validator.py
│   │
│   ├── requirements.txt
│   ├── Dockerfile
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── FileUpload.tsx
│   │   │   ├── SegmentTree.tsx
│   │   │   ├── ErrorPanel.tsx
│   │   │   ├── ChatPanel.tsx
│   │   │   ├── SummaryView.tsx
│   │   │
│   │   ├── pages/
│   │   │   ├── Home.tsx
│   │   │   ├── Dashboard.tsx
│   │   │
│   │   ├── services/
│   │   │   ├── api.ts
│   │   │
│   │   ├── hooks/
│   │   │   ├── useParser.ts
│   │   │   ├── useValidation.ts
│   │   │
│   │   ├── types/
│   │   │   ├── ediTypes.ts
│   │   │
│   │   ├── App.tsx
│   │   ├── main.tsx
│   │
│   ├── package.json
│   ├── tailwind.config.js
│
├── sample-data/                 # VERY IMPORTANT for demo
│   ├── valid_837.edi
│   ├── invalid_837.edi
│   ├── sample_835.edi
│   ├── sample_834.edi
│
├── docs/
│   ├── architecture.md
│   ├── parser-design.md
│   ├── validation-rules.md
│
├── docker-compose.yml
├── README.md
```
