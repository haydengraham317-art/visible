# GoldTree Property Management — SEO Content

SEO keyword research and blog drafts for [goldtreepropertymanagement.ca](https://goldtreepropertymanagement.ca) —
a full-service residential property management company based in Bedford, Nova Scotia, serving Halifax,
Bedford, Dartmouth, Sackville, Timberlea and the wider HRM.

## Contents

| File | What it is |
|---|---|
| [`keyword-research.md`](keyword-research.md) | Full keyword map — 8 clusters, ~70 keywords with intent and difficulty, People Also Ask mining, publishing priority and seasonal calendar |
| [`blogs/01-nova-scotia-rent-cap-2026.md`](blogs/01-nova-scotia-rent-cap-2026.md) | Rent cap + Form J notice deadlines |
| [`blogs/02-how-to-evict-a-tenant-nova-scotia.md`](blogs/02-how-to-evict-a-tenant-nova-scotia.md) | Eviction process, forms, timelines, costs |
| [`blogs/03-how-much-rent-can-i-charge-halifax.md`](blogs/03-how-much-rent-can-i-charge-halifax.md) | 2026 rents by area + pricing methodology |

## Why these three

All three target **rental owners** rather than tenants. Tenants generate most of the search volume in
Nova Scotia; owners generate the revenue. The overlap worth winning is *landlord compliance anxiety* —
owners who are worried about getting something legally wrong and are close to outsourcing the job.

1. **Rent cap / Form J** — highest owner-intent volume in the province, and there is a live 1 September
   2026 deadline for any 1 January 2027 increase.
2. **Evictions** — highest pain, highest conversion. An owner mid-eviction is the most likely person
   online to hire a property manager.
3. **Halifax rents** — highest raw volume of the three, and maps directly onto GoldTree's free rental
   analysis lead magnet.

## Format notes

Each draft is Markdown with YAML front matter containing the meta title, meta description, slug, primary
and secondary keywords, and the schema types to apply. Each post carries an FAQ section written for
`FAQPage` markup, internal links to its two siblings, and a CTA to the free rental analysis.

## Before publishing

- **Validate the volume estimates.** No keyword-tool API was available in the environment these were
  built in — figures in `keyword-research.md` are modelled, not pulled. See §0 of that file. The
  clustering and priority order stand regardless; the absolute numbers need confirming in Ahrefs or
  Keyword Planner set to Canada / Nova Scotia.
- **Re-verify every legal fact.** Nova Scotia tenancy law is actively changing. Facts were verified
  against sources current as of August 2026. Confirm form names and notice periods against the
  [official residential tenancy forms page](https://novascotia.ca/residential-tenancy-forms) — sources
  disagree on which form covers rent arrears, and the drafts follow the provincial government's own
  published guide.
- **Add a named author byline.** These are YMYL (legal/financial) topics where Google weights E-E-A-T
  heavily. Publish under a real person at GoldTree, not "Admin".
- **Diarise a review date.** Posts 1 and 2 need re-checking every January and immediately on any
  legislative change.
