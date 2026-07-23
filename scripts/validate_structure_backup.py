import os
import yaml


ROOT = "."


def check_file(path):
    if os.path.exists(path):
        return True
    return False


def check_skill_layer():

    print("\n=== Skill Layer Check ===")

    errors = []

    for category in ["frontend", "backend", "ui", "ux", "product"]:

        path = f"skills/{category}"

        if not os.path.exists(path):
            continue

        for skill in os.listdir(path):

            skill_path = os.path.join(path, skill)

            if not os.path.isdir(skill_path):
                continue

            required = [
                "SKILL.md",
                "README.md",
                "CHECKLIST.md"
            ]

            for file in required:

                target = os.path.join(skill_path, file)

                if not os.path.exists(target):
                    errors.append(target)

            examples = os.path.join(
                skill_path,
                "examples"
            )

            if not os.path.exists(examples):
                errors.append(
                    examples
                )


    if errors:

        print("❌ Skill Issues:")

        for e in errors:
            print("-", e)

    else:
        print("✅ All Skills Complete")


def check_agents():

    print("\n=== Agent Layer Check ===")

    errors=[]

    if not os.path.exists("agents"):
        print("agents missing")
        return


    for agent in os.listdir("agents"):

        path=f"agents/{agent}"

        if not os.path.isdir(path):
            continue


        for file in [
            "AGENT.md",
            "SOP.md",
            "README.md",
            "CHECKLIST.md",
            "agent.yaml"
        ]:

            if not os.path.exists(
                f"{path}/{file}"
            ):
                errors.append(
                    f"{path}/{file}"
                )


    if errors:

        print("❌ Agent Issues:")

        for e in errors:
            print("-",e)

    else:
        print("✅ All Agents Complete")


def check_runtime():

    print("\n=== Runtime Check ===")

    files=[
        "runtime/agent-registry.yaml",
        "runtime/skill-registry.yaml",
        "runtime/workflow-registry.yaml",
        "runtime/router.yaml"
    ]


    for f in files:

        if os.path.exists(f):
            print("✅",f)

        else:
            print("❌",f)



if __name__=="__main__":

    check_skill_layer()

    check_agents()

    check_runtime()

    print("\nValidation Finished.")
