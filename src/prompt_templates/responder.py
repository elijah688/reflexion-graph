from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from datetime import datetime


actor_prompt_template = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
                You're a researcher. 
                You're the rizzler. 
                You search the internet and write lit blogposts.
                You should carry out the following:
                Current Timestamp: {timestamp}
                1. {task_instruciton}
                2. Critique of your output. Be extra harsh and critical to maximize improvement.
                3. Generate 1 to 3 search terms that would aid in research for supplementary information, remember no more than 3 search tearms.
                to improve your report.
            """,
        ),
        MessagesPlaceholder("messages"),
    ]
).partial(**{"timestamp": datetime.now().isoformat()})

responder_template = actor_prompt_template.partial(
    **{"task_instruciton": "generate a report of 10 tokens. Do not generate more than 10 tokens"}
)
