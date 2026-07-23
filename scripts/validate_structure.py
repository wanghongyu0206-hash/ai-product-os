import os
import yaml


def load_registry():

    with open(
        "runtime/skill-registry.yaml",
        "r"
    ) as f:

        return yaml.safe_load(f)



def check_skills():

    print("\n=== Registry Skill Check ===")

    registry = load_registry()

    errors = []


    skills = registry.get(
        "skills",
        {}
    )


    for category, items in skills.items():

        for skill in items:

            base = f"skills/{category}/{skill}"

            required = [
                "SKILL.md",
                "README.md",
                "CHECKLIST.md"
            ]

            for file in required:

                path = f"{base}/{file}"

                if not os.path.exists(path):

                    errors.append(path)


            example_path = f"{base}/examples"

            if not os.path.exists(example_path):

                errors.append(example_path)



    if errors:

        print("❌ Missing Skill Files:")

        for e in errors:

            print("-",e)

    else:

        print("✅ All Registry Skills Complete")




def check_agents():

    print("\n=== Agent Check ===")

    errors=[]


    for agent in os.listdir("agents"):

        path=f"agents/{agent}"


        if not os.path.isdir(path):

            continue


        for file in [
            "AGENT.md",
            "README.md",
            "SOP.md",
            "agent.yaml"
        ]:

            if not os.path.exists(
                f"{path}/{file}"
            ):

                errors.append(
                    f"{path}/{file}"
                )


    if errors:

        print("❌ Agent Issues")

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


    for file in files:

        if os.path.exists(file):

            print("✅",file)

        else:

            print("❌",file)




if __name__=="__main__":

    check_skills()

    check_agents()

    check_runtime()

    print("\nValidation Finished.")
