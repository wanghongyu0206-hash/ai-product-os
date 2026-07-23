import os
import yaml


def load_yaml(path):

    with open(path,"r") as f:
        return yaml.safe_load(f)



def check_runtime_skills():

    print("\n=== Runtime Skill Registry ===")


    data = load_yaml(
        "runtime/skill-registry.yaml"
    )


    errors=[]


    categories=data.get(
        "categories",
        {}
    )


    for category,info in categories.items():

        skills=info.get(
            "skills",
            {}
        )


        for skill,config in skills.items():

            path=config.get(
                "path"
            )


            if not path:

                path=f"skills/{category}/{skill}/"


            if not os.path.exists(
                path
            ):

                errors.append(
                    f"Missing: {path}"
                )


    if errors:

        for e in errors:
            print("❌",e)

    else:

        print(
            "✅ Runtime skills exist"
        )




def check_agent_skills():

    print("\n=== Agent Skill References ===")


    registry=load_yaml(
        "runtime/agent-registry.yaml"
    )


    errors=[]


    for agent,data in registry["agents"].items():

        for skill in data.get(
            "skills",
            []
        ):

            path=f"skills/{skill}/"


            if not os.path.exists(
                path
            ):

                errors.append(
                    f"{agent}: {skill}"
                )


    if errors:

        for e in errors:
            print("❌",e)

    else:

        print(
            "✅ Agent skills valid"
        )




def check_catalog():

    print("\n=== Catalog Check ===")


    if os.path.exists(
        "catalog/skills.yaml"
    ):

        print(
            "✅ catalog/skills.yaml exists"
        )

    else:

        print(
            "❌ catalog/skills.yaml missing"
        )




if __name__=="__main__":

    check_runtime_skills()

    check_agent_skills()

    check_catalog()


    print(
        "\nSkill validation finished."
    )
