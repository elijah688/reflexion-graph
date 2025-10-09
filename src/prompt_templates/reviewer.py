from src.prompt_templates.responder import actor_prompt_template

reviewer_instruction = (
    """
        Take the the unecessary and missing stuff in your reflection and revise your report.
        Use the search tool.
        Add references so that your work can be verified, that doesn't go towards the total token limit
    """,
)


reviewer_agent_template = actor_prompt_template.partial(
    **{"task_instruciton": reviewer_instruction}
)

