# Brief: README hero and social preview

Date: 2026-11-26. Output: `docs/assets/hero-art.png` (AI illustration, no text), composed into `docs/assets/hero.jpg` (README banner) and `docs/assets/social-preview.jpg` (1280x640, upload in GitHub Settings → Social preview). The title and tagline are set in real type afterwards; the image model draws no text.

## What a newcomer must understand in two seconds

This API is zero-shot classification by meaning. You send one sentence and a few candidate labels; both are turned into vectors and the label whose vector sits closest to the sentence wins. No training, any labels.

## References (inspiration only, nothing copied or used as input)

| Reference | What works | Taken |
|---|---|---|
| [FastAPI README](https://github.com/fastapi/fastapi/blob/master/README.md) | One centred mark, one italic tagline, a small badge row | Calm hierarchy: one image, one line of text |
| [Qdrant README](https://github.com/qdrant/qdrant/blob/master/README.md) | Theme-aware header, tagline names the category, then a run command | Tagline names the category in plain words |
| [Chroma README](https://github.com/chroma-core/chroma/blob/main/README.md) | Light/dark wordmark, centred tagline | Works on light and dark GitHub themes: use a self-contained dark panel |
| [BentoML README](https://github.com/bentoml/BentoML/blob/main/README.md) | Banner states "build model inference APIs" | Say what the repo is, not a slogan |
| [sentence-transformers README](https://github.com/huggingface/sentence-transformers/blob/main/README.md) | No hero at all | Counter-example: decoration adds nothing; the art must explain the method |

Research note: none of the fetched ML API READMEs uses an illustrated hero. What we do differently: the illustration is the method (nearest label in embedding space), so it explains instead of decorating.

## Design (revised 2026-11-26)

- **Style:** Risograph paper-cut poster.
- **Why this picture:** Zero-shot classification is 'which label is nearest in meaning'. A compass choosing the nearest of three islands says that with no technical vocabulary.
- **Subject:** a large brass compass whose glowing needle points at the nearest of three paper-cut islands (coral with a striped lighthouse, then smaller mustard and teal ones joined by dotted routes) on layered paper waves. Cream paper grain, slight print misregistration. Palette: cream, coral, mustard, teal, ink navy.
- **Layout:** the left third stays quiet for the title; colours and font of the title are set per image in `compose_banner.py`.
- **Must not contain:** text, letters, numbers, logos, watermarks, borders, real people, robots.
- **QA:** schema check by a vision model against this brief, plus a manual look.

## Revision note

The first version of this banner used the same dark navy, teal and grid look as the owner's other repos. It was consistent but samey, so it was replaced with a distinct art direction per repo, each built on a metaphor for what the repo does.
