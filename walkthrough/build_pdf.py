#!/usr/bin/env python3
"""Build the repository-grounded RESONATE walkthrough. Requires reportlab.
Run from any directory: python3 walkthrough/build_pdf.py
No network, browser, or application server is required.
"""
from pathlib import Path
import re, math, random, json, subprocess, hashlib, textwrap, html
from collections import defaultdict
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph, Table, TableStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.enums import TA_LEFT

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'walkthrough'
W, H = 595.276, 841.89
M, CW = 53, W-106
BG, INK, MUTED = '#F7F8FA', '#142333', '#566578'
CYAN, PINK, NAVY = '#00F0FF', '#FF0055', '#07121F'
FONTROOT = Path('/usr/share/fonts/truetype/dejavu')
for name, file in [('Body','DejaVuSans.ttf'),('Bold','DejaVuSans-Bold.ttf'),('Mono','DejaVuSansMono.ttf')]:
    pdfmetrics.registerFont(TTFont(name, str(FONTROOT/file)))
pdfmetrics.registerFontFamily('Body', normal='Body', bold='Bold', italic='Body', boldItalic='Bold')
pdfmetrics.registerFontFamily('Mono', normal='Mono', bold='Mono', italic='Mono', boldItalic='Mono')


def mark(s):
    s=html.escape(s)
    s=re.sub(r'`([^`]+)`',r'<font name="Mono" size="8.5" color="#087680">\1</font>',s)
    s=re.sub(r'\*\*([^*]+)\*\*',r'<b>\1</b>',s)
    return s


def para(s, size=9.7, leading=14.6, color=INK, font='Body', **kw):
    return Paragraph(s, ParagraphStyle('p', fontName=font, fontSize=size, leading=leading,
        textColor=colors.HexColor(color), spaceAfter=0, splitLongWords=True, **kw))


def text(c,s,x,y,size=9,color=INK,font='Body'):
    c.setFillColor(colors.HexColor(color)); c.setFont(font,size); c.drawString(x,y,s)


def draw_p(c,s,x,y,width,size=9.7,leading=14.6,color=INK,font='Body'):
    p=para(s,size,leading,color,font); _,h=p.wrap(width,1000); p.drawOn(c,x,y-h); return h


def diagram(c, kind, x, y, width):
    heights={'architecture':152,'journey':100,'palette':94,'gpu':112,'waitlist':112}
    ht=heights[kind]
    c.saveState(); c.setFillColor(colors.HexColor(NAVY)); c.roundRect(x,y-ht,width,ht,7,fill=1,stroke=0)
    def box(xx,yy,ww,hh,label,sub='',accent=CYAN):
        c.setStrokeColor(colors.HexColor('#284354')); c.setFillColor(colors.HexColor('#101F30'))
        c.roundRect(xx, yy-hh, ww, hh, 4, fill=1,stroke=1)
        c.setFillColor(colors.HexColor(accent)); c.rect(xx,yy-hh,2,hh,fill=1,stroke=0)
        draw_p(c,html.escape(label),xx+10,yy-9,ww-18,8,11,'#E6F1F5','Bold')
        if sub: draw_p(c,html.escape(sub),xx+10,yy-25,ww-18,6.8,9,'#AEC0CC')
    def arrow(x1,y1,x2,y2):
        c.setStrokeColor(colors.HexColor(CYAN)); c.setLineWidth(.7); c.line(x1,y1,x2,y2)
        a=math.atan2(y2-y1,x2-x1)
        for d in [-.48,.48]: c.line(x2,y2,x2-4*math.cos(a+d),y2-4*math.sin(a+d))
    if kind=='architecture':
        box(x+15,y-14,width-30,40,'PRESENTATION / React + Vite','26 routes · motion · GLSL canvases · audio-driven UI')
        box(x+15,y-70,(width-45)/2,60,'DOMAIN + CORE','User · Circle · EmotionalState\nEvents · vector clocks',CYAN)
        box(x+30+(width-45)/2,y-70,(width-45)/2,60,'INFRASTRUCTURE','Audio connected; crypto, mesh,\ncompute and metrics foundations',PINK)
        arrow(x+width*.25,y-55,x+width*.25,y-67); arrow(x+width*.75,y-55,x+width*.75,y-67)
        text(c,'SEPARATE WORKSPACE: Express health API + generated contracts + empty DB schema',x+16,y-144,6.3,'#AAC0CD','Mono')
    elif kind=='journey':
        labels=[('INITIALIZE','User gesture'),('REVEAL','~30 sec cinema'),('EXPLORE','26 routes'),('INTERACT','Demos + terminal')]
        bw=(width-54)/4
        for i,(a,b) in enumerate(labels):
            xx=x+15+i*(bw+8); box(xx,y-23,bw,53,a,b)
            if i<3: arrow(xx+bw+1,y-50,xx+bw+7,y-50)
        text(c,'EXPERIENCE FLOW / not a verified clinical care pathway',x+16,y-91,6.3,'#AAC0CD','Mono')
    elif kind=='palette':
        vals=[('#000000','VOID BLACK'),('#0B001A','DEEP FREQUENCY'),('#00F0FF','RESONANCE'),('#FF0055','SHOCK'),('#E2E8F0','PRIMARY TEXT')]
        bw=(width-30)/5
        for i,(col,lab) in enumerate(vals):
            xx=x+15+i*bw; c.setFillColor(colors.HexColor(col)); c.rect(xx,y-48,bw-6,31,fill=1,stroke=0)
            text(c,col,xx,y-63,7,'#E6F1F5','Mono'); text(c,lab,xx,y-77,5.8,'#AEC0CC','Mono')
    elif kind=='gpu':
        labs=[('CPU BUFFERS','positions + randoms'),('VERTEX SHADER','noise + time + mouse'),('FRAGMENT SHADER','soft circular points')]
        bw=(width-46)/3
        for i,(a,b) in enumerate(labs):
            xx=x+15+i*(bw+8); box(xx,y-20,bw,56,a,b)
            if i<2: arrow(xx+bw+1,y-48,xx+bw+7,y-48)
        text(c,'60,000 PARTICLES / each frame updates uniforms, not 60,000 React nodes',x+16,y-97,6.3,'#AAC0CD','Mono')
    else:
        labels=[('NAME','minimum 2 chars'),('EMAIL','format check'),('ROLE','1–5 selection'),('LOCAL SAVE','browser only')]
        bw=(width-54)/4
        for i,(a,b) in enumerate(labels):
            xx=x+15+i*(bw+8); box(xx,y-20,bw,55,a,b, PINK if i==3 else CYAN)
            if i<3: arrow(xx+bw+1,y-48,xx+bw+7,y-48)
        text(c,'NO SERVER SUBMISSION / no verified invitation or encrypted enrollment',x+16,y-98,6.2,'#AAC0CD','Mono')
    c.restoreState(); return ht


def parse_blocks(body):
    blocks=[]; lines=body.strip().splitlines(); p=[]; code=[]; incode=False
    def flush():
        if p: blocks.append(('p',' '.join(p))); p.clear()
    for line in lines:
        if line.startswith('```'):
            flush()
            if incode: blocks.append(('code','\n'.join(code)));code=[]
            incode=not incode; continue
        if incode: code.append(line); continue
        if not line.strip(): flush(); continue
        if line.startswith('### '): flush();blocks.append(('h',line[4:]));continue
        if line.startswith('[[diagram:'): flush();blocks.append(('d',line[10:-2]));continue
        if line.startswith('- '): flush();blocks.append(('li',line[2:]));continue
        if line.startswith('**Evidence'): flush();blocks.append(('e',line));continue
        p.append(line)
    flush();return blocks


raw=(OUT/'walkthrough.md').read_text()
parts=re.split(r'<!-- PAGE (\d+) \| (.*?) \| (.*?) -->',raw)
pages=[]
for i in range(1,len(parts),4):
    pages.append({'id':parts[i], 'title':parts[i+1], 'sub':parts[i+2], 'body':parts[i+3].strip()})

# Appendices are generated from tracked repository files, not installed dependencies.
files=subprocess.check_output(['git','ls-files'],cwd=ROOT,text=True).splitlines()
files=[f for f in files if not f.startswith('walkthrough/')]
manifest=[]
for f in files:
    p=ROOT/f; data=p.read_bytes(); manifest.append({'path':f,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
(OUT/'evidence'/'source-manifest.json').write_text(json.dumps({'baseline':'14fe277','date':'2026-10-18','files':manifest},indent=2)+'\n')

def add(id,title,sub,body): pages.append({'id':id,'title':title,'sub':sub,'body':body})

add('A1','Read the code in this order','A guided source-study map', '''
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
''')

add('A2','More scenes, under the microscope','What the names really mean', '''
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
''')

add('A3','A test plan you can explain','From source inspection to dependable behavior', '''
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
''')

# Full file catalog: grouped to shorten repeated long prefixes, all 370 tracked paths retained.
groups=[('ROOT / workspace and deployment',[f for f in files if '/' not in f]),
        ('FRONTEND / artifacts/resonate',[f for f in files if f.startswith('artifacts/resonate/') and '/src/components/ui/' not in f]),
        ('UI LIBRARY / artifacts/resonate/src/components/ui',[f for f in files if f.startswith('artifacts/resonate/src/components/ui/')]),
        ('SERVICES + LIBRARIES / repository-relative',[f for f in files if f.startswith(('artifacts/api-server/','lib/','scripts/'))]),
        ('PREVIEW SANDBOX / artifacts/mockup-sandbox',[f for f in files if f.startswith('artifacts/mockup-sandbox/')]),
        ('MIGRATION BACKUP / .migration-backup',[f for f in files if f.startswith('.migration-backup/')]),
        ('ATTACHMENTS / attached_assets',[f for f in files if f.startswith('attached_assets/')])]
covered=[]; inv_index=0
for label, group in groups:
    if not group: continue
    covered+=group
    prefix= {'FRONTEND':'artifacts/resonate/','UI LIBRARY':'artifacts/resonate/src/components/ui/', 'PREVIEW SANDBOX':'artifacts/mockup-sandbox/','MIGRATION BACKUP':'.migration-backup/','ATTACHMENTS':'attached_assets/'}.get(label.split(' /')[0],'')
    # Grouped filenames, with line count useful for knowing scale; binary assets say bytes.
    rows=[]
    for f in group:
        p=ROOT/f; b=p.read_bytes()
        try: st=b.decode('utf-8'); count=f'{len(st.splitlines()):,} lines'
        except UnicodeDecodeError: count=f'{len(b):,} bytes'
        short=f[len(prefix):] if prefix else f
        rows.append((short,count))
    for start in range(0,len(rows),26):
        inv_index+=1
        add(f'B{inv_index}', 'Complete repository file catalog',label+(' · continued' if start else ''),'')
        pages[-1]['table']=[['PATH (relative to the scope above)','SIZE / SCALE']]+rows[start:start+26]
        pages[-1]['note']='Every tracked baseline file is indexed once in this catalog. Third-party node_modules, generated build output, .git internals, and the new walkthrough files are excluded. Line counts are file scale, not a measure of original authorship. Migration and UI scaffolds are listed without implying active runtime use.'
assert sorted(covered)==sorted(files), 'Catalog omitted or duplicated a source file'

# Dependency declarations deduplicated by name+declaration, recording all package scopes.
manifest_paths=[p for p in files if p.endswith('package.json')]
entries=defaultdict(list)
for p in manifest_paths:
    pkg=json.loads((ROOT/p).read_text()); scope=p.replace('/package.json','').replace('package.json','root')
    for typ in ['dependencies','devDependencies']:
        for dep,ver in pkg.get(typ,{}).items(): entries[(dep,ver)].append(scope)
# Resolve catalog versions from known simple YAML catalog lines without adding a YAML build dependency.
workspace=(ROOT/'pnpm-workspace.yaml').read_text(); catpart=workspace.split('catalog:',1)[1].split('autoInstallPeers:',1)[0]
catalog={}
for line in catpart.splitlines():
    match=re.match(r"\s{2}['\"]?([^'\" :]+)['\"]?:\s*(.+?)\s*$",line)
    if match: catalog[match[1]]=match[2].split(' #')[0]
roles={
 'react':'UI component and state runtime','react-dom':'React browser rendering', 'typescript':'Static type checking','vite':'Frontend dev server and bundler','wouter':'Client-side routing','tailwindcss':'Utility-first styling','@tailwindcss/vite':'Tailwind build integration','@tailwindcss/postcss':'Original Next/Tailwind integration','@tailwindcss/typography':'Prose styling extension','tw-animate-css':'Animation utility styles',
 'three':'3D rendering objects and materials','@react-three/fiber':'React renderer for Three.js','@react-three/drei':'React Three helper components','@react-three/postprocessing':'React postprocessing wrappers','three-stdlib':'Three helper implementations',
 'gsap':'Imperative animation and scroll tooling','@gsap/react':'React/GSAP integration helper','framer-motion':'Declarative UI animation','animejs':'Animation library; v4 active/v3 backup','@types/animejs':'Original Anime.js type support','lenis':'Smooth scroll engine','lucide-react':'Interface icons','react-icons':'Additional icon library',
 'zustand':'Lightweight local state store','@tanstack/react-query':'Async query client/provider','express':'HTTP service framework','cors':'Cross-origin middleware','cookie-parser':'Cookie parsing scaffold','pino':'Structured logger','pino-http':'HTTP logging middleware','pino-pretty':'Development log formatting','thread-stream':'Logging worker transport',
 'zod':'Validation and schema types','orval':'OpenAPI code generation','drizzle-orm':'Database query/model layer','drizzle-zod':'DB-to-validation helpers','drizzle-kit':'Schema tooling','pg':'PostgreSQL driver','prettier':'Code formatting','tsx':'TypeScript script runner','esbuild':'API bundler / build tool','esbuild-plugin-pino':'Pino bundling integration',
 'clsx':'Conditional class strings','tailwind-merge':'Tailwind class conflict resolution','class-variance-authority':'Variant-based class composition','cmdk':'Command-menu UI primitive','react-hook-form':'Form management library','@hookform/resolvers':'Form/schema adapters','date-fns':'Date utilities','react-day-picker':'Calendar selection UI','embla-carousel-react':'Carousel behavior','input-otp':'OTP input primitive','react-resizable-panels':'Resizable layout panels','recharts':'Chart UI library','sonner':'Toast notifications','vaul':'Drawer primitive','next-themes':'Theme helper; not Next runtime proof',
 'next':'Preserved original framework, not active app','eslint':'Original lint tooling','eslint-config-next':'Original Next lint rules','raw-loader':'Original shader/raw import loader','@webgpu/types':'Original browser GPU declarations','@types/three':'Original Three declarations','fast-glob':'Preview component discovery','chokidar':'Preview file watching','@types/node':'Node platform type declarations','@types/react':'React type declarations','@types/react-dom':'React DOM type declarations'
}
scopemap={'root':'ROOT','artifacts/resonate':'WEB','artifacts/api-server':'API','artifacts/mockup-sandbox':'PREVIEW','.migration-backup':'OLD','lib/api-client-react':'CLIENT','lib/api-spec':'SPEC','lib/api-zod':'VALIDATE','lib/db':'DB','scripts':'SCRIPTS'}
dep_rows=[]
for (dep,ver),scopes in sorted(entries.items()):
    shown=ver if ver!='catalog:' else f"{catalog.get(dep,'catalog')} [catalog]"
    role=roles.get(dep)
    if not role:
        if dep.startswith('@radix-ui/'): role='Accessible UI primitive: '+dep.split('react-')[-1].replace('-',' ')
        elif dep.startswith('@replit/'): role='Replit development/preview tooling'
        elif dep.startswith('@workspace/'): role='Internal workspace package link'
        elif dep.startswith('@types/'): role='Type declarations for '+dep[7:]
        else: role='Supporting package; see declaring manifest'
    dep_rows.append((dep,shown,role+' · '+', '.join(scopemap.get(s,s) for s in scopes)))
for start in range(0,len(dep_rows),17):
    add(f'C{start//17+1}','Every declared package','Dependency reference · active workspace and preserved original','')
    pages[-1]['deptable']=[['PACKAGE','DECLARED VERSION','ROLE / DECLARING SCOPE']]+dep_rows[start:start+17]
    pages[-1]['note']='Versions are manifest declarations/ranges, not a claim about every installed resolution. Catalog references are expanded from pnpm-workspace.yaml. WEB = frontend; API = server; PREVIEW = mockup sandbox; OLD = migration backup. CLIENT / SPEC / VALIDATE / DB / SCRIPTS refer to shared packages. A declared dependency is not evidence of runtime use.'

add('D1','Sources, reproducibility, and credits','Use the document with confidence', f'''
### Source of truth
This document is grounded in the local checkout of `UCHIHA-MADARA-ANUJ/Resonate-Portfolio` at baseline `14fe27732222a28335c2cb7d45ea5fdf3bf95f8e`. The repository has shallow history here; no detailed individual contribution timeline is inferred. The source catalog covers {len(files)} tracked baseline files. Lockfiles were used for dependency evidence, not reproduced as pages of package-manager internals.

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
''')

# Save a text version of generated reference material as a companion.
appendix=['# RESONATE — generated reference appendices','']
for p in pages[33:]:
    appendix.extend([f"## {p['id']} — {p['title']}",p['sub'],'',p['body']])
    for key in ['table','deptable']:
        if key in p:
            rows=p[key];appendix.extend(['| '+' | '.join(rows[0])+' |','|'+'|'.join(['---']*len(rows[0]))+'|'])
            appendix.extend('| '+' | '.join(row)+' |' for row in rows[1:])
    if 'note' in p:appendix.append(p['note'])
    appendix.append('')
(OUT/'reference-appendices.md').write_text('\n'.join(appendix))

TOTAL=1+2+len(pages)
C=canvas.Canvas(str(OUT/'RESONATE_Complete_Project_Walkthrough.pdf'),pagesize=(W,H),pageCompression=1)
C.setTitle('RESONATE — The Complete Project Walkthrough')
C.setAuthor('RESONATE project walkthrough • repository-grounded edition')
C.setSubject('Vision, technology, architecture, implementation, demonstrations, limitations and presentation guide')
C.setKeywords('RESONATE, portfolio, React, Vite, Three.js, project walkthrough')
C.setViewerPreference('DisplayDocTitle','true')


def chrome(c,n,dark=False):
    c.setFillColor(colors.HexColor(NAVY if dark else BG));c.rect(0,0,W,H,fill=1,stroke=0)
    c.setFillColor(colors.HexColor(CYAN));c.rect(0,H-5,W*.73,5,fill=1,stroke=0)
    c.setFillColor(colors.HexColor(PINK));c.rect(W*.73,H-5,W*.27,5,fill=1,stroke=0)
    text(c,'RESONATE',M,H-39,10,'#E3EDF5' if dark else INK,'Bold')
    text(c,'PROJECT FIELD GUIDE / 2026.10',W-260,H-38,7,'#94AABB' if dark else MUTED,'Mono')
    c.setStrokeColor(colors.HexColor('#284052' if dark else '#D7DEE5'));c.setLineWidth(.6);c.line(M,52,W-M,52)
    text(c,'VISION  /  EXPERIENCE  /  ENGINEERING',M,34,6.3,'#8AA4B6' if dark else MUTED,'Mono')
    lab=f'{n:02d} / {TOTAL:02d}';c.setFont('Mono',7);c.setFillColor(colors.HexColor('#D5E6F0' if dark else MUTED));c.drawRightString(W-M,34,lab)


def cover(c):
    chrome(c,1,True)
    random.seed(47)
    # Procedural orbital field, not an application screenshot.
    for j in range(27):
        path=c.beginPath()
        for i in range(210):
            t=i/209*math.pi*2
            r=113+j*2.3 + 9*math.sin(3*t+j*.11)
            xx=W*.62+math.cos(t)*r*1.6; yy=H*.43+math.sin(t)*r*.73
            if i==0:path.moveTo(xx,yy)
            else:path.lineTo(xx,yy)
        c.setStrokeColor(colors.HexColor('#123542' if j%4 else '#17606B'));c.setLineWidth(.32);c.drawPath(path)
    for i in range(720):
        t=random.random()*math.pi*2;r=random.gauss(140,35)
        xx=W*.62+math.cos(t)*r*1.6; yy=H*.43+math.sin(t)*r*.73
        c.setFillColor(colors.HexColor(CYAN if i%7 else PINK));c.circle(xx,yy,random.uniform(.25,1.05),fill=1,stroke=0)
    text(c,'ALGORITHMIC SANCTUARY',M,H-105,9,CYAN,'Mono')
    text(c,'RESONATE',M,H-187,61,'#F2F7FB','Bold')
    draw_p(c,'The complete<br/>project walkthrough',M,H-221,450,27,33,'#FFFFFF','Bold')
    draw_p(c,'Why it exists. What you built.<br/>How every part fits together.',M,H-316,430,13,21,'#AEC4D3')
    c.setFillColor(colors.HexColor(PINK));c.rect(M,184,43,3,fill=1,stroke=0)
    draw_p(c,'A detailed, source-grounded guide to the vision, visual engine, product demos, software architecture, and responsible next steps.',M,169,435,11,17,'#D6E2EA')
    text(c,'26 ROUTES',M,91,8.5,CYAN,'Mono');text(c,'CUSTOM SHADERS',M+126,91,8.5,CYAN,'Mono');text(c,'FULL SOURCE REFERENCE',M+306,91,8.5,CYAN,'Mono')
    c.bookmarkPage('cover');c.addOutlineEntry('RESONATE — Complete Walkthrough','cover',0,False)
    c.showPage()


def toc(c,part):
    n=2+part;chrome(c,n,True)
    text(c,'READING MAP',M,H-91,8,CYAN,'Mono')
    text(c,'Inside this walkthrough',M,H-133,26,'#FFFFFF','Bold')
    if part==0:
        draw_p(c,'Start with the story. Then follow the experience into the code.',M,H-157,CW,10,15,'#ADC2D1')
        items=pages[:18]
    else:
        draw_p(c,'Study the engineering, rehearse the presentation, and use the reference.',M,H-157,CW,10,15,'#ADC2D1')
        items=pages[18:33]
    y=H-204
    for p in items:
        idx=pages.index(p); physical=4+idx
        text(c,p['id'].zfill(2),M,y,8,CYAN,'Mono')
        text(c,p['title'],M+33,y,10,'#E6EEF5')
        c.setFont('Mono',8);c.setFillColor(colors.HexColor('#ADC2D1'));c.drawRightString(W-M,y,str(physical))
        c.linkRect('',p['id'],(M,y-7,W-M,y+13),relative=0,thickness=0)
        c.setStrokeColor(colors.HexColor('#193043'));c.line(M,y-13,W-M,y-13);y-=27
    if part==1:
        y-=13
        for prefix,label in [('A','Code-reading map, scene deep dives, and test plan'),('B','Complete tracked-file catalog'),('C','Every declared dependency'),('D','Sources, reproducibility, and credits')]:
            p=next(p for p in pages if p['id'].startswith(prefix)); physical=4+pages.index(p)
            text(c,prefix,M,y,8,PINK,'Mono');text(c,label,M+33,y,9,'#D6E6EF')
            c.setFont('Mono',8);c.drawRightString(W-M,y,str(physical));c.linkRect('',p['id'],(M,y-7,W-M,y+13),relative=0,thickness=0);y-=26
    draw_p(c,'HOW TO USE IT  /  Chapters 01–08 for the big picture. Chapters 09–29 for implementation and honest technical defense. Chapters 30–33 for next steps and presentation practice. PDF bookmarks and contents entries are clickable.',M,114,CW,8.3,13,'#95ACBE')
    c.showPage()


def page_heading(c,p,n):
    chrome(c,n)
    text(c,f"{p['id']}  /  {p['sub'].upper()}",M,H-83,7.5,'#087680','Mono')
    title=para(html.escape(p['title']),24,29,INK,'Bold')
    _,th=title.wrap(CW,1000);title.drawOn(c,M,H-105-th)
    yy=H-122-th
    c.setFillColor(colors.HexColor(PINK));c.rect(M,yy,31,2,fill=1,stroke=0)
    return yy-19


def content_layout(p,start,scale=1,draw=False):
    y=start; evidence=[]
    for typ,s in parse_blocks(p['body']):
        if typ=='e': evidence.append(s);continue
        if typ=='d':
            ht={'architecture':152,'journey':100,'palette':94,'gpu':112,'waitlist':112}[s]
            if draw: diagram(C,s,M,y,CW)
            y-=ht+15;continue
        if typ=='code':
            lines=s.splitlines();ht=20+len(lines)*12*scale
            if draw:
                C.setFillColor(colors.HexColor('#E9EFF3'));C.roundRect(M,y-ht,CW,ht,4,fill=1,stroke=0)
                for i,l in enumerate(lines):text(C,l,M+12,y-17-i*12*scale,8*scale,'#163747','Mono')
            y-=ht+12*scale;continue
        if typ=='h':
            pp=para(mark(s),10.5*scale,15*scale,INK,'Bold');space=7*scale;after=5*scale;x=M;ww=CW
        elif typ=='li':
            pp=para('• '+mark(s),9.7*scale,14.6*scale,INK);space=0;after=6*scale;x=M+4;ww=CW-5
        else:
            pp=para(mark(s),9.7*scale,14.6*scale,INK);space=0;after=10*scale;x=M;ww=CW
        y-=space;_,hh=pp.wrap(ww,1000)
        if draw:pp.drawOn(C,x,y-hh)
        y-=hh+after
    # Evidence reference strip, fixed to bottom but measured for collision.
    evid=' '.join(evidence)
    if evid:
        ep=para(mark(evid),7,10,MUTED)
        _,eh=ep.wrap(CW-14,1000)
        if draw:
            C.setStrokeColor(colors.HexColor('#CBD8E2'));C.line(M,73+eh+8,W-M,73+eh+8)
            ep.drawOn(C,M,73)
        miny=73+eh+16
    else:miny=73
    return y,miny


def draw_table_page(p,start):
    dep='deptable' in p;rows=p['deptable' if dep else 'table']
    widths=[192,103,CW-295] if dep else [CW-92,92]
    data=[]
    for ri,row in enumerate(rows):
        data.append([para(html.escape(str(v)),6.4 if dep and ri==0 else (7.1 if dep else 7.6),10 if dep else 11.5,
            '#FFFFFF' if ri==0 else INK,'Bold' if ri==0 else ('Mono' if ci==0 else 'Body')) for ci,v in enumerate(row)])
    t=Table(data,colWidths=widths,hAlign='LEFT')
    t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor(NAVY)),('VALIGN',(0,0),(-1,-1),'TOP'),
        ('LEFTPADDING',(0,0),(-1,-1),8),('RIGHTPADDING',(0,0),(-1,-1),8),('TOPPADDING',(0,0),(-1,-1),4),('BOTTOMPADDING',(0,0),(-1,-1),4),
        ('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.HexColor('#FFFFFF'),colors.HexColor('#ECF1F4')]),('LINEBELOW',(0,0),(-1,0),1,colors.HexColor('#00A5B4'))]))
    _,ht=t.wrap(CW,H)
    if start-ht<135: raise RuntimeError(f"Table overflow {p['id']}: {ht}")
    t.drawOn(C,M,start-ht)
    draw_p(C,mark(p['note']),M,108,CW,7.2,11,MUTED)

cover(C);toc(C,0);toc(C,1)
layout_report=[]
for i,p in enumerate(pages):
    C.bookmarkPage(p['id']);C.addOutlineEntry(f"{p['id']}  {p['title']}",p['id'],1,False)
    start=page_heading(C,p,4+i)
    if 'table' in p or 'deptable' in p:draw_table_page(p,start);scale=1
    else:
        scale=1
        while True:
            y,bottom=content_layout(p,start,scale)
            if y>=bottom:break
            scale-=.015
            if scale<.82: raise RuntimeError(f"Text overflow in {p['id']}: {y:.1f} < {bottom:.1f}")
        content_layout(p,start,scale,True)
    layout_report.append({'id':p['id'],'page':i+4,'title':p['title'],'scale':round(scale,3)})
    C.showPage()
C.save()
(OUT/'evidence'/'pdf-layout.json').write_text(json.dumps({'pages':TOTAL,'chapters':33,'source_files':len(files),'declared_package_variants':len(dep_rows),'layout':layout_report},indent=2)+'\n')
print(f'Wrote {TOTAL} pages, {len(files)} source files indexed, {len(dep_rows)} dependency declarations.')
print('Minimum text scale:',min(p['scale'] for p in layout_report))
print(OUT/'RESONATE_Complete_Project_Walkthrough.pdf')
