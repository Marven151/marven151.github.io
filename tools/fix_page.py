"""en/fix/: the one-screen landing that the US outreach e-mails link to. Website fixes only, no data services."""
import html
from strings import MAIL, SITE

URL = SITE + "en/fix/"
TITLE = "Website fix for a fixed price"
DESC = "Mobile layout, HTTPS, a contact form that sends nothing, an out-of-date footer, slow photos: fixed for $60–$300, paid when you've checked it works."

PRICES = [
    ("Phone layout", "$90", "Your site shows the desktop version on a phone and people pinch to read it. I add the mobile layout so it fits any screen."),
    ("HTTPS and the “Not secure” label", "$90", "The certificate and the redirect, so Chrome stops warning your visitors. Usually free hosting-side, I set it up."),
    ("Contact form that actually sends", "$120", "A form that lands in your inbox with a copy to the customer, spam filtered."),
    ("Speed: photos and loading", "$150", "Photos shrunk from megabytes to kilobytes without visible loss, loading under two seconds on a phone."),
    ("Footer year, texts, hours, menu", "$60", "The small things that make a site look abandoned: the © year, old hours, a closed-location address."),
    ("Several at once", "under $300", "Quoted up front as one number. If it needs a rebuild instead, a one-page site is $450 flat."),
]

STEPS = [
    ("Reply to the e-mail, or write below", "Tell me it's fine to look. I already know which problem I saw."),
    ("I send the fixed version on a test address", "Within three working days: a link to the repaired page next to a screenshot of the current one."),
    ("You check it, then it goes live, then you pay", "Card, PayPal or bank transfer, invoice included. Your site stays with your hosting and your domain; nothing depends on me afterwards."),
]

CSS = r"""
:root{--bg:#edccbe;--tone:#e3b9a8;--ink:#351a2b;--muted:#6c4857;--ink3:#241120;--display:'Bodoni Moda',Georgia,serif;--text:'Jost',system-ui,sans-serif}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font:400 clamp(1.0625rem,1rem + .25vw,1.1875rem)/1.6 var(--text);-webkit-font-smoothing:antialiased}
h1,h2,h3,p,ul,ol,dl,dd,figure{margin:0}
a{color:inherit}
img{display:block;max-width:100%;height:auto}
.wrap{max-width:1080px;margin:0 auto;padding:0 clamp(16px,5vw,64px)}
.display{font-family:var(--display);font-weight:500;letter-spacing:-.02em;line-height:.98}
.stripe{display:flex;width:100%;height:28px;overflow:hidden}
.stripe i{flex:none;width:28px;height:100%;background:var(--ink)}
.stripe i:nth-child(even){background:var(--bg)}
header{background:var(--ink);color:var(--bg);padding:clamp(40px,8vw,96px) 0 clamp(36px,6vw,72px)}
header .kicker{font-size:.875rem;letter-spacing:.14em;text-transform:uppercase;opacity:.75}
header h1{font-size:clamp(2.25rem,6.5vw,5rem);margin:14px 0 22px;max-width:14ch}
header p{max-width:60ch;font-size:clamp(1.125rem,1.05rem + .5vw,1.375rem);opacity:.92}
.btn{display:inline-flex;align-items:center;min-height:52px;padding:0 28px;background:var(--bg);color:var(--ink);text-decoration:none;font-weight:500;margin-top:28px}
.btn.ink{background:var(--ink);color:var(--bg)}
section{padding:clamp(40px,7vw,88px) 0}
section h2{font-size:clamp(1.75rem,4vw,2.75rem);margin-bottom:clamp(20px,3vw,36px)}
.proof{display:grid;grid-template-columns:1fr 1fr;gap:clamp(16px,3vw,40px);align-items:center}
.proof figure{background:var(--ink);padding:8px}
.proof figcaption{color:var(--bg);font-size:.875rem;padding:10px 6px 4px;opacity:.8}
.scores{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:20px}
.scores div{background:var(--tone);padding:14px 16px}
.scores b{display:block;font-family:var(--display);font-size:2rem;font-weight:500;line-height:1}
.scores span{font-size:.875rem;color:var(--muted)}
.prices{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:12px}
.prices article{background:var(--tone);padding:22px 22px 24px;display:flex;flex-direction:column;gap:8px}
.prices h3{font-size:1.125rem;font-weight:500}
.prices .p{font-family:var(--display);font-size:2.25rem;font-weight:500;line-height:1}
.prices p{color:var(--ink);font-size:1rem}
ol.steps{list-style:none;padding:0;display:grid;gap:14px;counter-reset:s}
ol.steps li{display:grid;grid-template-columns:56px 1fr;gap:16px;background:var(--tone);padding:20px}
ol.steps li::before{counter-increment:s;content:counter(s);font-family:var(--display);font-size:2.5rem;line-height:1;font-weight:500}
ol.steps b{display:block;font-weight:500;margin-bottom:4px}
.trust{background:var(--ink);color:var(--bg)}
.trust ul{list-style:none;padding:0;display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:18px 32px;font-size:1rem}
.trust li::before{content:"\2014  ";opacity:.6}
.contact p{max-width:60ch}
.contact .mail{font-family:var(--display);font-size:clamp(1.5rem,3.5vw,2.5rem);word-break:break-all;display:inline-block;margin:16px 0 4px}
footer{padding:28px 0 40px;font-size:.875rem;color:var(--muted)}
footer a{margin-right:18px}
@media (max-width:720px){.proof{grid-template-columns:1fr}.scores{grid-template-columns:1fr 1fr}ol.steps li{grid-template-columns:40px 1fr;padding:16px}}
"""


def esc(s): return html.escape(s, quote=True)


def page():
    prices = "".join(f'<article><h3>{esc(t)}</h3><div class="p">{esc(p)}</div><p>{esc(d)}</p></article>' for t, p, d in PRICES)
    steps = "".join(f'<li><div><b>{esc(t)}</b>{esc(d)}</div></li>' for t, d in STEPS)
    subject = "My website: " + "the e-mail you sent"
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(TITLE)} · Marcin Świerczyński</title>
<meta name="description" content="{esc(DESC)}">
<link rel="canonical" href="{URL}">
<meta name="robots" content="noindex">
<meta property="og:title" content="{esc(TITLE)}"><meta property="og:description" content="{esc(DESC)}"><meta property="og:url" content="{URL}"><meta property="og:image" content="{SITE}img/og.jpg">
<meta name="theme-color" content="#351a2b">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bodoni+Moda:ital,opsz,wght@0,6..96,500&family=Jost:wght@400;500&display=swap" rel="stylesheet" media="print" onload="this.media='all'">
<noscript><link href="https://fonts.googleapis.com/css2?family=Bodoni+Moda:ital,opsz,wght@0,6..96,500&family=Jost:wght@400;500&display=swap" rel="stylesheet"></noscript>
<style>{CSS}</style>
</head>
<body>
<header><div class="wrap">
<p class="kicker">Marcin Świerczyński · web developer, Poland · for US small businesses</p>
<h1 class="display">Your website has a problem. I'll fix it for a fixed price.</h1>
<p>You got my e-mail because I found something concrete on your site: a layout that breaks on a phone, a "Not secure" label, a form that sends nothing, photos that take ten seconds to load. I fix that kind of thing for $60–$300, and you only pay when you've checked that it works.</p>
<a class="btn" href="#contact">Tell me it's fine to look</a>
</div></header>
<div class="stripe">{"".join("<i></i>" for _ in range(80))}</div>

<section><div class="wrap">
<h2 class="display">What a fix looks like</h2>
<div class="proof">
<figure><img src="../../img/site-fix-demo.webp" alt="A bakery website before and after the fixes, with Lighthouse scores" width="1280" height="800"><figcaption>A small bakery site, broken on the left and repaired on the right. Photos went from 4.9 MB to 303 KB, the form sends, the layout fits a phone. <a href="https://marven151.github.io/site-fix-demo/">Open the demo</a></figcaption></figure>
<div>
<p>Same business, same content, same hosting. Nothing was rebuilt; the broken parts were fixed. The numbers are Google's own Lighthouse scores, before and after.</p>
<div class="scores">
<div><b>75 → 100</b><span>performance</span></div>
<div><b>45 → 100</b><span>accessibility</span></div>
<div><b>4.9 MB → 303 KB</b><span>photos</span></div>
<div><b>3 days</b><span>from your go-ahead to the test link</span></div>
</div>
</div>
</div>
</div></section>

<section style="padding-top:0"><div class="wrap">
<h2 class="display">Prices, agreed before I start</h2>
<div class="prices">{prices}</div>
</div></section>

<section style="padding-top:0"><div class="wrap">
<h2 class="display">How it goes</h2>
<ol class="steps">{steps}</ol>
</div></section>

<section class="trust"><div class="wrap">
<ul>
<li>Freelance developer in Poland, working US hours by e-mail. No calls needed.</li>
<li>Invoice with every job. Card, PayPal or bank transfer, after you've checked the work.</li>
<li>You keep every file and every login; the site stays on your hosting and your domain.</li>
<li>Code and other work: <a href="{SITE}en/">marven151.github.io/en</a></li>
</ul>
</div></section>

<section class="contact" id="contact"><div class="wrap">
<h2 class="display">Write to me</h2>
<p>One line is enough: your website address and "go ahead and look". You'll get the fixed version on a test link within three working days, with the price next to it.</p>
<a class="mail" href="mailto:{MAIL}?subject={esc(subject)}">{MAIL}</a>
<p style="font-size:.9375rem;color:var(--muted)">Or just reply to the e-mail I sent you.</p>
</div></section>

<footer><div class="wrap"><a href="{SITE}en/">All services</a><a href="{SITE}informacja/">Data notice</a>Marcin Świerczyński, Poland</div></footer>
</body>
</html>'''
