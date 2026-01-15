import re
from collections import Counter

STOPWORDS = {"the", "is", "and", "to", "of", "a", "in"}

def tokenize(text: str):
    # Match words like firewall, ids, vpn, network-security
    return re.findall(r"[a-zA-Z][a-zA-Z\-]+", text.lower())

def evaluate_summary(original: str, summary: str) -> dict:
    orig_tokens = tokenize(original)
    summ_tokens = tokenize(summary)

    # Top keywords from original text
    top_words = [
        w for w, _ in Counter(
            w for w in orig_tokens if w not in STOPWORDS
        ).most_common(20)
    ]

    coverage = sum(1 for w in top_words if w in summ_tokens) / max(len(top_words), 1)

    return {
        "original_words": len(orig_tokens),
        "summary_words": len(summ_tokens),
        "compression_ratio": round(len(summ_tokens) / max(len(orig_tokens), 1), 3),
        "keyword_coverage": round(coverage, 3),
    }
