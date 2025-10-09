from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder


formatter_template = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
                Take the report and reflection and format it appropriately as a ReviewerOuptut Object.
            """,
        ),
        MessagesPlaceholder("messages"),
    ]
)
