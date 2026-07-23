from pathlib import Path
import yaml


ROOT = Path(".")


errors = []


def check_file(path):
    if not Path(path).exists():
        errors.append(f"Missing: {path}")
        return False
    return True


def check_yaml(path):
    try:
        with open(path, "r") as f:
            yaml.safe_load(f)
        print("✅ YAML", path)
    except Exception as e:
        errors.append(
            f"YAML error {path}: {e}"
        )


def check_runtime():

    print("\n=== Runtime ===")

    files = [
        "runtime/agent-registry.yaml",
        "runtime/skill-registry.yaml",
        "runtime/workflow-registry.yaml",
        "runtime/router.yaml"
    ]

    for f in files:
        if check_file(f):
            check_yaml(f)



def check_agents():

    print("\n=== Agents ===")

    agents = [
        "architect",
        "backend",
        "frontend",
        "product-manager",
        "qa",
        "ui-designer",
        "ux-designer"
    ]

    for a in agents:

        base=f"agents/{a}"

        for f in [
            "AGENT.md",
            "README.md",
            "SOP.md",
            "agent.yaml"
        ]:

            check_file(
                f"{base}/{f}"
            )



def check_skills():

    print("\n=== Skills ===")

    skills = [
        "skills/frontend/react-component",
        "skills/frontend/nextjs-app-router",
        "skills/frontend/tailwind-system",
        "skills/frontend/shadcn-component",
        "skills/frontend/frontend-architecture",
        "skills/frontend/frontend-performance",
        "skills/frontend/frontend-review",

        "skills/backend/system-design",
        "skills/backend/api-design",
        "skills/backend/database-design",
        "skills/backend/authentication",
        "skills/backend/deployment",
        "skills/backend/rag-architecture",
        "skills/backend/ai-service",
    ]


    required=[
        "SKILL.md",
        "README.md",
        "CHECKLIST.md",
    ]


    for skill in skills:

        for f in required:
            check_file(
                f"{skill}/{f}"
            )

        if not Path(
            f"{skill}/examples"
        ).exists():

            errors.append(
                f"Missing examples: {skill}"
            )



def check_gitignore():

    print("\n=== Git ===")

    if not Path(".gitignore").exists():

        errors.append(
            "Missing .gitignore"
        )



if __name__=="__main__":

    check_runtime()
    check_agents()
    check_skills()
    check_gitignore()


    print("\n================")

    if errors:

        print("❌ FOUND ISSUES\n")

        for e in errors:
            print("-",e)

    else:

        print(
            "✅ PROJECT READY FOR COMMIT"
        )
