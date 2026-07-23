from pathlib import Path


file = Path("runtime/skill-registry.yaml")

text = file.read_text()


replacements = {
    "skills/backend/database/":
    "skills/backend/database-design/",

    "skills/backend/auth/":
    "skills/backend/authentication/",

    "skills/backend/rag/":
    "skills/backend/rag-architecture/",
}


for old, new in replacements.items():
    text = text.replace(old, new)


file.write_text(text)


print("skill registry updated")
