---
description: Validates Schema Markup and Indexes the site on Google Search Console
---

1. **Schema Validation**
   - Read `src/pages/index.astro`. Check `schema` object:
     - Verify `@id` and `url` match the production domain (e.g. `https://landscaperspakenham.com.au`).
     - Verify `FAQPage` questions match visible text content on the page.
   - Read `src/layouts/Layout.astro`. Verify `schema` prop is passed to the `<SEO />` component.
   - Read `src/components/SEO.astro`.
     - Verify `<script type="application/ld+json" set:html={schema} />` exists.
     - Check `siteName` variable matches the actual Business Name.

2. **Commit & Deploy Fixes**
   - If any issues were found in Step 1, apply fixes.
   - Commit and Push: `git add . && git commit -m "Fix Schema and SEO" && git push`
   - **WAIT** for Coolify deployment to complete (Green status).

3. **GSC Indexing**
   // turbo
   - Run verification check: `python execution/gsc_manager.py --action verify`
   // turbo
   - Submit sitemap: `python execution/gsc_manager.py --action sitemap`
