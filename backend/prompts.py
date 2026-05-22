def build_prompt(text: str) -> str:
    return f"""
You are an AI study assistant.

Based on the text below, generate the following sections in clear, markdown-formatted output:

## Summary
- A concise summary (5–10 bullet points).

## Flashcards
- 10 flashcards in the format:
  Q: ...
  A: ...

## Key Terms
- A list of key terms with short definitions.

## Quiz Questions
- 5 quiz questions (mix of multiple choice and short answer).

Text:
{text}
"""
