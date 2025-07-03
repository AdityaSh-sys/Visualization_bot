def build_rag_prompt(df, matched_rows, user_query, chart_type=None, max_schema_cols=9, context_caption="Sample Rows"):
    raw_cols = list(df.columns)
    schema_desc = " | ".join(raw_cols[:max_schema_cols])
    if len(raw_cols) > max_schema_cols:
        schema_desc += " | ..."
    context = f"=== {context_caption} ===\n" + "\n".join(matched_rows)
    chart_hint = f"\nChart suggestion: {chart_type.lower()}" if chart_type and chart_type.lower() != "let llama pick" else ""
    system = (
        f"You are a highly helpful data QA and visualization assistant."
        f"\nYou will be given natural language questions and information from a table, including column names and a selection of the most relevant rows."
        f"\nIf the user's request needs a visualization or chart, output ONLY python code (matplotlib or seaborn, with plt or sns already imported, dataframe is 'df'), in a markdown code block, with NO extra text or markdown. End with plt.show()."
        f"\nIf it's a calculation or summary, output strictly ONE short sentence (no code/block)."
        f"\nNever mix code and plain text."
    )
    user = (
        f"Table columns: {schema_desc}\n"
        f"{context}\n"
        f"User question: {user_query}{chart_hint}"
    )
    return system, user