# RESONATE — Complete Project Walkthrough

## Main deliverable

**[Open the 67-page PDF](RESONATE_Complete_Project_Walkthrough.pdf)**

A designed, searchable technical walkthrough with clickable contents and PDF bookmarks. It covers:

- The project idea, stated motivation, audience, and suggested first-person introduction
- All 26 explicit routes and the complete visitor journey
- Visual design, GPU graphics, custom shaders, motion, and procedural audio
- Each feature demo, the terminal parser, virtual filesystem, and local waitlist
- Domain models, state management, vector clocks, WebGPU/worker experiments, cryptography, and peer-network foundations
- The API/database scaffold, workspace tooling, migration, deployment boundaries, and build evidence
- A realistic next-step plan, five-minute presentation script, interview Q&A, and glossary
- All 370 baseline tracked files and every direct package declaration across the current workspace and preserved original

The document explicitly separates functioning interfaces, scripted demos, isolated foundations, future product goals, and unsupported marketing claims. First-person passages are suggested presentation language based on the repository, not invented personal biography or contribution history.

## Editable material

- `walkthrough.md` — the 33 main chapters in Markdown
- `reference-appendices.md` — generated code-study guides and full source/dependency references
- `build_pdf.py` — self-contained PDF builder with vector illustrations
- `requirements.txt` — pinned PDF-generation dependency

## Evidence

- `evidence/frontend-build.txt` — targeted Vite production build, passed
- `evidence/typecheck.txt` — workspace typecheck, failed on existing frontend errors
- `evidence/source-manifest.json` — baseline file paths, sizes, and SHA-256 hashes
- `evidence/pdf-layout.json` — PDF page map and layout sizing
- `evidence/pdf-validation.json` — PDF structural, text-boundary, and navigation checks

Reviewed baseline: `14fe27732222a28335c2cb7d45ea5fdf3bf95f8e`, 18 October 2026. No application source was changed to make the walkthrough. Node 22.22.3 and pnpm 10.32.1 were used for the recorded application checks; the Replit configuration specifies Node 24.

No browser E2E, real peer-network test, clinical evaluation, database integration test, or deployment test is represented as having passed. Build success is deliberately distinguished from TypeScript correctness.

## Rebuild

Requires Python 3 and the local DejaVu Sans / Sans Mono fonts available in the documented sandbox. To use other systems, adjust `FONTROOT` in the builder if needed.

```sh
python3 -m venv .venv-docs
.venv-docs/bin/pip install -r walkthrough/requirements.txt
.venv-docs/bin/python walkthrough/build_pdf.py
```

The builder uses no external web assets. It reads tracked repository files to refresh the appendix and source manifest, so the exact catalog will change if tracked source changes. The PDF's explanatory vector diagrams are not screenshots of a deployed application. PyMuPDF was used separately to inspect the resulting PDF; it is not required to rebuild it.
