# Profile README maintenance

This is the public profile repository for [@shivarajsg](https://github.com/shivarajsg).

## Active visuals

- `README.md` — profile introduction, six concise project cards, an architecture flowchart, dashboard, toolkit, and contribution animation.
- `assets/tech-sphere.svg` — self-hosted, animated rotating technology sphere adapted from the CC0 [Tech Sphere template](https://github.com/beydemirfurkan/awesome-github-profile/tree/main/templates/03-3d-immersive/tech-sphere).
- `assets/github-dashboard.svg` — animated repository dashboard generated from GitHub's public repository metadata.
- `scripts/update_profile_dashboard.py` — obtains public repository data from the GitHub REST API and generates the dashboard.
- `.github/workflows/update-profile-dashboard.yml` — refreshes the dashboard daily, on manual dispatch, and when its generator/workflow changes.
- `.github/workflows/generate-snake.yml` — generates the light and dark contribution-snake SVGs and publishes them to the `output` branch.

## Dashboard metrics

The dashboard only uses public repository data. It shows the number of public repositories, the number whose GitHub primary-language field is Python, the number of curated featured systems, primary-language counts by repository, and aggregate public stars/forks.

Language bars represent **repository counts**, not lines of code or coding time. The featured-system count is a curated profile setting in the generator, not a GitHub activity metric.

## Refresh and troubleshooting

1. Open the [profile dashboard workflow](https://github.com/shivarajsg/shivarajsg/actions/workflows/update-profile-dashboard.yml).
2. Choose **Run workflow** to refresh manually, or wait for its daily schedule.
3. The workflow updates `assets/github-dashboard.svg` only when content changes.
4. Open the latest workflow run if dashboard generation fails. The existing SVG is left intact when the script fails.
5. The contribution snake is maintained separately in the [snake workflow](https://github.com/shivarajsg/shivarajsg/actions/workflows/generate-snake.yml).

The dashboard workflow needs repository Actions enabled and `contents: write` permission so it can commit the generated SVG. Its push trigger is limited to the script and workflow files to avoid a loop when the generated dashboard is committed.

## Legacy artwork

`assets/header.svg`, `assets/animated-headline.svg`, `assets/typewriter-intro.svg`, and `assets/neon-pulse-banner.svg` are retained legacy assets; the current README does not reference them.
