from pathlib import Path

base = Path(__file__).parent / "areas"
base.mkdir(parents=True, exist_ok=True)

areas = [
  {
    "slug": "vernon-hills-60061",
    "city": "Vernon Hills",
    "zip": "60061",
    "county": "Lake County",
    "primary": True,
    "title": "Vernon Hills Realtor | Homes for Sale in 60061 | Rick Brown Coldwell Banker",
    "meta": "Looking for a Vernon Hills realtor in ZIP 60061? Rick Brown at Coldwell Banker helps buyers and sellers with pricing, offers, and local market strategy. Call 847-400-6018.",
    "h1": "Vernon Hills realtor for buyers and sellers in ZIP 60061",
    "lead": "Rick Brown is a Coldwell Banker realtor focused on Vernon Hills, IL 60061. Get clear guidance on buying, selling, or timing both moves in this Lake County market.",
    "about": "Vernon Hills sits in the heart of southern Lake County with shopping at Hawthorn and Mellody Farm, strong park district amenities, and quick access to I-94. Buyers often compare Gregg's Landing and nearby master-planned streets with townhome and condo options closer to retail corridors. Sellers in 60061 need pricing that reflects school boundaries, updates, and recent nearby closings, not a county-wide average.",
    "buyer": "When you buy in Vernon Hills, Rick helps you target the right inventory lane, schedule tours efficiently, and write offers that fit local competition. Whether you want a single-family home near parks or a lower-maintenance attached property, the plan starts with real comps for 60061.",
    "seller": "Selling in 60061 means positioning against live demand. Rick covers pre-list prep, pricing strategy, listing presentation, showing feedback, and negotiation through closing so DOM does not drift without a reason.",
    "nearby": "Nearby markets include Libertyville 60048, Buffalo Grove 60089, and Wheeling 60090. Many clients sell in one ZIP and buy in another with a coordinated timeline.",
    "faq1_q": "What should buyers know about Vernon Hills 60061?",
    "faq1_a": "Inventory, price bands, and competition vary by neighborhood and property type. Rick translates current listings and recent sales into a practical budget and offer range before you write.",
    "faq2_q": "How do I get a home value estimate in Vernon Hills?",
    "faq2_a": "Call or text 847-400-6018 or use the contact form. Rick reviews your address, condition, and recent 60061 comps, then walks through a recommended listing strategy.",
  },
  {
    "slug": "libertyville-60048",
    "city": "Libertyville",
    "zip": "60048",
    "county": "Lake County",
    "primary": False,
    "title": "Libertyville Realtor | Homes for Sale in 60048 | Rick Brown Coldwell Banker",
    "meta": "Need a Libertyville realtor near ZIP 60048? Rick Brown Coldwell Banker helps with downtown homes, later neighborhoods, buyer offers, and seller pricing. Office at 1133 So. Milwaukee Ave. Call 847-400-6018.",
    "h1": "Libertyville realtor helping buyers and sellers in ZIP 60048",
    "lead": "Based at 1133 So. Milwaukee Ave. in Libertyville, Rick Brown supports buyers and sellers across 60048 with local pricing, showing strategy, and clean transaction management.",
    "about": "Libertyville is known for a walkable downtown, historic residential character, Metra access, and recreation around Independence Grove. Traditional neighborhoods near downtown attract buyers who want older architecture and walkability, while later neighborhoods offer a more classic suburban layout. Pricing here is sensitive to location relative to downtown, schools, and updates.",
    "buyer": "Rick helps Libertyville buyers filter for lifestyle fit first, then narrow by budget and school priorities. Tours are organized around real options, not endless listing noise.",
    "seller": "Sellers in 60048 benefit from presentation that matches buyer expectations for the street and style of home. Rick builds a marketing and pricing plan around current Libertyville demand.",
    "nearby": "Clients often compare Libertyville with Vernon Hills 60061 and Buffalo Grove 60089 when weighing walkability, newer construction, and commute tradeoffs.",
    "faq1_q": "Where is Rick Brown's Libertyville office?",
    "faq1_a": "1133 So. Milwaukee Ave., Libertyville, IL 60048. Appointments are available in-office, at the property, or by phone.",
    "faq2_q": "Do you help with downtown Libertyville homes and newer subdivisions?",
    "faq2_a": "Yes. Rick works both character homes near downtown and later neighborhoods across 60048, with comps specific to each micro-market.",
  },
  {
    "slug": "buffalo-grove-60089",
    "city": "Buffalo Grove",
    "zip": "60089",
    "county": "Lake County / Cook County edge",
    "primary": False,
    "title": "Buffalo Grove Realtor | Homes for Sale in 60089 | Rick Brown Coldwell Banker",
    "meta": "Buffalo Grove realtor for ZIP 60089. Rick Brown Coldwell Banker helps buyers and sellers with local comps, offers, and listing strategy near Lake County. Call 847-400-6018.",
    "h1": "Buffalo Grove realtor for ZIP 60089 buyers and sellers",
    "lead": "Rick Brown helps homeowners and relocating buyers navigate Buffalo Grove 60089 with practical pricing, clear offer guidance, and local market context.",
    "about": "Buffalo Grove offers family-oriented neighborhoods, a practical price mix, and convenient access across Lake and Cook County corridors. Buyers often weigh attached homes against single-family streets. Sellers need accurate positioning because 60089 demand can move differently from neighboring Vernon Hills or Wheeling.",
    "buyer": "Rick builds a Buffalo Grove search around budget, school priorities, and commute. You get a short list that matches how you actually live, then disciplined offer support.",
    "seller": "For sellers, Rick focuses on condition, competitive set, and buyer feedback loops so pricing and presentation stay aligned with current 60089 traffic.",
    "nearby": "Many shoppers also consider Vernon Hills 60061, Wheeling 60090, and Arlington Heights 60005 when comparing value and location.",
    "faq1_q": "Can Rick help me sell in Buffalo Grove and buy elsewhere?",
    "faq1_a": "Yes. Dual moves are common. Rick maps contingencies and equity use so the sale and purchase timelines do not collide.",
    "faq2_q": "Is Buffalo Grove part of Rick's active service area?",
    "faq2_a": "Yes. 60089 is one of the listed coverage ZIPs alongside the primary Vernon Hills market.",
  },
  {
    "slug": "wheeling-60090",
    "city": "Wheeling",
    "zip": "60090",
    "county": "Cook County / Lake County edge",
    "primary": False,
    "title": "Wheeling Realtor | Homes for Sale in 60090 | Rick Brown Coldwell Banker",
    "meta": "Wheeling IL realtor for ZIP 60090. Rick Brown Coldwell Banker supports buyers and sellers with market comps, negotiations, and a clear home search plan. Call 847-400-6018.",
    "h1": "Wheeling realtor covering ZIP 60090 for buyers and sellers",
    "lead": "If you are buying or selling in Wheeling 60090, Rick Brown brings Lake County and NW suburban market experience to your offer, pricing, and closing timeline.",
    "about": "Wheeling attracts buyers looking for connectivity, practical inventory, and access into the northwest suburbs. The ZIP often serves move-up and first-time buyers who want value relative to neighboring Buffalo Grove or Arlington Heights. Local comps matter because attached and detached inventory can behave differently.",
    "buyer": "Rick helps Wheeling buyers set a realistic spending lane, tour efficiently, and negotiate from data instead of hope. Financing timing and inspection plans stay front and center.",
    "seller": "Sellers get a prep checklist, pricing against current 60090 competition, and showing strategy designed to generate strong early interest.",
    "nearby": "Nearby searches often expand into Buffalo Grove 60089, Arlington Heights 60005, and Vernon Hills 60061 depending on budget.",
    "faq1_q": "Do you work with first-time buyers in Wheeling?",
    "faq1_a": "Yes. Rick explains offer structure, contingencies, and closing steps in plain language so first-time buyers move with confidence.",
    "faq2_q": "How do I start a seller consult in 60090?",
    "faq2_a": "Call 847-400-6018 or send the form on this page. Include address and timeline for the fastest turnaround.",
  },
  {
    "slug": "winnetka-60093",
    "city": "Winnetka / Northfield",
    "zip": "60093",
    "county": "Cook County North Shore",
    "primary": False,
    "title": "Winnetka & Northfield Realtor | ZIP 60093 | Rick Brown Coldwell Banker",
    "meta": "Realtor for Winnetka and Northfield ZIP 60093. Rick Brown Coldwell Banker assists with North Shore buying and selling strategy, pricing, and negotiations. Call 847-400-6018.",
    "h1": "Winnetka & Northfield realtor for buyers and sellers in 60093",
    "lead": "Rick Brown helps clients evaluating Winnetka and Northfield 60093 with careful pricing, discreet representation, and a plan that respects North Shore buyer expectations.",
    "about": "ZIP 60093 covers Winnetka and Northfield, markets where presentation, lot, school context, and renovation quality can shift pricing quickly. Buyers and sellers often need nuanced comps rather than broad average values. Rick pairs North Shore expectations with clear next steps.",
    "buyer": "For buyers, Rick focuses on fit, condition, and negotiation leverage. Showings are targeted. Offers are structured with local norms in mind.",
    "seller": "Sellers receive a prep and pricing conversation rooted in current 60093 activity, then a marketing path aimed at qualified interest without unnecessary delay.",
    "nearby": "Clients compare 60093 with Libertyville 60048, Vernon Hills 60061, and other North Shore options when lifestyle and commute priorities differ.",
    "faq1_q": "Is 60093 within Rick's coverage?",
    "faq1_a": "Yes. Winnetka and Northfield are part of the listed service ZIP set, with Libertyville as the office base.",
    "faq2_q": "Can I get a confidential seller consult?",
    "faq2_a": "Yes. Call or email Rick directly. He can discuss pricing privately before any public listing conversation.",
  },
  {
    "slug": "palatine-60094",
    "city": "Palatine",
    "zip": "60094",
    "county": "Cook County",
    "primary": False,
    "title": "Palatine Realtor | Homes & Seller Help in 60094 | Rick Brown Coldwell Banker",
    "meta": "Palatine realtor support for ZIP 60094. Rick Brown Coldwell Banker helps with home search, listing strategy, and negotiations. Call 847-400-6018 for a free consult.",
    "h1": "Palatine realtor helping clients in and around ZIP 60094",
    "lead": "Rick Brown supports buyers and sellers connected to Palatine 60094 with straightforward market guidance and full transaction coordination through Coldwell Banker.",
    "about": "Palatine buyers and sellers often need help translating neighborhood differences into price and timing decisions. Whether you are relocating into the northwest suburbs or preparing a local sale, Rick keeps the plan simple and local. Coverage for 60094 is part of a broader set that includes Arlington Heights and Buffalo Grove.",
    "buyer": "Buyers get help defining must-haves, touring options that match budget, and writing competitive but responsible offers.",
    "seller": "Sellers get a clear pricing frame, listing prep priorities, and negotiation support from first showing through closing.",
    "nearby": "Common comparison ZIPs include Arlington Heights 60005, Buffalo Grove 60089, and Wheeling 60090.",
    "faq1_q": "Do you only work Lake County, or also Palatine?",
    "faq1_a": "Rick's primary focus is Vernon Hills 60061 and Lake County, with active coverage that includes Palatine 60094 and other nearby suburbs.",
    "faq2_q": "How soon can we tour homes?",
    "faq2_a": "Often same-day or next-day depending on listing access. Call or text 847-400-6018 with your must-haves and budget.",
  },
  {
    "slug": "arlington-heights-60005",
    "city": "Arlington Heights",
    "zip": "60005",
    "county": "Cook County",
    "primary": False,
    "title": "Arlington Heights Realtor | ZIP 60005 Homes | Rick Brown Coldwell Banker",
    "meta": "Arlington Heights realtor for ZIP 60005. Rick Brown Coldwell Banker helps buyers and sellers with local comps, Metra-town living, and listing strategy. Call 847-400-6018.",
    "h1": "Arlington Heights realtor for buyers and sellers in ZIP 60005",
    "lead": "Rick Brown helps people buying or selling in Arlington Heights 60005 with practical market advice, strong negotiation support, and a clean path to closing.",
    "about": "Arlington Heights is a classic train-town northwest suburb with established residential streets and active buyer interest around lifestyle and commute. ZIP 60005 can include a mix of housing styles, so local comps and condition drive pricing more than ZIP-wide averages alone.",
    "buyer": "Rick helps buyers prioritize proximity, updates, and school considerations, then manage offers in a competitive suburban setting.",
    "seller": "Sellers get a plan for presentation, pricing, and timing that reflects current 60005 demand and nearby competition.",
    "nearby": "Buyers often compare Arlington Heights with Buffalo Grove 60089, Palatine 60094, and Wheeling 60090.",
    "faq1_q": "Can Rick represent me as a buyer in Arlington Heights?",
    "faq1_a": "Yes. Buyer representation covers search strategy, tours, offers, inspections, and closing coordination.",
    "faq2_q": "What if I need to sell in 60005 and buy in Vernon Hills?",
    "faq2_a": "That is a common path. Rick sequences the sale and purchase with contingencies and equity planning so both sides stay on track.",
  },
]

nav_links = "\n".join(
    f'          <li><a href="{a["slug"]}.html">{a["city"].split(" / ")[0]} {a["zip"]}</a></li>'
    for a in areas
)

for a in areas:
    badge = "Primary coverage ZIP" if a["primary"] else f"Service area · {a['county']}"
    others = [x for x in areas if x["slug"] != a["slug"]]
    related_parts = []
    for x in others[:6]:
        cls = "area-link primary" if x["primary"] else "area-link"
        related_parts.append(
            f'          <a class="{cls}" href="{x["slug"]}.html">\n'
            f'            <span class="zip">{x["zip"]}</span>\n'
            f'            <h3>{x["city"]}</h3>\n'
            f'            <p>Local realtor guidance for {x["city"]} {x["zip"]}.</p>\n'
            f"          </a>"
        )
    related = "\n".join(related_parts)
    city_short = a["city"].split(" / ")[0]

    html = f"""<!DOCTYPE html>
<html lang="en-US">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{a["title"]}</title>
  <meta name="description" content="{a["meta"]}">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <meta name="geo.region" content="US-IL">
  <meta name="geo.placename" content="{a["city"]}, Illinois">
  <link rel="canonical" href="https://rickbrownhomes.com/areas/{a["slug"]}.html">
  <meta property="og:type" content="website">
  <meta property="og:title" content="{a["title"]}">
  <meta property="og:description" content="{a["meta"]}">
  <meta property="og:url" content="https://rickbrownhomes.com/areas/{a["slug"]}.html">
  <meta property="og:image" content="https://rickbrownhomes.com/images/rick-brown-720.jpg">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600;700&family=Figtree:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../css/styles.css">
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@graph": [
      {{
        "@type": "RealEstateAgent",
        "@id": "https://rickbrownhomes.com/#business",
        "name": "Rick Brown | Coldwell Banker",
        "image": "https://rickbrownhomes.com/images/rick-brown-720.jpg",
        "url": "https://rickbrownhomes.com/",
        "telephone": "+18474006018",
        "email": "rick.brown@cbexchange.com",
        "address": {{
          "@type": "PostalAddress",
          "streetAddress": "1133 So. Milwaukee Ave.",
          "addressLocality": "Libertyville",
          "addressRegion": "IL",
          "postalCode": "60048",
          "addressCountry": "US"
        }},
        "areaServed": {{
          "@type": "PostalCode",
          "name": "{a["zip"]}",
          "description": "{a["city"]}, IL"
        }},
        "sameAs": [
          "https://www.zillow.com/profile/user8984945",
          "https://www.facebook.com/rick.brown.925602"
        ]
      }},
      {{
        "@type": "WebPage",
        "@id": "https://rickbrownhomes.com/areas/{a["slug"]}.html#webpage",
        "url": "https://rickbrownhomes.com/areas/{a["slug"]}.html",
        "name": "{a["title"]}",
        "description": "{a["meta"]}",
        "about": {{"@id": "https://rickbrownhomes.com/#business"}},
        "breadcrumb": {{
          "@type": "BreadcrumbList",
          "itemListElement": [
            {{"@type": "ListItem", "position": 1, "name": "Home", "item": "https://rickbrownhomes.com/"}},
            {{"@type": "ListItem", "position": 2, "name": "Service Areas", "item": "https://rickbrownhomes.com/#areas"}},
            {{"@type": "ListItem", "position": 3, "name": "{a["city"]} {a["zip"]}", "item": "https://rickbrownhomes.com/areas/{a["slug"]}.html"}}
          ]
        }}
      }},
      {{
        "@type": "Service",
        "name": "Real estate services in {a["city"]} {a["zip"]}",
        "provider": {{"@id": "https://rickbrownhomes.com/#business"}},
        "areaServed": "{a["city"]}, IL {a["zip"]}",
        "description": "Buyer and seller representation for homes in {a["city"]}, Illinois ZIP {a["zip"]}."
      }}
    ]
  }}
  </script>
</head>
<body>
  <div class="topbar">
    <div class="container">
      <span>Coldwell Banker · {a["city"]} {a["zip"]}</span>
      <span>
        <a href="tel:+18474006018">847-400-6018</a>
        ·
        <a href="mailto:rick.brown@cbexchange.com">rick.brown@cbexchange.com</a>
      </span>
    </div>
  </div>

  <header class="site-header">
    <div class="container">
      <a class="brand" href="../index.html">
        <span class="brand-name">Rick Brown</span>
        <span class="brand-tag">Coldwell Banker</span>
      </a>
      <button class="nav-toggle" type="button" aria-label="Open menu" aria-expanded="false">☰</button>
      <nav class="nav" aria-label="Primary">
        <a href="../index.html#areas">Service Areas</a>
        <a href="../index.html#services">Services</a>
        <a href="#contact">Contact</a>
        <a class="nav-cta" href="tel:+18474006018">Call Now</a>
      </nav>
    </div>
  </header>

  <main>
    <section class="page-hero">
      <div class="container">
        <p class="breadcrumb"><a href="../index.html">Home</a> / Service Areas / {a["city"]} {a["zip"]}</p>
        <p class="eyebrow" style="color:#f0c34a">{badge}</p>
        <h1>{a["h1"]}</h1>
        <p>{a["lead"]}</p>
        <div class="hero-actions" style="margin-top:1.5rem">
          <a class="btn btn-primary" href="#contact">Free {city_short} consult</a>
          <a class="btn btn-ghost" href="tel:+18474006018">847-400-6018</a>
        </div>
      </div>
    </section>

    <section class="section section-tight" style="background:#fff;border-bottom:1px solid var(--line)">
      <div class="container split about-split" style="gap:1.5rem;align-items:center">
        <div class="split-visual photo-frame">
          <img class="agent-portrait-clean" src="../images/rick-brown-600.jpg" srcset="../images/rick-brown-400.jpg 400w, ../images/rick-brown-600.jpg 600w, ../images/rick-brown-720.jpg 720w" sizes="280px" alt="Rick Brown, Coldwell Banker realtor" width="280" height="280" loading="lazy" decoding="async">
        </div>
        <div>
          <p class="eyebrow">Your realtor</p>
          <h2 style="font-family:var(--font-display);font-size:1.9rem;margin:0 0 .5rem">Rick Brown · 177 total sales</h2>
          <p style="margin:0;color:var(--muted)">Coldwell Banker agent specializing in buyer representation, listings, and new construction. Rick helps buyers and sellers in {a["city"]} with pricing, negotiation, and a personal approach built on trust.</p>
          <div class="profile-links" style="margin-top:1rem">
            <a class="btn btn-dark" href="https://www.zillow.com/profile/user8984945" target="_blank" rel="noopener noreferrer">Zillow profile</a>
            <a class="btn btn-outline" href="https://www.facebook.com/rick.brown.925602" target="_blank" rel="noopener noreferrer">Facebook</a>
            <a class="btn btn-outline" href="../index.html#about">Full bio</a>
          </div>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container prose">
        <p class="eyebrow">{a["city"]} real estate</p>
        <h2>Local context for buying or selling in {a["zip"]}</h2>
        <p>{a["about"]}</p>
        <h2>Buying a home in {a["city"]}</h2>
        <p>{a["buyer"]}</p>
        <h2>Selling a home in {a["zip"]}</h2>
        <p>{a["seller"]}</p>
        <h2>Nearby markets clients also compare</h2>
        <p>{a["nearby"]}</p>
        <ul class="check-list">
          <li>Free consultation by phone, text, or email</li>
          <li>Local comps and pricing conversation before you commit</li>
          <li>Buyer and seller representation through Coldwell Banker</li>
          <li>Office at 1133 So. Milwaukee Ave., Libertyville, IL 60048</li>
        </ul>
      </div>
    </section>

    <section class="section" style="background:#fff">
      <div class="container" style="display:grid;grid-template-columns:0.9fr 1.1fr;gap:2rem;align-items:start">
        <div class="section-head" style="margin:0">
          <p class="eyebrow">FAQ · {a["zip"]}</p>
          <h2>Questions buyers and sellers ask about {a["city"]}</h2>
        </div>
        <div class="faq">
          <details open>
            <summary>{a["faq1_q"]}</summary>
            <p>{a["faq1_a"]}</p>
          </details>
          <details>
            <summary>{a["faq2_q"]}</summary>
            <p>{a["faq2_a"]}</p>
          </details>
          <details>
            <summary>How do I contact Rick Brown?</summary>
            <p>Call or text 847-400-6018, email rick.brown@cbexchange.com, or use the form below. Connect on <a href="https://www.zillow.com/profile/user8984945" target="_blank" rel="noopener noreferrer">Zillow</a> or <a href="https://www.facebook.com/rick.brown.925602" target="_blank" rel="noopener noreferrer">Facebook</a>.</p>
          </details>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="section-head">
          <p class="eyebrow">More service areas</p>
          <h2>Explore nearby ZIP coverage</h2>
        </div>
        <div class="area-grid">
{related}
        </div>
      </div>
    </section>

    <section class="section contact-band" id="contact">
      <div class="container contact-grid">
        <div class="contact-copy">
          <p class="eyebrow" style="color:#f0c34a">Talk with Rick</p>
          <h2 style="font-family:var(--font-display);font-size:clamp(2rem,4vw,2.6rem);margin:0 0 .75rem;line-height:1.1">Ready for a {a["city"]} market consult?</h2>
          <p style="margin:0;color:rgba(255,255,255,.8)">Share your goal for {a["zip"]}. Rick will reply with next steps by phone or email.</p>
          <dl class="contact-meta">
            <div>
              <dt>Phone / Text</dt>
              <dd><a href="tel:+18474006018">847-400-6018</a></dd>
            </div>
            <div>
              <dt>Email</dt>
              <dd><a href="mailto:rick.brown@cbexchange.com">rick.brown@cbexchange.com</a></dd>
            </div>
            <div>
              <dt>Office NAP</dt>
              <dd>1133 So. Milwaukee Ave., Libertyville, IL 60048</dd>
            </div>
          </dl>
        </div>
        <div class="form-panel">
          <h3>Start with {a["city"]}</h3>
          <p>Form opens an email draft to Rick with your details ready to send.</p>
          <form id="lead-form" novalidate>
            <div class="form-grid">
              <label>Full name*<input type="text" name="name" required></label>
              <label>Phone*<input type="tel" name="phone" required></label>
              <label class="full">Email*<input type="email" name="email" required></label>
              <label>Area / ZIP
                <select name="area" id="area">
                  <option value="{a["city"]} {a["zip"]}" selected>{a["city"]} {a["zip"]}</option>
                  <option value="Vernon Hills 60061">Vernon Hills 60061</option>
                  <option value="Libertyville 60048">Libertyville 60048</option>
                  <option value="Buffalo Grove 60089">Buffalo Grove 60089</option>
                  <option value="Wheeling 60090">Wheeling 60090</option>
                  <option value="Winnetka / Northfield 60093">Winnetka / Northfield 60093</option>
                  <option value="Palatine 60094">Palatine 60094</option>
                  <option value="Arlington Heights 60005">Arlington Heights 60005</option>
                </select>
              </label>
              <label>Goal
                <select name="goal">
                  <option value="Buying">Buying</option>
                  <option value="Selling">Selling</option>
                  <option value="Buying and Selling">Buying and Selling</option>
                  <option value="Home value check">Home value check</option>
                </select>
              </label>
              <label class="full">Message<textarea name="message" placeholder="Address, timeline, or what you need..."></textarea></label>
              <div class="full">
                <button class="btn btn-primary" type="submit" style="width:100%">Send to Rick</button>
                <div id="form-status" class="form-status" role="status" aria-live="polite"></div>
              </div>
            </div>
          </form>
        </div>
      </div>
    </section>
  </main>

  <footer class="site-footer">
    <div class="container footer-grid">
      <div>
        <h2>Rick Brown</h2>
        <p>Coldwell Banker · {a["city"]} {a["zip"]} and surrounding markets.</p>
        <p style="margin-top:1rem">1133 So. Milwaukee Ave.<br>Libertyville, IL 60048<br><a href="tel:+18474006018">847-400-6018</a></p>
      </div>
      <div>
        <h3>Service Areas</h3>
        <ul>
{nav_links}
        </ul>
      </div>
      <div>
        <h3>Links</h3>
        <ul>
          <li><a href="../index.html">Home</a></li>
          <li><a href="../index.html#contact">Contact</a></li>
          <li><a href="https://www.zillow.com/profile/user8984945" target="_blank" rel="noopener noreferrer">Zillow</a></li>
          <li><a href="https://www.facebook.com/rick.brown.925602" target="_blank" rel="noopener noreferrer">Facebook</a></li>
        </ul>
      </div>
    </div>
    <div class="container footer-bottom">
      <span>© 2026 Rick Brown | Coldwell Banker</span>
      <span>Equal Housing Opportunity</span>
    </div>
  </footer>
  <script src="../js/main.js"></script>
</body>
</html>
"""
    path = base / f'{a["slug"]}.html'
    path.write_text(html)
    print("Wrote", path.name)

print("Done", len(areas), "area pages")
