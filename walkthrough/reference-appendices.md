# RESONATE — generated reference appendices

## A1 — Read the code in this order
A guided source-study map


### Pass 1 — Understand the actual runtime
Read `artifacts/resonate/index.html`, `src/main.tsx`, and `src/App.tsx`. Trace the root element, CSS import, provider nesting, loader gate, and explicit route switch. Then read `vite.config.ts` to understand aliases, shader imports, ports, and output paths. This prevents treating the preserved Next.js structure as active framework behavior.

### Pass 2 — Follow a real user event
Read `presentation/layouts/AppProvider.tsx`, `presentation/components/animations/CinematicLoader.tsx`, and `infrastructure/audio/AcousticResonator.ts`. Follow one click from state change through AudioContext initialization, timers, Anime.js transition, and route-content mount. Note exactly which timers and resources have cleanup.

### Pass 3 — Study the most complete interactive page
Read Terminal's types and `FS`, then `runCommand`, onboarding branches, keyboard handler, and log renderer. Draw the phases on paper. Follow a successful and an invalid join input. Search for `localStorage` and identify the actual record rather than repeating the success message.

### Pass 4 — Trace one graphics frame
Read `NeuralNetworkCanvas.tsx`, `neural.vert`, and `neural.frag`. Identify geometry attributes, uniforms, material settings, pointer normalization, and the `useFrame` update. Compare with FluidCanvas, where JavaScript updates thousands of instances each frame instead of moving the whole animation into a vertex shader.

### Pass 5 — Separate demo from infrastructure
Read Echo Studio and AdvancedChat before reading NeuralComputeNode and the sentiment worker. Search for calls connecting them: a nearby folder or similarly named concept does not establish an integration. Repeat this check for CipherProtocol, PeerTopologyMesh, EventBus, Zustand, and LWWMap.

### Pass 6 — Inspect backend contracts and evidence
Read `lib/api-spec/openapi.yaml`, generated health client/validator, Express routing, and the empty DB schema. Finish with the build/typecheck logs. Compare every marketing guarantee with the implementation it would require.

**Evidence:** all paths above are present in the baseline; the next appendices index the full tracked repository and declared package set.


## A2 — More scenes, under the microscope
What the names really mean


### Not all particle scenes use the same technique
CinematicLoaderCanvas uses 25,000 colored points in a tunnel-like distribution. MeshTopologyCanvas builds a sphere-like arrangement of nodes and connecting line segments. DNAHelixCanvas uses 3,000 points in two alternating strands with time-varying movement. These are mathematical visualizations, not network or genomic data.

GlobeCanvas distributes 3,000 points over a sphere using a formula based on index/angle. It colors a selected region and rotates the scene. The “impact globe” does not fetch a live map of students. VectorFieldCanvas draws an instanced cone grid whose orientations respond to pointer distance. It illustrates a field but is not the vector-clock implementation.

### FluidCanvas is CPU-updated instancing
The fluid scene uses 10,000 instances with randomized motion parameters. Each frame iterates the particles, computes trigonometric positions and orientation, updates matrices/colors, and marks instance buffers dirty. Instancing reduces draw-call overhead, but these per-instance calculations still run in JavaScript. Its comment about “WGSL-like logic” does not make it a WebGPU compute shader.

### Other specialized scenes
AudioVisualizerCanvas deforms a plane using layered sine/cosine waves and a center pulse. It does not read microphone spectrum data or an AnalyserNode. RoadmapCanvas creates a Catmull–Rom spline and maps scroll progress to camera movement along negative Z. PrismCanvas rotates an icosahedron with custom glass shaders and an inner dark core. SingularityCanvas is an elaborate 150,000-point experimental scene with postprocessing imports and pointer-velocity input.

### A concrete performance improvement
FluidCanvas allocates Color objects inside its per-particle frame loop. Reusing scratch objects and precomputed endpoint colors would reduce allocation pressure. Scene work should also pause when offscreen or hidden, scale with device capability, and dispose resources reliably. Do not use a synthetic animated “memory” label as a substitute for profiling.

### Shader path audit
PrismCanvas imports `../shaders/glass.*` even though it lives in the nested `canvas/premium` directory. That relative path does not point to the sibling presentation shader directory. It is an inactive-source maintenance hazard: importing that component into a live route would require fixing resolution and testing it. Successful current bundling does not validate every unreferenced scene.

**Evidence:** all eleven files in `src/presentation/canvas/`, including nested scene directories; custom shader import paths; build log.


## A3 — A test plan you can explain
From source inspection to dependable behavior


### Unit tests for the foundations
Test EmotionalState boundaries, NaN/nonfinite input, and arousal/dominance validation. Test User event payloads, stable identity, and event clearing. Test circles at zero/full capacity, duplicate joins, repeated leaves, and inconsistent initial participants. Replace event `@ts-ignore` contracts with a typed union before relying on handlers.

For clocks, test equality, dominance, concurrency, partial client sets, and repeated merges. Property-style tests should check commutativity, associativity, and idempotence under the intended merge contract. Add clock skew, tied timestamps, serialization round-trips, and deletion behavior. A passing example is not a convergence proof.

### Integration tests for sensitive operations
Test encryption/decryption round-trip, wrong keys, altered ciphertext, fresh IVs, stored salt/IV encoding, and failure recovery. Test GPU input lengths and unsupported-device behavior separately from model accuracy. Test peer negotiation with real signaling, disconnect/reconnect, permission denial, and relay-only connectivity once those features exist.

### Browser tests for the existing prototype
Verify all 26 routes and direct deep links, the 404, menu focus, touch navigation, context-menu edges, and base-path deployment. Exercise loader completion and unavailable audio. Confirm transcript timing and scripted chat behavior; use fake timers to catch callbacks surviving unmount. Verify terminal input validation, command history, path navigation, and blocked/quota-full localStorage.

### Performance and accessibility checks
Measure initial transfer, parse/execute time, long tasks, frame rate, and memory on representative low-end phones. Check re-entry after route changes. Audit focus order, names/labels, contrast, heading hierarchy, reduced motion, zoom, and screen-reader announcement of streaming logs. The viewport's `maximum-scale=1` deserves removal/review to support user zoom.

### What is not already proven
No test scripts or automated product test suite in the inspected manifests establish these guarantees today. The two executed validation commands check type correctness and bundle construction, not all runtime or safety behavior. Treat this page as an actionable plan.

**Evidence basis:** current source structure, lifecycle patterns, declarations, and recorded validation output. Proposed tests have not been claimed as executed.


## B1 — Complete repository file catalog
ROOT / workspace and deployment


| PATH (relative to the scope above) | SIZE / SCALE |
|---|---|
| .gitignore | 49 lines |
| .npmrc | 2 lines |
| .replit | 32 lines |
| .replitignore | 5 lines |
| package.json | 16 lines |
| pnpm-lock.yaml | 6,296 lines |
| pnpm-workspace.yaml | 160 lines |
| replit.md | 57 lines |
| tsconfig.base.json | 26 lines |
| tsconfig.json | 16 lines |
| vercel.json | 12 lines |
Every tracked baseline file is indexed once in this catalog. Third-party node_modules, generated build output, .git internals, and the new walkthrough files are excluded. Line counts are file scale, not a measure of original authorship. Migration and UI scaffolds are listed without implying active runtime use.

## B2 — Complete repository file catalog
FRONTEND / artifacts/resonate


| PATH (relative to the scope above) | SIZE / SCALE |
|---|---|
| .replit-artifact/artifact.toml | 31 lines |
| components.json | 20 lines |
| index.html | 24 lines |
| package.json | 87 lines |
| public/favicon.svg | 3 lines |
| public/file.svg | 1 lines |
| public/globe.svg | 1 lines |
| public/next.svg | 1 lines |
| public/opengraph.jpg | 120,056 bytes |
| public/robots.txt | 2 lines |
| public/vercel.svg | 1 lines |
| public/window.svg | 1 lines |
| src/App.tsx | 93 lines |
| src/app/about/page.tsx | 74 lines |
| src/app/archives/page.tsx | 36 lines |
| src/app/blog/page.tsx | 47 lines |
| src/app/careers/page.tsx | 48 lines |
| src/app/crdt/page.tsx | 40 lines |
| src/app/engine/page.tsx | 116 lines |
| src/app/favicon.ico | 25,931 bytes |
| src/app/features/echo-studio/page.tsx | 97 lines |
| src/app/features/empathy-coach/page.tsx | 44 lines |
| src/app/features/heritage-echoes/page.tsx | 43 lines |
| src/app/features/mood-genome/page.tsx | 64 lines |
| src/app/features/page.tsx | 46 lines |
| src/app/features/resoquests/page.tsx | 61 lines |
Every tracked baseline file is indexed once in this catalog. Third-party node_modules, generated build output, .git internals, and the new walkthrough files are excluded. Line counts are file scale, not a measure of original authorship. Migration and UI scaffolds are listed without implying active runtime use.

## B3 — Complete repository file catalog
FRONTEND / artifacts/resonate · continued


| PATH (relative to the scope above) | SIZE / SCALE |
|---|---|
| src/app/features/safe-circles/page.tsx | 46 lines |
| src/app/founders/page.tsx | 165 lines |
| src/app/globals.css | 129 lines |
| src/app/impact/page.tsx | 81 lines |
| src/app/join/page.tsx | 56 lines |
| src/app/manifesto/page.tsx | 53 lines |
| src/app/not-found.tsx | 39 lines |
| src/app/page.tsx | 195 lines |
| src/app/privacy/page.tsx | 37 lines |
| src/app/protocol/page.tsx | 37 lines |
| src/app/roadmap/page.tsx | 109 lines |
| src/app/schools/page.tsx | 78 lines |
| src/app/technology/page.tsx | 73 lines |
| src/app/telemetry/page.tsx | 42 lines |
| src/app/terminal/page.tsx | 973 lines |
| src/app/terms/page.tsx | 32 lines |
| src/components/animations/LoadingScreen.tsx | 101 lines |
| src/components/canvas/HeroCanvas.tsx | 68 lines |
| src/components/layout/AppProvider.tsx | 17 lines |
| src/components/layout/LenisProvider.tsx | 31 lines |
| src/core/cqrs/Entity.ts | 31 lines |
| src/core/cqrs/EventBus.ts | 35 lines |
| src/core/crdt/VectorClock.ts | 121 lines |
| src/core/memory/GarbageCollector.ts | 81 lines |
| src/domain/entities/ResonanceCircle.ts | 60 lines |
| src/domain/entities/User.ts | 48 lines |
Every tracked baseline file is indexed once in this catalog. Third-party node_modules, generated build output, .git internals, and the new walkthrough files are excluded. Line counts are file scale, not a measure of original authorship. Migration and UI scaffolds are listed without implying active runtime use.

## B4 — Complete repository file catalog
FRONTEND / artifacts/resonate · continued


| PATH (relative to the scope above) | SIZE / SCALE |
|---|---|
| src/domain/value-objects/EmotionalState.ts | 45 lines |
| src/hooks/use-mobile.tsx | 19 lines |
| src/hooks/use-toast.ts | 191 lines |
| src/index.css | 143 lines |
| src/infrastructure/ai/webgpu/NeuralComputeNode.ts | 120 lines |
| src/infrastructure/audio/AcousticResonator.ts | 148 lines |
| src/infrastructure/crypto/CipherProtocol.ts | 63 lines |
| src/infrastructure/telemetry/AnonymizedMetrics.ts | 45 lines |
| src/infrastructure/webrtc/PeerTopologyMesh.ts | 95 lines |
| src/lib/utils.ts | 6 lines |
| src/main.tsx | 5 lines |
| src/pages/not-found.tsx | 21 lines |
| src/presentation/canvas/CinematicLoaderCanvas.tsx | 100 lines |
| src/presentation/canvas/MeshTopologyCanvas.tsx | 101 lines |
| src/presentation/canvas/NeuralNetworkCanvas.tsx | 93 lines |
| src/presentation/canvas/SingularityCanvas.tsx | 144 lines |
| src/presentation/canvas/archives/DNAHelixCanvas.tsx | 95 lines |
| src/presentation/canvas/audio/AudioVisualizerCanvas.tsx | 60 lines |
| src/presentation/canvas/fluid/FluidCanvas.tsx | 86 lines |
| src/presentation/canvas/impact/GlobeCanvas.tsx | 94 lines |
| src/presentation/canvas/premium/PrismCanvas.tsx | 59 lines |
| src/presentation/canvas/roadmap/RoadmapCanvas.tsx | 76 lines |
| src/presentation/canvas/vector/VectorFieldCanvas.tsx | 110 lines |
| src/presentation/components/CustomCursor.tsx | 65 lines |
| src/presentation/components/MagneticElement.tsx | 51 lines |
| src/presentation/components/MatrixRain.tsx | 73 lines |
Every tracked baseline file is indexed once in this catalog. Third-party node_modules, generated build output, .git internals, and the new walkthrough files are excluded. Line counts are file scale, not a measure of original authorship. Migration and UI scaffolds are listed without implying active runtime use.

## B5 — Complete repository file catalog
FRONTEND / artifacts/resonate · continued


| PATH (relative to the scope above) | SIZE / SCALE |
|---|---|
| src/presentation/components/PurgeScreen.tsx | 81 lines |
| src/presentation/components/ScrambleText.tsx | 43 lines |
| src/presentation/components/TextReveal.tsx | 37 lines |
| src/presentation/components/animations/CinematicLoader.tsx | 152 lines |
| src/presentation/components/chat/AdvancedChat.tsx | 136 lines |
| src/presentation/components/navigation/GlobalNav.tsx | 120 lines |
| src/presentation/components/transitions/TransitionShutter.tsx | 60 lines |
| src/presentation/components/ui/CinematicText.tsx | 41 lines |
| src/presentation/components/ui/ContextMenu.tsx | 55 lines |
| src/presentation/hooks/useGSAPOrchestrator.ts | 37 lines |
| src/presentation/layouts/AppProvider.tsx | 20 lines |
| src/presentation/layouts/LenisProvider.tsx | 31 lines |
| src/presentation/shaders/glass.frag | 32 lines |
| src/presentation/shaders/glass.vert | 12 lines |
| src/presentation/shaders/neural.frag | 11 lines |
| src/presentation/shaders/neural.vert | 132 lines |
| src/presentation/shaders/singularity.frag | 13 lines |
| src/presentation/shaders/singularity.vert | 76 lines |
| src/presentation/store/empathyStore.ts | 29 lines |
| src/workers/sentiment.worker.ts | 40 lines |
| tsconfig.json | 24 lines |
| vite.config.ts | 71 lines |
Every tracked baseline file is indexed once in this catalog. Third-party node_modules, generated build output, .git internals, and the new walkthrough files are excluded. Line counts are file scale, not a measure of original authorship. Migration and UI scaffolds are listed without implying active runtime use.

## B6 — Complete repository file catalog
UI LIBRARY / artifacts/resonate/src/components/ui


| PATH (relative to the scope above) | SIZE / SCALE |
|---|---|
| accordion.tsx | 55 lines |
| alert-dialog.tsx | 139 lines |
| alert.tsx | 59 lines |
| aspect-ratio.tsx | 5 lines |
| avatar.tsx | 50 lines |
| badge.tsx | 43 lines |
| breadcrumb.tsx | 115 lines |
| button-group.tsx | 83 lines |
| button.tsx | 65 lines |
| calendar.tsx | 213 lines |
| card.tsx | 76 lines |
| carousel.tsx | 260 lines |
| chart.tsx | 367 lines |
| checkbox.tsx | 28 lines |
| collapsible.tsx | 11 lines |
| command.tsx | 153 lines |
| context-menu.tsx | 198 lines |
| dialog.tsx | 120 lines |
| drawer.tsx | 116 lines |
| dropdown-menu.tsx | 201 lines |
| empty.tsx | 104 lines |
| field.tsx | 244 lines |
| form.tsx | 176 lines |
| hover-card.tsx | 27 lines |
| input-group.tsx | 168 lines |
| input-otp.tsx | 69 lines |
Every tracked baseline file is indexed once in this catalog. Third-party node_modules, generated build output, .git internals, and the new walkthrough files are excluded. Line counts are file scale, not a measure of original authorship. Migration and UI scaffolds are listed without implying active runtime use.

## B7 — Complete repository file catalog
UI LIBRARY / artifacts/resonate/src/components/ui · continued


| PATH (relative to the scope above) | SIZE / SCALE |
|---|---|
| input.tsx | 22 lines |
| item.tsx | 193 lines |
| kbd.tsx | 28 lines |
| label.tsx | 26 lines |
| menubar.tsx | 254 lines |
| navigation-menu.tsx | 128 lines |
| pagination.tsx | 117 lines |
| popover.tsx | 31 lines |
| progress.tsx | 28 lines |
| radio-group.tsx | 42 lines |
| resizable.tsx | 45 lines |
| scroll-area.tsx | 46 lines |
| select.tsx | 159 lines |
| separator.tsx | 29 lines |
| sheet.tsx | 140 lines |
| sidebar.tsx | 727 lines |
| skeleton.tsx | 15 lines |
| slider.tsx | 26 lines |
| sonner.tsx | 31 lines |
| spinner.tsx | 16 lines |
| switch.tsx | 27 lines |
| table.tsx | 120 lines |
| tabs.tsx | 53 lines |
| textarea.tsx | 22 lines |
| toast.tsx | 127 lines |
| toaster.tsx | 33 lines |
Every tracked baseline file is indexed once in this catalog. Third-party node_modules, generated build output, .git internals, and the new walkthrough files are excluded. Line counts are file scale, not a measure of original authorship. Migration and UI scaffolds are listed without implying active runtime use.

## B8 — Complete repository file catalog
UI LIBRARY / artifacts/resonate/src/components/ui · continued


| PATH (relative to the scope above) | SIZE / SCALE |
|---|---|
| toggle-group.tsx | 61 lines |
| toggle.tsx | 43 lines |
| tooltip.tsx | 32 lines |
Every tracked baseline file is indexed once in this catalog. Third-party node_modules, generated build output, .git internals, and the new walkthrough files are excluded. Line counts are file scale, not a measure of original authorship. Migration and UI scaffolds are listed without implying active runtime use.

## B9 — Complete repository file catalog
SERVICES + LIBRARIES / repository-relative


| PATH (relative to the scope above) | SIZE / SCALE |
|---|---|
| artifacts/api-server/.replit-artifact/artifact.toml | 32 lines |
| artifacts/api-server/build.mjs | 126 lines |
| artifacts/api-server/package.json | 32 lines |
| artifacts/api-server/src/app.ts | 34 lines |
| artifacts/api-server/src/index.ts | 25 lines |
| artifacts/api-server/src/lib/.gitkeep | 0 lines |
| artifacts/api-server/src/lib/logger.ts | 20 lines |
| artifacts/api-server/src/middlewares/.gitkeep | 0 lines |
| artifacts/api-server/src/routes/health.ts | 11 lines |
| artifacts/api-server/src/routes/index.ts | 8 lines |
| artifacts/api-server/tsconfig.json | 19 lines |
| lib/api-client-react/package.json | 15 lines |
| lib/api-client-react/src/custom-fetch.ts | 371 lines |
| lib/api-client-react/src/generated/api.schemas.ts | 10 lines |
| lib/api-client-react/src/generated/api.ts | 101 lines |
| lib/api-client-react/src/index.ts | 4 lines |
| lib/api-client-react/tsconfig.json | 12 lines |
| lib/api-spec/openapi.yaml | 36 lines |
| lib/api-spec/orval.config.ts | 72 lines |
| lib/api-spec/package.json | 11 lines |
| lib/api-zod/package.json | 12 lines |
| lib/api-zod/src/generated/api.ts | 16 lines |
| lib/api-zod/src/generated/types/healthStatus.ts | 11 lines |
| lib/api-zod/src/generated/types/index.ts | 9 lines |
| lib/api-zod/src/index.ts | 2 lines |
| lib/api-zod/tsconfig.json | 11 lines |
Every tracked baseline file is indexed once in this catalog. Third-party node_modules, generated build output, .git internals, and the new walkthrough files are excluded. Line counts are file scale, not a measure of original authorship. Migration and UI scaffolds are listed without implying active runtime use.

## B10 — Complete repository file catalog
SERVICES + LIBRARIES / repository-relative · continued


| PATH (relative to the scope above) | SIZE / SCALE |
|---|---|
| lib/db/drizzle.config.ts | 14 lines |
| lib/db/package.json | 25 lines |
| lib/db/src/index.ts | 16 lines |
| lib/db/src/schema/index.ts | 20 lines |
| lib/db/tsconfig.json | 12 lines |
| scripts/package.json | 14 lines |
| scripts/post-merge.sh | 4 lines |
| scripts/src/hello.ts | 1 lines |
| scripts/tsconfig.json | 9 lines |
Every tracked baseline file is indexed once in this catalog. Third-party node_modules, generated build output, .git internals, and the new walkthrough files are excluded. Line counts are file scale, not a measure of original authorship. Migration and UI scaffolds are listed without implying active runtime use.

## B11 — Complete repository file catalog
PREVIEW SANDBOX / artifacts/mockup-sandbox


| PATH (relative to the scope above) | SIZE / SCALE |
|---|---|
| .replit-artifact/artifact.toml | 17 lines |
| components.json | 21 lines |
| index.html | 31 lines |
| mockupPreviewPlugin.ts | 180 lines |
| package.json | 74 lines |
| src/.generated/mockup-components.ts | 5 lines |
| src/App.tsx | 146 lines |
| src/components/ui/accordion.tsx | 55 lines |
| src/components/ui/alert-dialog.tsx | 139 lines |
| src/components/ui/alert.tsx | 59 lines |
| src/components/ui/aspect-ratio.tsx | 5 lines |
| src/components/ui/avatar.tsx | 50 lines |
| src/components/ui/badge.tsx | 37 lines |
| src/components/ui/breadcrumb.tsx | 115 lines |
| src/components/ui/button-group.tsx | 83 lines |
| src/components/ui/button.tsx | 58 lines |
| src/components/ui/calendar.tsx | 213 lines |
| src/components/ui/card.tsx | 76 lines |
| src/components/ui/carousel.tsx | 260 lines |
| src/components/ui/chart.tsx | 365 lines |
| src/components/ui/checkbox.tsx | 28 lines |
| src/components/ui/collapsible.tsx | 11 lines |
| src/components/ui/command.tsx | 153 lines |
| src/components/ui/context-menu.tsx | 198 lines |
| src/components/ui/dialog.tsx | 120 lines |
| src/components/ui/drawer.tsx | 116 lines |
Every tracked baseline file is indexed once in this catalog. Third-party node_modules, generated build output, .git internals, and the new walkthrough files are excluded. Line counts are file scale, not a measure of original authorship. Migration and UI scaffolds are listed without implying active runtime use.

## B12 — Complete repository file catalog
PREVIEW SANDBOX / artifacts/mockup-sandbox · continued


| PATH (relative to the scope above) | SIZE / SCALE |
|---|---|
| src/components/ui/dropdown-menu.tsx | 201 lines |
| src/components/ui/empty.tsx | 104 lines |
| src/components/ui/field.tsx | 244 lines |
| src/components/ui/form.tsx | 176 lines |
| src/components/ui/hover-card.tsx | 27 lines |
| src/components/ui/input-group.tsx | 165 lines |
| src/components/ui/input-otp.tsx | 69 lines |
| src/components/ui/input.tsx | 22 lines |
| src/components/ui/item.tsx | 193 lines |
| src/components/ui/kbd.tsx | 28 lines |
| src/components/ui/label.tsx | 26 lines |
| src/components/ui/menubar.tsx | 254 lines |
| src/components/ui/navigation-menu.tsx | 128 lines |
| src/components/ui/pagination.tsx | 117 lines |
| src/components/ui/popover.tsx | 31 lines |
| src/components/ui/progress.tsx | 28 lines |
| src/components/ui/radio-group.tsx | 42 lines |
| src/components/ui/resizable.tsx | 45 lines |
| src/components/ui/scroll-area.tsx | 46 lines |
| src/components/ui/select.tsx | 159 lines |
| src/components/ui/separator.tsx | 29 lines |
| src/components/ui/sheet.tsx | 140 lines |
| src/components/ui/sidebar.tsx | 714 lines |
| src/components/ui/skeleton.tsx | 15 lines |
| src/components/ui/slider.tsx | 26 lines |
| src/components/ui/sonner.tsx | 31 lines |
Every tracked baseline file is indexed once in this catalog. Third-party node_modules, generated build output, .git internals, and the new walkthrough files are excluded. Line counts are file scale, not a measure of original authorship. Migration and UI scaffolds are listed without implying active runtime use.

## B13 — Complete repository file catalog
PREVIEW SANDBOX / artifacts/mockup-sandbox · continued


| PATH (relative to the scope above) | SIZE / SCALE |
|---|---|
| src/components/ui/spinner.tsx | 16 lines |
| src/components/ui/switch.tsx | 27 lines |
| src/components/ui/table.tsx | 120 lines |
| src/components/ui/tabs.tsx | 53 lines |
| src/components/ui/textarea.tsx | 22 lines |
| src/components/ui/toast.tsx | 127 lines |
| src/components/ui/toaster.tsx | 33 lines |
| src/components/ui/toggle-group.tsx | 61 lines |
| src/components/ui/toggle.tsx | 43 lines |
| src/components/ui/tooltip.tsx | 32 lines |
| src/hooks/use-mobile.tsx | 19 lines |
| src/hooks/use-toast.ts | 189 lines |
| src/index.css | 185 lines |
| src/lib/utils.ts | 6 lines |
| src/main.tsx | 5 lines |
| tsconfig.json | 18 lines |
| vite.config.ts | 71 lines |
Every tracked baseline file is indexed once in this catalog. Third-party node_modules, generated build output, .git internals, and the new walkthrough files are excluded. Line counts are file scale, not a measure of original authorship. Migration and UI scaffolds are listed without implying active runtime use.

## B14 — Complete repository file catalog
MIGRATION BACKUP / .migration-backup


| PATH (relative to the scope above) | SIZE / SCALE |
|---|---|
| .gitignore | 41 lines |
| .replit | 6 lines |
| AGENTS.md | 5 lines |
| CLAUDE.md | 1 lines |
| IDEAS.md | 39 lines |
| README.md | 36 lines |
| eslint.config.mjs | 18 lines |
| next.config.ts | 29 lines |
| package-lock.json | 8,301 lines |
| package.json | 44 lines |
| postcss.config.mjs | 7 lines |
| public/file.svg | 1 lines |
| public/globe.svg | 1 lines |
| public/next.svg | 1 lines |
| public/vercel.svg | 1 lines |
| public/window.svg | 1 lines |
| src/app/about/page.tsx | 74 lines |
| src/app/archives/page.tsx | 36 lines |
| src/app/blog/page.tsx | 47 lines |
| src/app/careers/page.tsx | 48 lines |
| src/app/crdt/page.tsx | 40 lines |
| src/app/engine/page.tsx | 116 lines |
| src/app/favicon.ico | 25,931 bytes |
| src/app/features/echo-studio/page.tsx | 97 lines |
| src/app/features/empathy-coach/page.tsx | 44 lines |
| src/app/features/heritage-echoes/page.tsx | 43 lines |
Every tracked baseline file is indexed once in this catalog. Third-party node_modules, generated build output, .git internals, and the new walkthrough files are excluded. Line counts are file scale, not a measure of original authorship. Migration and UI scaffolds are listed without implying active runtime use.

## B15 — Complete repository file catalog
MIGRATION BACKUP / .migration-backup · continued


| PATH (relative to the scope above) | SIZE / SCALE |
|---|---|
| src/app/features/mood-genome/page.tsx | 64 lines |
| src/app/features/page.tsx | 46 lines |
| src/app/features/resoquests/page.tsx | 61 lines |
| src/app/features/safe-circles/page.tsx | 46 lines |
| src/app/founders/page.tsx | 106 lines |
| src/app/globals.css | 129 lines |
| src/app/impact/page.tsx | 81 lines |
| src/app/join/page.tsx | 56 lines |
| src/app/layout.tsx | 39 lines |
| src/app/manifesto/page.tsx | 53 lines |
| src/app/not-found.tsx | 39 lines |
| src/app/page.tsx | 195 lines |
| src/app/privacy/page.tsx | 37 lines |
| src/app/protocol/page.tsx | 37 lines |
| src/app/roadmap/page.tsx | 109 lines |
| src/app/schools/page.tsx | 78 lines |
| src/app/technology/page.tsx | 73 lines |
| src/app/telemetry/page.tsx | 42 lines |
| src/app/template.tsx | 8 lines |
| src/app/terminal/page.tsx | 177 lines |
| src/app/terms/page.tsx | 32 lines |
| src/components/animations/LoadingScreen.tsx | 101 lines |
| src/components/canvas/HeroCanvas.tsx | 68 lines |
| src/components/layout/AppProvider.tsx | 17 lines |
| src/components/layout/LenisProvider.tsx | 31 lines |
| src/core/cqrs/Entity.ts | 31 lines |
Every tracked baseline file is indexed once in this catalog. Third-party node_modules, generated build output, .git internals, and the new walkthrough files are excluded. Line counts are file scale, not a measure of original authorship. Migration and UI scaffolds are listed without implying active runtime use.

## B16 — Complete repository file catalog
MIGRATION BACKUP / .migration-backup · continued


| PATH (relative to the scope above) | SIZE / SCALE |
|---|---|
| src/core/cqrs/EventBus.ts | 35 lines |
| src/core/crdt/VectorClock.ts | 121 lines |
| src/core/memory/GarbageCollector.ts | 81 lines |
| src/domain/entities/ResonanceCircle.ts | 60 lines |
| src/domain/entities/User.ts | 48 lines |
| src/domain/value-objects/EmotionalState.ts | 45 lines |
| src/infrastructure/ai/webgpu/NeuralComputeNode.ts | 120 lines |
| src/infrastructure/audio/AcousticResonator.ts | 148 lines |
| src/infrastructure/crypto/CipherProtocol.ts | 63 lines |
| src/infrastructure/telemetry/AnonymizedMetrics.ts | 45 lines |
| src/infrastructure/webrtc/PeerTopologyMesh.ts | 95 lines |
| src/presentation/canvas/CinematicLoaderCanvas.tsx | 100 lines |
| src/presentation/canvas/MeshTopologyCanvas.tsx | 101 lines |
| src/presentation/canvas/NeuralNetworkCanvas.tsx | 93 lines |
| src/presentation/canvas/SingularityCanvas.tsx | 144 lines |
| src/presentation/canvas/archives/DNAHelixCanvas.tsx | 95 lines |
| src/presentation/canvas/audio/AudioVisualizerCanvas.tsx | 60 lines |
| src/presentation/canvas/fluid/FluidCanvas.tsx | 86 lines |
| src/presentation/canvas/impact/GlobeCanvas.tsx | 94 lines |
| src/presentation/canvas/premium/PrismCanvas.tsx | 59 lines |
| src/presentation/canvas/roadmap/RoadmapCanvas.tsx | 76 lines |
| src/presentation/canvas/vector/VectorFieldCanvas.tsx | 110 lines |
| src/presentation/components/CustomCursor.tsx | 65 lines |
| src/presentation/components/MagneticElement.tsx | 51 lines |
| src/presentation/components/MatrixRain.tsx | 73 lines |
| src/presentation/components/PurgeScreen.tsx | 81 lines |
Every tracked baseline file is indexed once in this catalog. Third-party node_modules, generated build output, .git internals, and the new walkthrough files are excluded. Line counts are file scale, not a measure of original authorship. Migration and UI scaffolds are listed without implying active runtime use.

## B17 — Complete repository file catalog
MIGRATION BACKUP / .migration-backup · continued


| PATH (relative to the scope above) | SIZE / SCALE |
|---|---|
| src/presentation/components/ScrambleText.tsx | 43 lines |
| src/presentation/components/TextReveal.tsx | 37 lines |
| src/presentation/components/animations/CinematicLoader.tsx | 153 lines |
| src/presentation/components/chat/AdvancedChat.tsx | 136 lines |
| src/presentation/components/navigation/GlobalNav.tsx | 120 lines |
| src/presentation/components/transitions/TransitionShutter.tsx | 60 lines |
| src/presentation/components/ui/CinematicText.tsx | 41 lines |
| src/presentation/components/ui/ContextMenu.tsx | 55 lines |
| src/presentation/hooks/useGSAPOrchestrator.ts | 37 lines |
| src/presentation/layouts/AppProvider.tsx | 20 lines |
| src/presentation/layouts/LenisProvider.tsx | 31 lines |
| src/presentation/shaders/glass.frag | 32 lines |
| src/presentation/shaders/glass.vert | 12 lines |
| src/presentation/shaders/neural.frag | 11 lines |
| src/presentation/shaders/neural.vert | 132 lines |
| src/presentation/shaders/singularity.frag | 13 lines |
| src/presentation/shaders/singularity.vert | 76 lines |
| src/presentation/store/empathyStore.ts | 29 lines |
| src/workers/sentiment.worker.ts | 40 lines |
| tsconfig.json | 35 lines |
Every tracked baseline file is indexed once in this catalog. Third-party node_modules, generated build output, .git internals, and the new walkthrough files are excluded. Line counts are file scale, not a measure of original authorship. Migration and UI scaffolds are listed without implying active runtime use.

## B18 — Complete repository file catalog
ATTACHMENTS / attached_assets


| PATH (relative to the scope above) | SIZE / SCALE |
|---|---|
| 4b70fb0a802ae4e14bed695f3e576db9_1781772643839.jpg | 27,931 bytes |
| g1h7uuanzez51_1781772614449.jpg | 35,195 bytes |
Every tracked baseline file is indexed once in this catalog. Third-party node_modules, generated build output, .git internals, and the new walkthrough files are excluded. Line counts are file scale, not a measure of original authorship. Migration and UI scaffolds are listed without implying active runtime use.

## C1 — Every declared package
Dependency reference · active workspace and preserved original


| PACKAGE | DECLARED VERSION | ROLE / DECLARING SCOPE |
|---|---|---|
| @gsap/react | ^2.1.2 | React/GSAP integration helper · OLD, WEB |
| @hookform/resolvers | ^3.10.0 | Form/schema adapters · PREVIEW, WEB |
| @radix-ui/react-accordion | ^1.2.12 | Accessible UI primitive: accordion · PREVIEW |
| @radix-ui/react-accordion | ^1.2.4 | Accessible UI primitive: accordion · WEB |
| @radix-ui/react-alert-dialog | ^1.1.15 | Accessible UI primitive: alert dialog · PREVIEW |
| @radix-ui/react-alert-dialog | ^1.1.7 | Accessible UI primitive: alert dialog · WEB |
| @radix-ui/react-aspect-ratio | ^1.1.3 | Accessible UI primitive: aspect ratio · WEB |
| @radix-ui/react-aspect-ratio | ^1.1.8 | Accessible UI primitive: aspect ratio · PREVIEW |
| @radix-ui/react-avatar | ^1.1.11 | Accessible UI primitive: avatar · PREVIEW |
| @radix-ui/react-avatar | ^1.1.4 | Accessible UI primitive: avatar · WEB |
| @radix-ui/react-checkbox | ^1.1.5 | Accessible UI primitive: checkbox · WEB |
| @radix-ui/react-checkbox | ^1.3.3 | Accessible UI primitive: checkbox · PREVIEW |
| @radix-ui/react-collapsible | ^1.1.12 | Accessible UI primitive: collapsible · PREVIEW |
| @radix-ui/react-collapsible | ^1.1.4 | Accessible UI primitive: collapsible · WEB |
| @radix-ui/react-context-menu | ^2.2.16 | Accessible UI primitive: context menu · PREVIEW |
| @radix-ui/react-context-menu | ^2.2.7 | Accessible UI primitive: context menu · WEB |
| @radix-ui/react-dialog | ^1.1.15 | Accessible UI primitive: dialog · PREVIEW |
Versions are manifest declarations/ranges, not a claim about every installed resolution. Catalog references are expanded from pnpm-workspace.yaml. WEB = frontend; API = server; PREVIEW = mockup sandbox; OLD = migration backup. CLIENT / SPEC / VALIDATE / DB / SCRIPTS refer to shared packages. A declared dependency is not evidence of runtime use.

## C2 — Every declared package
Dependency reference · active workspace and preserved original


| PACKAGE | DECLARED VERSION | ROLE / DECLARING SCOPE |
|---|---|---|
| @radix-ui/react-dialog | ^1.1.7 | Accessible UI primitive: dialog · WEB |
| @radix-ui/react-dropdown-menu | ^2.1.16 | Accessible UI primitive: dropdown menu · PREVIEW |
| @radix-ui/react-dropdown-menu | ^2.1.7 | Accessible UI primitive: dropdown menu · WEB |
| @radix-ui/react-hover-card | ^1.1.15 | Accessible UI primitive: hover card · PREVIEW |
| @radix-ui/react-hover-card | ^1.1.7 | Accessible UI primitive: hover card · WEB |
| @radix-ui/react-label | ^2.1.3 | Accessible UI primitive: label · WEB |
| @radix-ui/react-label | ^2.1.8 | Accessible UI primitive: label · PREVIEW |
| @radix-ui/react-menubar | ^1.1.16 | Accessible UI primitive: menubar · PREVIEW |
| @radix-ui/react-menubar | ^1.1.7 | Accessible UI primitive: menubar · WEB |
| @radix-ui/react-navigation-menu | ^1.2.14 | Accessible UI primitive: navigation menu · PREVIEW |
| @radix-ui/react-navigation-menu | ^1.2.6 | Accessible UI primitive: navigation menu · WEB |
| @radix-ui/react-popover | ^1.1.15 | Accessible UI primitive: popover · PREVIEW |
| @radix-ui/react-popover | ^1.1.7 | Accessible UI primitive: popover · WEB |
| @radix-ui/react-progress | ^1.1.3 | Accessible UI primitive: progress · WEB |
| @radix-ui/react-progress | ^1.1.8 | Accessible UI primitive: progress · PREVIEW |
| @radix-ui/react-radio-group | ^1.2.4 | Accessible UI primitive: radio group · WEB |
| @radix-ui/react-radio-group | ^1.3.8 | Accessible UI primitive: radio group · PREVIEW |
Versions are manifest declarations/ranges, not a claim about every installed resolution. Catalog references are expanded from pnpm-workspace.yaml. WEB = frontend; API = server; PREVIEW = mockup sandbox; OLD = migration backup. CLIENT / SPEC / VALIDATE / DB / SCRIPTS refer to shared packages. A declared dependency is not evidence of runtime use.

## C3 — Every declared package
Dependency reference · active workspace and preserved original


| PACKAGE | DECLARED VERSION | ROLE / DECLARING SCOPE |
|---|---|---|
| @radix-ui/react-scroll-area | ^1.2.10 | Accessible UI primitive: scroll area · PREVIEW |
| @radix-ui/react-scroll-area | ^1.2.4 | Accessible UI primitive: scroll area · WEB |
| @radix-ui/react-select | ^2.1.7 | Accessible UI primitive: select · WEB |
| @radix-ui/react-select | ^2.2.6 | Accessible UI primitive: select · PREVIEW |
| @radix-ui/react-separator | ^1.1.3 | Accessible UI primitive: separator · WEB |
| @radix-ui/react-separator | ^1.1.8 | Accessible UI primitive: separator · PREVIEW |
| @radix-ui/react-slider | ^1.2.4 | Accessible UI primitive: slider · WEB |
| @radix-ui/react-slider | ^1.3.6 | Accessible UI primitive: slider · PREVIEW |
| @radix-ui/react-slot | ^1.2.0 | Accessible UI primitive: slot · WEB |
| @radix-ui/react-slot | ^1.2.4 | Accessible UI primitive: slot · PREVIEW |
| @radix-ui/react-switch | ^1.1.4 | Accessible UI primitive: switch · WEB |
| @radix-ui/react-switch | ^1.2.6 | Accessible UI primitive: switch · PREVIEW |
| @radix-ui/react-tabs | ^1.1.13 | Accessible UI primitive: tabs · PREVIEW |
| @radix-ui/react-tabs | ^1.1.4 | Accessible UI primitive: tabs · WEB |
| @radix-ui/react-toast | ^1.2.15 | Accessible UI primitive: toast · PREVIEW |
| @radix-ui/react-toast | ^1.2.7 | Accessible UI primitive: toast · WEB |
| @radix-ui/react-toggle | ^1.1.10 | Accessible UI primitive: toggle · PREVIEW |
Versions are manifest declarations/ranges, not a claim about every installed resolution. Catalog references are expanded from pnpm-workspace.yaml. WEB = frontend; API = server; PREVIEW = mockup sandbox; OLD = migration backup. CLIENT / SPEC / VALIDATE / DB / SCRIPTS refer to shared packages. A declared dependency is not evidence of runtime use.

## C4 — Every declared package
Dependency reference · active workspace and preserved original


| PACKAGE | DECLARED VERSION | ROLE / DECLARING SCOPE |
|---|---|---|
| @radix-ui/react-toggle | ^1.1.3 | Accessible UI primitive: toggle · WEB |
| @radix-ui/react-toggle-group | ^1.1.11 | Accessible UI primitive: toggle group · PREVIEW |
| @radix-ui/react-toggle-group | ^1.1.3 | Accessible UI primitive: toggle group · WEB |
| @radix-ui/react-tooltip | ^1.2.0 | Accessible UI primitive: tooltip · WEB |
| @radix-ui/react-tooltip | ^1.2.8 | Accessible UI primitive: tooltip · PREVIEW |
| @react-three/drei | ^10.7.7 | React Three helper components · OLD, WEB |
| @react-three/fiber | ^9.6.1 | React renderer for Three.js · OLD, WEB |
| @react-three/postprocessing | ^3.0.4 | React postprocessing wrappers · OLD, WEB |
| @replit/vite-plugin-cartographer | ^0.5.21 [catalog] | Replit development/preview tooling · PREVIEW, WEB |
| @replit/vite-plugin-dev-banner | ^0.1.1 [catalog] | Replit development/preview tooling · WEB |
| @replit/vite-plugin-runtime-error-modal | ^0.0.6 [catalog] | Replit development/preview tooling · PREVIEW, WEB |
| @tailwindcss/postcss | ^4 | Original Next/Tailwind integration · OLD |
| @tailwindcss/typography | ^0.5.15 | Prose styling extension · WEB |
| @tailwindcss/vite | ^4.1.14 [catalog] | Tailwind build integration · PREVIEW, WEB |
| @tanstack/react-query | ^5.90.21 [catalog] | Async query client/provider · WEB, CLIENT |
| @types/animejs | ^3.1.13 | Original Anime.js type support · OLD |
| @types/cookie-parser | ^1.4.10 | Type declarations for cookie-parser · API |
Versions are manifest declarations/ranges, not a claim about every installed resolution. Catalog references are expanded from pnpm-workspace.yaml. WEB = frontend; API = server; PREVIEW = mockup sandbox; OLD = migration backup. CLIENT / SPEC / VALIDATE / DB / SCRIPTS refer to shared packages. A declared dependency is not evidence of runtime use.

## C5 — Every declared package
Dependency reference · active workspace and preserved original


| PACKAGE | DECLARED VERSION | ROLE / DECLARING SCOPE |
|---|---|---|
| @types/cors | ^2.8.19 | Type declarations for cors · API |
| @types/express | ^5.0.6 | Type declarations for express · API |
| @types/node | ^20 | Node platform type declarations · OLD |
| @types/node | ^25.3.3 [catalog] | Node platform type declarations · API, PREVIEW, WEB, DB, SCRIPTS |
| @types/pg | ^8.20.0 | Type declarations for pg · DB |
| @types/react | ^19 | React type declarations · OLD |
| @types/react | ^19.2.0 [catalog] | React type declarations · PREVIEW, WEB |
| @types/react-dom | ^19 | React DOM type declarations · OLD |
| @types/react-dom | ^19.2.0 [catalog] | React DOM type declarations · PREVIEW, WEB |
| @types/three | ^0.184.1 | Original Three declarations · OLD |
| @vitejs/plugin-react | ^5.0.4 [catalog] | Supporting package; see declaring manifest · PREVIEW, WEB |
| @webgpu/types | ^0.1.70 | Original browser GPU declarations · OLD |
| @workspace/api-client-react | workspace:* | Internal workspace package link · WEB |
| @workspace/api-zod | workspace:* | Internal workspace package link · API |
| @workspace/db | workspace:* | Internal workspace package link · API |
| animejs | ^3.2.2 | Animation library; v4 active/v3 backup · OLD |
| animejs | ^4.4.1 | Animation library; v4 active/v3 backup · WEB |
Versions are manifest declarations/ranges, not a claim about every installed resolution. Catalog references are expanded from pnpm-workspace.yaml. WEB = frontend; API = server; PREVIEW = mockup sandbox; OLD = migration backup. CLIENT / SPEC / VALIDATE / DB / SCRIPTS refer to shared packages. A declared dependency is not evidence of runtime use.

## C6 — Every declared package
Dependency reference · active workspace and preserved original


| PACKAGE | DECLARED VERSION | ROLE / DECLARING SCOPE |
|---|---|---|
| chokidar | ^4.0.3 | Preview file watching · PREVIEW |
| class-variance-authority | ^0.7.1 [catalog] | Variant-based class composition · PREVIEW, WEB |
| clsx | ^2.1.1 | Conditional class strings · OLD |
| clsx | ^2.1.1 [catalog] | Conditional class strings · PREVIEW, WEB |
| cmdk | ^1.1.1 | Command-menu UI primitive · PREVIEW, WEB |
| cookie-parser | ^1.4.7 | Cookie parsing scaffold · API |
| cors | ^2.8.6 | Cross-origin middleware · API |
| date-fns | ^3.6.0 | Date utilities · PREVIEW, WEB |
| drizzle-kit | ^0.31.10 | Schema tooling · DB |
| drizzle-orm | ^0.45.2 [catalog] | Database query/model layer · API, DB |
| drizzle-zod | ^0.8.3 | DB-to-validation helpers · DB |
| embla-carousel-react | ^8.6.0 | Carousel behavior · PREVIEW, WEB |
| esbuild | 0.27.3 | API bundler / build tool · API |
| esbuild-plugin-pino | ^2.3.3 | Pino bundling integration · API |
| eslint | ^9 | Original lint tooling · OLD |
| eslint-config-next | 16.2.9 | Original Next lint rules · OLD |
| express | ^5.2.1 | HTTP service framework · API |
Versions are manifest declarations/ranges, not a claim about every installed resolution. Catalog references are expanded from pnpm-workspace.yaml. WEB = frontend; API = server; PREVIEW = mockup sandbox; OLD = migration backup. CLIENT / SPEC / VALIDATE / DB / SCRIPTS refer to shared packages. A declared dependency is not evidence of runtime use.

## C7 — Every declared package
Dependency reference · active workspace and preserved original


| PACKAGE | DECLARED VERSION | ROLE / DECLARING SCOPE |
|---|---|---|
| fast-glob | ^3.3.3 | Preview component discovery · PREVIEW |
| framer-motion | ^12.40.0 | Declarative UI animation · OLD |
| framer-motion | ^12.23.24 [catalog] | Declarative UI animation · PREVIEW, WEB |
| gsap | ^3.15.0 | Imperative animation and scroll tooling · OLD, WEB |
| input-otp | ^1.4.2 | OTP input primitive · PREVIEW, WEB |
| lenis | ^1.3.23 | Smooth scroll engine · OLD, WEB |
| lucide-react | ^1.17.0 | Interface icons · OLD |
| lucide-react | ^0.545.0 [catalog] | Interface icons · PREVIEW, WEB |
| next | 16.2.9 | Preserved original framework, not active app · OLD |
| next-themes | ^0.4.6 | Theme helper; not Next runtime proof · PREVIEW, WEB |
| orval | ^8.9.1 | OpenAPI code generation · SPEC |
| pg | ^8.20.0 | PostgreSQL driver · DB |
| pino | ^9.14.0 | Structured logger · API |
| pino-http | ^10.5.0 | HTTP logging middleware · API |
| pino-pretty | ^13.1.3 | Development log formatting · API |
| prettier | ^3.8.3 | Code formatting · ROOT |
| raw-loader | ^4.0.2 | Original shader/raw import loader · OLD |
Versions are manifest declarations/ranges, not a claim about every installed resolution. Catalog references are expanded from pnpm-workspace.yaml. WEB = frontend; API = server; PREVIEW = mockup sandbox; OLD = migration backup. CLIENT / SPEC / VALIDATE / DB / SCRIPTS refer to shared packages. A declared dependency is not evidence of runtime use.

## C8 — Every declared package
Dependency reference · active workspace and preserved original


| PACKAGE | DECLARED VERSION | ROLE / DECLARING SCOPE |
|---|---|---|
| react | 19.2.4 | UI component and state runtime · OLD |
| react | 19.1.0 [catalog] | UI component and state runtime · PREVIEW, WEB |
| react-day-picker | ^9.11.1 | Calendar selection UI · WEB |
| react-day-picker | ^9.14.0 | Calendar selection UI · PREVIEW |
| react-dom | 19.2.4 | React browser rendering · OLD |
| react-dom | 19.1.0 [catalog] | React browser rendering · PREVIEW, WEB |
| react-hook-form | ^7.55.0 | Form management library · WEB |
| react-hook-form | ^7.75.0 | Form management library · PREVIEW |
| react-icons | ^5.4.0 | Additional icon library · WEB |
| react-resizable-panels | ^2.1.7 | Resizable layout panels · WEB |
| react-resizable-panels | ^2.1.9 | Resizable layout panels · PREVIEW |
| recharts | ^2.15.2 | Chart UI library · WEB |
| recharts | ^2.15.4 | Chart UI library · PREVIEW |
| sonner | ^2.0.7 | Toast notifications · PREVIEW, WEB |
| tailwind-merge | ^3.6.0 | Tailwind class conflict resolution · OLD |
| tailwind-merge | ^3.3.1 [catalog] | Tailwind class conflict resolution · PREVIEW, WEB |
| tailwindcss | ^4 | Utility-first styling · OLD |
Versions are manifest declarations/ranges, not a claim about every installed resolution. Catalog references are expanded from pnpm-workspace.yaml. WEB = frontend; API = server; PREVIEW = mockup sandbox; OLD = migration backup. CLIENT / SPEC / VALIDATE / DB / SCRIPTS refer to shared packages. A declared dependency is not evidence of runtime use.

## C9 — Every declared package
Dependency reference · active workspace and preserved original


| PACKAGE | DECLARED VERSION | ROLE / DECLARING SCOPE |
|---|---|---|
| tailwindcss | ^4.1.14 [catalog] | Utility-first styling · PREVIEW, WEB |
| tailwindcss-animate | ^1.0.7 | Supporting package; see declaring manifest · PREVIEW |
| thread-stream | 3.1.0 | Logging worker transport · API |
| three | ^0.184.0 | 3D rendering objects and materials · OLD, WEB |
| three-stdlib | ^2.36.1 | Three helper implementations · OLD, WEB |
| tsx | ^4.21.0 [catalog] | TypeScript script runner · SCRIPTS |
| tw-animate-css | ^1.4.0 | Animation utility styles · PREVIEW, WEB |
| typescript | ^5 | Static type checking · OLD |
| typescript | ~5.9.3 | Static type checking · ROOT |
| vaul | ^1.1.2 | Drawer primitive · PREVIEW, WEB |
| vite | ^7.3.2 [catalog] | Frontend dev server and bundler · PREVIEW, WEB |
| wouter | ^3.3.5 | Client-side routing · WEB |
| zod | ^3.25.76 [catalog] | Validation and schema types · PREVIEW, WEB, VALIDATE, DB |
| zustand | ^5.0.14 | Lightweight local state store · OLD, WEB |
Versions are manifest declarations/ranges, not a claim about every installed resolution. Catalog references are expanded from pnpm-workspace.yaml. WEB = frontend; API = server; PREVIEW = mockup sandbox; OLD = migration backup. CLIENT / SPEC / VALIDATE / DB / SCRIPTS refer to shared packages. A declared dependency is not evidence of runtime use.

## D1 — Sources, reproducibility, and credits
Use the document with confidence


### Source of truth
This document is grounded in the local checkout of `UCHIHA-MADARA-ANUJ/Resonate-Portfolio` at baseline `14fe27732222a28335c2cb7d45ea5fdf3bf95f8e`. The repository has shallow history here; no detailed individual contribution timeline is inferred. The source catalog covers 370 tracked baseline files. Lockfiles were used for dependency evidence, not reproduced as pages of package-manager internals.

### Evidence bundle
`walkthrough/evidence/frontend-build.txt` and `typecheck.txt` preserve the command output described in Chapter 28. `source-manifest.json` records every indexed path, file size, and SHA-256 digest so the source snapshot can be compared later. The manifest excludes walkthrough deliverables and installed/build artifacts. No secret environment file or Git credential data is included.

### Rebuild the PDF
The readable manuscript is `walkthrough/walkthrough.md`. `walkthrough/build_pdf.py` parses its chapter markers, adds the full source/dependency catalog from tracked files, and draws the diagrams and page layouts. It uses local DejaVu fonts and ReportLab; it does not fetch web content or images. Install the documented Python dependency in an isolated environment and run the script from the repository checkout. Rebuilding after source edits will appropriately update the catalog.

```sh
python3 -m venv .venv-docs
.venv-docs/bin/pip install -r walkthrough/requirements.txt
.venv-docs/bin/python walkthrough/build_pdf.py
```

### Attribution and limits
The active founder profiles identify Anuj Phulera with development/AI/backend and Aarav Choudhary with vision/marketing/ideas. Older planning notes differ; confirm personal credits before public use. The two attached founder images are stylized anime assets. This PDF does not reuse them, and no ownership or license claim is made for those images. The root manifest declares MIT but a standalone license file is not present in the indexed baseline.

This is a technical walkthrough, not medical advice, a security certification, a verified social-impact report, or a legal-compliance assessment. Recommendations and first-person scripts are clearly editorial. Diagrams are explanatory vector illustrations—not screenshots or representations of a deployed service.

**Final note:** the strongest version of the project story combines ambition with precision. Show what you built, explain how it works, acknowledge what is simulated, and make the next step testable.

