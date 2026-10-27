# Profile README maintenance

This repository is the public GitHub profile repository for [@shivarajsg](https://github.com/shivarajsg).

## Files

- <code>README.md</code> — the profile page. It uses a self-hosted animated SVG headline, skill icons, GitHub Stats Extended cards, and generated contribution-snake SVGs. The old header banner is no longer displayed.
- <code>assets/header.svg</code> — retained legacy artwork; it is not referenced by the current README.
- <code>.github/workflows/generate-snake.yml</code> — generates light and dark contribution-snake SVGs and publishes them to the <code>output</code> branch.

## Contribution animation

The workflow runs daily and can also be started manually from the repository's Actions tab. It publishes:

- <code>github-snake.svg</code>
- <code>github-snake-dark.svg</code>

The README loads these files from the <code>output</code> branch using raw.githubusercontent.com.

If the animation appears broken:

1. Open the [workflow runs](https://github.com/shivarajsg/shivarajsg/actions/workflows/generate-snake.yml).
2. Inspect the latest run and fix any failed step.
3. Confirm that both SVGs exist on the <code>output</code> branch.
4. Open the profile in GitHub and allow cached images to refresh.

The workflow requires repository Actions to be enabled and a token with permission to write repository contents. Keep the workflow permissions minimal and review third-party action changes before updating the pinned commit SHAs.

## External visuals

The headline animation lives in [assets/animated-headline.svg](https://github.com/shivarajsg/shivarajsg/blob/main/assets/animated-headline.svg), so it does not depend on a separate typing service. The stats cards use [GitHub Stats Extended](https://github.com/stats-organization/github-stats-extended), the actively maintained successor to github-readme-stats. These are external services; if a hosted endpoint becomes unavailable or rate-limited, remove or replace the affected image rather than allowing the README to accumulate broken widgets.
