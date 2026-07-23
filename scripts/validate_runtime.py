import os
import yaml


def load_yaml(path):

    with open(path,"r") as f:

        return yaml.safe_load(f)



def normalize_name(value):

    """
    支持:

    agent: architect

    或:

    agent:
      name: architect
    """

    if isinstance(value,dict):

        return value.get("name")

    return value




def check_agents():

    print("\n=== Agent Registry ===")

    data = load_yaml(
        "runtime/agent-registry.yaml"
    )

    errors=[]


    for name,agent in data["agents"].items():

        if not os.path.exists(
            agent["path"]
        ):

            errors.append(
                f"Missing agent {agent['path']}"
            )


        for skill in agent.get(
            "skills",
            []
        ):

            if not os.path.exists(
                "skills/"+skill
            ):

                errors.append(
                    f"{name} missing skill {skill}"
                )


    if errors:

        for e in errors:
            print("❌",e)

    else:

        print("✅ Agent references valid")




def check_workflows():

    print("\n=== Workflow Registry ===")


    data=load_yaml(
        "runtime/workflow-registry.yaml"
    )


    errors=[]


    for workflow,config in data["workflows"].items():

        for step in config.get(
            "sequence",
            []
        ):

            agent = normalize_name(
                step.get("agent")
            )


            if agent and not os.path.exists(
                f"agents/{agent}"
            ):

                errors.append(
                    f"{workflow} missing agent {agent}"
                )


    if errors:

        for e in errors:
            print("❌",e)

    else:

        print("✅ Workflow agents valid")




def check_router():

    print("\n=== Router ===")


    router=load_yaml(
        "runtime/router.yaml"
    )


    workflows=load_yaml(
        "runtime/workflow-registry.yaml"
    )["workflows"]


    errors=[]


    for route,item in router["routes"].items():

        agent=normalize_name(
            item.get("agent")
        )

        workflow=normalize_name(
            item.get("workflow")
        )


        if agent and not os.path.exists(
            f"agents/{agent}"
        ):

            errors.append(
                f"{route} missing agent {agent}"
            )


        if workflow and workflow not in workflows:

            errors.append(
                f"{route} missing workflow {workflow}"
            )


    if errors:

        for e in errors:
            print("❌",e)

    else:

        print("✅ Router references valid")




if __name__=="__main__":

    check_agents()

    check_workflows()

    check_router()

    print(
        "\nRuntime validation finished."
    )
