# Rick Brown | RE/MAX — Local SEO Landing Site

Static, SEO-focused landing site for Rick Brown (RE/MAX), Libertyville / Vernon Hills market.

## Preview locally

```bash
cd "/Users/macbookpro/Desktop/Business - Websites/rick-brown-remax"
python3 -m http.server 8080
```

Open http://localhost:8080

## Pages

- `/` Homepage (primary Vernon Hills 60061 targeting)
- `/areas/vernon-hills-60061.html` Primary ZIP
- `/areas/libertyville-60048.html` Office city
- `/areas/buffalo-grove-60089.html`
- `/areas/wheeling-60090.html`
- `/areas/winnetka-60093.html`
- `/areas/palatine-60094.html`
- `/areas/arlington-heights-60005.html`

## Built-in SEO

- Unique title + meta description per page
- Canonical URLs
- JSON-LD: RealEstateAgent, Person, WebPage, Service, BreadcrumbList
- NAP consistency (name, address, phone) sitewide
- Google Maps embed (office)
- `sitemap.xml`, `robots.txt`, `llms.txt` (AI/GEO)
- Internal links between all ZIP pages
- Click-to-call + working lead form (mailto draft to rick.brown@remax.net)

## Before going live

1. Replace `https://rickbrownhomes.com` with the real domain in:
   - all HTML canonical / schema / OG tags
   - `sitemap.xml`
   - `robots.txt`
   - `llms.txt`
2. Connect a real form backend (Formspree, Getform, HubSpot, or GHL webhook) if you want inbox leads without mailto.
3. Claim / optimize Google Business Profile for the Libertyville address.
4. Submit sitemap in Google Search Console.
5. Add real headshot and brokerage-approved photos when available.
6. Confirm RE/MAX co-branding / disclaimer requirements with the office.

## Contact data used

- Rick Brown
- 847-400-6018
- rick.brown@remax.net
- 1133 So. Milwaukee Ave., Libertyville, IL 60048
- Zillow: https://www.zillow.com/profile/user8984945
- Primary ZIP: 60061 (Vernon Hills)
