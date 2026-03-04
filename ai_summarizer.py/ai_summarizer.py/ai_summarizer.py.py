
import re

def summarize_text(text, max_sentences=2):
    sentences = re.split(r'(?<=[.!?]) +', text)
    if len(sentences) <= max_sentences:
        return text
    return " ".join(sentences[:max_sentences])

if __name__ == "__main__":
    sample_text = """
    Artificial intelligence is transforming the world. It helps automate tasks,
    improve decision-making, and increase productivity. Many industries now rely
    on AI tools to enhance their workflows and deliver better results.
    """

    summary = summarize_text(sample_text)
    print("Original text:")
    print(sample_text)
    print("\nSummary:")
    print(summary)