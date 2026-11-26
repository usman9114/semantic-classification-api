# Brief: README hero and social preview

Date: 2026-11-26. Output: `docs/assets/hero-art.png` (AI illustration, no text), composed into `docs/assets/hero.png` (README banner) and `docs/assets/social-preview.png` (1280x640, upload in GitHub Settings → Social preview). The title and tagline are set in real type afterwards; the image model draws no text.

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

## Design

- **Subject:** an abstract 3D vector space. One bright query point (the sentence) with a soft glow. Three label points around it at different distances, each a small glowing sphere in its own colour; a thin luminous line connects the query to the nearest label, and that label glows brighter. Faint dotted lines to the two farther labels. Sparse field of tiny dim points in the background (other vectors), faint grid floor in perspective.
- **Composition:** wide, the cluster sits in the right two-thirds; the left third stays calm, dark negative space for the title set later. Slight isometric camera, depth of field.
- **Palette:** deep navy/ink background (#0B1020 range), FastAPI-adjacent teal (#05998B range) for the query and the winning link, muted violet and amber for the two losing labels, white highlights. High contrast, no neon overload.
- **Style:** clean technical illustration, soft glow, minimal, modern; not photoreal, no robots, no brains, no human figures, no circuit-board cliché.
- **Must not contain:** any text, letters, numbers, logos, brand marks, watermarks, borders or UI chrome.

## Prompt sent to the image model

See `docs/assets/hero-art.png.json` (sidecar) for the exact prompt, model and timing.
