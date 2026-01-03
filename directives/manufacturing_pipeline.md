# DIR: Manufacturing-Pipeline (v1.6 - Astro Edition)

## 1. PURPOSE
Autonomous "Factory" for high-end trade sites using Astro (Static HTML) for maximum performance and minimum resource usage.
- Brain: Gemini 1.5 Pro (Research & UI)
- Eyes: Nano Banana Pro (NBP) (Hero Imagery)
- Hands: Python/Git/Coolify (Deployment)
- Standard: [Master Design Prompt](file:///c:/Users/srkel/Downloads/Website-builder-antigravity-at-scale/directives/master_design_prompt.md)

## 2. INPUTS
- `TRADE`: Business type (e.g., "High-End Roofer")
- `LOC`: Target City, State
- `BRAND`: (Auto-gen if null)
- `DETAILS`: Specific business details provided in Section 1 of the Master Prompt.

## 3. LAYER 3 TOOLS (Execution Manifest)
- `execution/research_market.py` -> API search (Tavily/Exa) for keywords and local context.
- `execution/generate_hero_nbp.py` -> Call NBP API; save to `public/images/hero.jpg`.
- `execution/unified_deploy.py` -> Astro build -> Git push -> Coolify.

## 4. WORKFLOW (Layer 2 Orchestration)

### Phase 1: Market Intelligence & Creative Direction
1. **Search Grounding**: Use the `search` tool to analyze the specific subject matter and location (vegetation, architecture, terrain).
2. **Keyword Discovery**: Identify 10+ geo-targeted and semantic keywords.
3. **Data Store**: Save brief to `.tmp/market_data.json`.

### Phase 2: Visual Asset Generation
1. **Prompt Engineering**: Write photorealistic prompts for unique images for every section.
2. **Guidelines**: No people, no license plates, daytime lighting, professional composition.
3. **Storage**: Save unique assets to `public/images/`.

### Phase 3: High-End UI Manufacturing (Astro)
1. **Structure**: Use `src/layouts/Layout.astro` and `src/pages/index.astro`.
2. **Design Standards**: 
   - Strategic Typography (blended weights).
   - Functional Whitespace.
   - Depth & Texture (shadows, blurs, grain).
3. **SEO Mandate**: 
   - Mandatory `<SEO />` component.
   - Semantic HTML5 structure.
   - Hyper-local content specificity.

### Phase 4: Deterministic Deployment
1. **Build**: Run `npm run build` to verify the static output.
2. **Infrastructure**: Deploy using the factory's automated scripts to Coolify.

## 5. COOLIFY DEPLOYMENT PROTOCOL
(Unchanged - using Nixpacks for Astro)

## 6. SELF-ANNEALING LOOPS
- **Performance Fail**: If Lighthouse score < 95, optimize images -> Regenerate.
- **Copy Fail**: If tone is generic, apply "Editorial Voice" -> Regenerate.

## 7. DELIVERABLES
- **LIVE_URL**: [Coolify Endpoint]
- **GIT_REPO**: [GitHub URL]
- **STATUS**: Success
