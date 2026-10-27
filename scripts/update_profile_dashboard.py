#!/usr/bin/env python3
"""Generate an animated, self-hosted dashboard from public GitHub repository metadata."""

from collections import Counter
from datetime import datetime, timezone
from html import escape
import json
import os
from pathlib import Path
from urllib.request import Request, urlopen

USERNAME = os.environ.get("GITHUB_USERNAME", "shivarajsg")
TOKEN = os.environ.get("GITHUB_TOKEN", "")
FEATURED_REPOSITORIES = (
    "PreAuth",
    "TenderBid",
    "graphrag-knowledge-pipeline",
    "ReliaLM",
    "autonomous_multi_agentic_ai",
    "OIL-Is-Well",
)
ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "assets" / "github-dashboard.svg"


def fetch_public_repositories():
    """Fetch every public repository owned by USERNAME using GitHub's REST API."""
    repositories = []
    page = 1
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "shivarajsg-profile-dashboard",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if TOKEN:
        headers["Authorization"] = "Bearer " + TOKEN

    while True:
        url = (
            "https://api.github.com/users/"
            + USERNAME
            + "/repos?type=owner&per_page=100&page="
            + str(page)
            + "&sort=updated"
        )
        request = Request(url, headers=headers)
        with urlopen(request, timeout=30) as response:
            batch = json.loads(response.read().decode("utf-8"))

        if not isinstance(batch, list):
            raise RuntimeError("GitHub API returned an unexpected repository response.")
        repositories.extend(
            repo for repo in batch
            if not repo.get("private", False) and repo.get("owner", {}).get("login", "").lower() == USERNAME.lower()
        )
        if len(batch) < 100:
            break
        page += 1

    return repositories


def render_dashboard(repositories):
    language_counts = Counter(
        repo.get("language")
        for repo in repositories
        if repo.get("language")
    )
    public_count = len(repositories)
    python_count = language_counts.get("Python", 0)
    stars_total = sum(int(repo.get("stargazers_count", 0) or 0) for repo in repositories)
    forks_total = sum(int(repo.get("forks_count", 0) or 0) for repo in repositories)
    language_rows = language_counts.most_common(5)
    max_language_count = max((count for _, count in language_rows), default=1)
    synced = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    parts = [
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 490" width="1200" height="490" role="img" aria-labelledby="title desc">',
        '<title id="title">Shivaraj GitHub engineering dashboard</title>',
        '<desc id="desc">A daily refreshed summary of public repositories, Python-primary repositories, featured AI systems, primary languages, and public stars and forks.</desc>',
        '<defs>',
        '<linearGradient id="bg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0b1120"/><stop offset="1" stop-color="#060914"/></linearGradient>',
        '<linearGradient id="bar" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#38bdf8"/><stop offset="1" stop-color="#818cf8"/></linearGradient>',
        '<linearGradient id="accent" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#38bdf8"/><stop offset="1" stop-color="#a78bfa"/></linearGradient>',
        '</defs>',
        '<style>',
        'text{font-family:ui-monospace,SFMono-Regular,Consolas,monospace}',
        '.muted{fill:#8492ad}.primary{fill:#e5edf9}.panel{fill:#10182a;stroke:#202b43;stroke-width:1}',
        '.bar{filter:drop-shadow(0 0 4px #38bdf822)}',
        '@keyframes pulse{0%,100%{opacity:.45}50%{opacity:1}}',
        '.pulse{animation:pulse 1.8s ease-in-out infinite}',
        '@media (prefers-reduced-motion:reduce){.pulse{animation:none;opacity:1}}',
        '</style>',
        '<rect width="1200" height="490" rx="22" fill="url(#bg)"/>',
    ]

    # Quiet grid texture.
    for x in range(60, 1200, 60):
        parts.append(f'<line x1="{x}" y1="0" x2="{x}" y2="490" stroke="#152039" stroke-width=".5" opacity=".55"/>')
    for y in range(50, 490, 50):
        parts.append(f'<line x1="0" y1="{y}" x2="1200" y2="{y}" stroke="#152039" stroke-width=".5" opacity=".4"/>')

    parts.extend([
        '<circle cx="67" cy="39" r="4" fill="#4ade80" class="pulse"/>',
        '<text x="82" y="43" font-size="10" letter-spacing="2.5" fill="#93c5fd">ENGINEERING TELEMETRY / PUBLIC REPOSITORIES</text>',
        f'<text x="1140" y="43" text-anchor="end" font-size="10" class="muted">SYNCED {escape(synced)}</text>',
        '<text x="60" y="83" font-size="27" font-weight="700" class="primary">Portfolio, in numbers.</text>',
        '<text x="60" y="104" font-size="11" class="muted">Verified repository metadata · refreshed daily · public repositories only</text>',
    ])

    cards = [
        ("PUBLIC REPOSITORIES", str(public_count), "Public repositories owned by this account", "#38bdf8"),
        ("PYTHON-PRIMARY REPOS", str(python_count), "Repos where GitHub reports Python as primary", "#a78bfa"),
        ("FEATURED AI SYSTEMS", str(len(FEATURED_REPOSITORIES)), "Curated engineering projects shown below", "#4ade80"),
    ]
    card_x = (60, 432, 804)
    for x, (label, value, subtitle, accent) in zip(card_x, cards):
        parts.extend([
            f'<rect x="{x}" y="125" width="336" height="102" rx="13" class="panel"/>',
            f'<rect x="{x}" y="125" width="3" height="102" rx="1.5" fill="{accent}"/>',
            f'<text x="{x+20}" y="151" font-size="10" letter-spacing="1.8" class="muted">{escape(label)}</text>',
            f'<text x="{x+20}" y="193" font-size="35" font-weight="700" class="primary">{escape(value)}</text>',
            f'<text x="{x+20}" y="213" font-size="10" class="muted">{escape(subtitle)}</text>',
        ])

    # Language distribution: counts represent repositories by GitHub's primary-language field, not lines of code.
    parts.extend([
        '<rect x="60" y="246" width="620" height="190" rx="14" class="panel"/>',
        '<text x="82" y="272" font-size="10" letter-spacing="1.8" fill="#c4b5fd">PRIMARY LANGUAGE MIX</text>',
        '<text x="658" y="272" text-anchor="end" font-size="9" class="muted">REPOSITORY COUNT</text>',
    ])
    if not language_rows:
        parts.append('<text x="82" y="315" font-size="12" class="muted">Language data is not available yet.</text>')
    else:
        for index, (language, count) in enumerate(language_rows):
            y = 300 + index * 25
            width = max(6, int(285 * count / max_language_count))
            delay = f"{0.12 * index:.2f}s"
            parts.extend([
                f'<text x="82" y="{y+11}" font-size="11" class="primary">{escape(language)}</text>',
                f'<rect x="235" y="{y}" width="285" height="13" rx="6.5" fill="#1b2740"/>',
                f'<rect class="bar" x="235" y="{y}" width="{width}" height="13" rx="6.5" fill="url(#bar)">',
                f'<animate attributeName="width" from="0" to="{width}" dur="0.9s" begin="{delay}" fill="freeze"/>',
                '</rect>',
                f'<text x="545" y="{y+11}" font-size="11" class="primary">{count}</text>',
                f'<text x="658" y="{y+11}" text-anchor="end" font-size="9" class="muted">{(count / max(1, public_count)) * 100:.0f}% of public repos</text>',
            ])

    # Fixed, factual areas of work—not fabricated activity metrics.
    parts.extend([
        '<rect x="700" y="246" width="440" height="190" rx="14" class="panel"/>',
        '<text x="722" y="272" font-size="10" letter-spacing="1.8" fill="#67e8f9">ENGINEERING FOCUS</text>',
    ])
    focus = [
        ("01", "RETRIEVAL SYSTEMS", "RAG · GraphRAG · evidence"),
        ("02", "AGENTIC WORKFLOWS", "tools · orchestration · state"),
        ("03", "LLM RELIABILITY", "evaluation · schemas · tracing"),
        ("04", "BACKEND SYSTEMS", "FastAPI · data · testing"),
    ]
    for i, (number, label, detail) in enumerate(focus):
        y = 300 + i * 31
        parts.extend([
            f'<circle cx="732" cy="{y}" r="10" fill="#14243b" stroke="#334766"/>',
            f'<text x="732" y="{y+3}" text-anchor="middle" font-size="8" fill="#7dd3fc">{number}</text>',
            f'<text x="752" y="{y+1}" font-size="10" class="primary">{escape(label)}</text>',
            f'<text x="752" y="{y+14}" font-size="9" class="muted">{escape(detail)}</text>',
            f'<circle cx="1113" cy="{y}" r="2.8" fill="#818cf8" class="pulse"/>',
        ])

    parts.extend([
        f'<text x="60" y="464" font-size="10" class="muted">PUBLIC SIGNALS · {stars_total} STARS · {forks_total} FORKS</text>',
        '<text x="1140" y="464" text-anchor="end" font-size="9" class="muted">SOURCE: GITHUB REST API · UTC SNAPSHOT</text>',
        '<rect x="60" y="478" width="1080" height="2" rx="1" fill="#17233b"/>',
        '<rect x="60" y="478" width="240" height="2" rx="1" fill="url(#accent)"/>',
        '</svg>',
    ])
    return "\n".join(parts) + "\n"


def main():
    repositories = fetch_public_repositories()
    if not repositories:
        raise RuntimeError("No public repositories were returned; refusing to publish an empty dashboard.")
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(render_dashboard(repositories), encoding="utf-8")
    print(
        "Updated dashboard: "
        + str(len(repositories))
        + " public repositories; "
        + str(sum(int(r.get("stargazers_count", 0) or 0) for r in repositories))
        + " stars; "
        + str(sum(int(r.get("forks_count", 0) or 0) for r in repositories))
        + " forks."
    )


if __name__ == "__main__":
    main()
