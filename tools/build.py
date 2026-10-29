import json, html, os

HERE = os.path.dirname(os.path.abspath(__file__))
from strings import PL, EN, MAIL, SITE

CSS = r"""
:root{
  --bg:#edccbe; --tone:#e3b9a8; --tone2:#d6a998; --ink:#351a2b; --muted:#6c4857; --ink2:#4a2a3e; --ink3:#241120;
  --m:12px; --gap:16px; --pad:clamp(20px,6vw,96px);
  --step-small:clamp(.8125rem,.79rem + .1vw,.875rem);
  --step-body:clamp(1.0625rem,1rem + .25vw,1.1875rem);
  --step-lead:clamp(1.25rem,1.1rem + .7vw,1.625rem);
  --display:'Bodoni Moda',Georgia,serif; --text:'Jost',system-ui,sans-serif;
  --ease:cubic-bezier(.16,1,.3,1);
}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--ink);font:400 var(--step-body)/1.6 var(--text);letter-spacing:.01em;-webkit-font-smoothing:antialiased}
h1,h2,h3,p,ul,ol,dl,dd,figure{margin:0}
a{color:inherit}
img{display:block;max-width:100%}
button,input,textarea{font:inherit;color:inherit;letter-spacing:inherit}
button{background:none;border:0;padding:0;cursor:pointer}
:focus-visible{outline:2px solid currentColor;outline-offset:3px}
::selection{background:var(--ink);color:var(--bg)}
.skip{position:absolute;left:-999px;top:8px;background:var(--bg);color:var(--ink);padding:10px 16px;z-index:100}
.skip:focus{left:8px}
.display{font-family:var(--display);font-weight:500;letter-spacing:-.02em;line-height:.95}
.btn{display:inline-flex;align-items:center;justify-content:center;min-height:52px;padding:0 30px;background:var(--ink);color:var(--bg);text-decoration:none;font-weight:500;transition:background .2s,color .2s,transform .2s var(--ease)}
.btn:hover{background:var(--ink3)}
.btn:active{transform:translateY(1px)}
.btn.inv{background:var(--bg);color:var(--ink)}
.stripe{display:flex;width:100%;height:56px;overflow:hidden;flex:none}
.stripe i{flex:none;width:28px;height:100%;background:var(--ink)}
.stripe i:nth-child(even){background:var(--bg)}

/* hero */
.hero{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:12px;padding:12px;background:var(--ink)}
.card{position:relative;min-width:0;overflow:hidden;background:var(--bg);display:flex;flex-direction:column;align-items:center;text-align:center;min-height:calc(100svh - 24px)}
.me{position:absolute;right:clamp(20px,3.4vw,48px);top:clamp(84px,11svh,120px);width:clamp(92px,8vw,124px);padding:6px;background:var(--tone);transform:rotate(3deg)}
.me img{width:100%;height:auto;aspect-ratio:4/5;object-fit:cover;background:var(--ink2)}
.card .mark{margin-top:clamp(28px,7svh,72px);font-size:clamp(3.25rem,5.6vw,5.5rem)}
.card h1{margin-top:clamp(24px,5svh,48px);font-size:clamp(2.5rem,3.6vw,3.5rem);line-height:1}
.card .lead{margin:24px auto 32px;max-width:36ch;font-size:1.0625rem;color:var(--ink)}
.card .links{margin-top:auto;padding:28px 20px;display:flex;gap:28px;flex-wrap:wrap;justify-content:center;font-size:15px}
.card .links a{text-decoration:none;padding:6px 0}
.card .links a:hover{text-decoration:underline;text-underline-offset:5px}
.photo{position:sticky;top:12px;height:calc(100svh - 24px);overflow:hidden;background:var(--ink2)}
.slide{position:absolute;inset:0;display:flex;flex-direction:column;justify-content:center;gap:18px;padding:0 clamp(16px,3vw,48px);color:var(--bg);opacity:0}
.slide:first-child{opacity:1}
.slide .frm{background:var(--ink3)}
.slide .frm .bar{height:32px;display:flex;align-items:center;padding:0 12px;font-size:13px;color:var(--bg)}
.slide .frm .url{overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.slide img{width:100%;height:auto;aspect-ratio:16/10;object-fit:contain;background:var(--ink2)}
.slide figcaption{font-size:15px}

/* work */
.work{background:var(--ink);color:var(--bg);padding:clamp(96px,12vw,200px) 0 clamp(120px,14vw,240px)}
.work header{padding:0 var(--pad) 56px;display:flex;align-items:baseline;gap:32px;flex-wrap:wrap}
.work h2{font-size:32px}
.work header p{font-size:15px;color:var(--bg)}
.folder{--n:0;position:sticky;top:calc(var(--n) * 64px);min-height:82svh;background:var(--bg);color:var(--ink);margin-top:44px;padding:64px var(--pad) 40px;display:grid;grid-template-columns:repeat(12,1fr);column-gap:var(--gap);align-content:start}
.folder:nth-of-type(even){background:var(--tone)}
.tabs{position:absolute;left:var(--pad);top:-44px;display:flex;gap:6px}
.tab{height:44px;display:flex;align-items:center;padding:0 34px 0 24px;background:var(--ink3);color:var(--bg);clip-path:polygon(0 100%,0 14px,14px 0,calc(100% - 22px) 0,100% 100%)}
.tab.n{font-family:var(--display);font-weight:500;font-size:26px;letter-spacing:-.01em}
.tab.s{background:var(--ink2);font-size:15px}
.folder .kind{position:absolute;right:var(--pad);top:-44px;height:44px;display:flex;align-items:center;padding:0 22px;background:var(--ink2);color:var(--bg);font-size:15px}
.dev{grid-column:1/9;align-self:start;background:var(--ink3);color:var(--bg)}
.dev .bar{height:40px;display:flex;align-items:center;justify-content:space-between;gap:12px;padding:0 14px;font-size:14px}
.dev .url{min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;color:var(--bg)}
.dev .tg{display:flex;gap:6px;flex:none}
.dev .tg button{min-height:28px;padding:0 12px;font-size:14px;background:var(--ink2);color:var(--bg);transition:background .2s,color .2s}
.dev .tg button:hover{background:var(--ink)}
.dev .tg button.on{background:var(--bg);color:var(--ink)}
.dev .view{position:relative;aspect-ratio:16/10;overflow:hidden;background:var(--ink2)}
.dev .view .poster{position:absolute;inset:0;width:100%;height:100%;object-fit:contain;object-position:50% 0;transition:opacity .4s}
.dev .view iframe{position:absolute;left:0;top:0;border:0;background:#fff;transform-origin:0 0;opacity:0;transition:opacity .4s;pointer-events:none}
.dev.loaded .view iframe{opacity:1}
.dev.loaded .view .poster{opacity:0}
.dev .view.act iframe{pointer-events:auto}
.dev .view::after{content:attr(data-hint);position:absolute;right:12px;bottom:12px;padding:6px 12px;font-size:13px;background:var(--ink3);color:var(--bg);opacity:0;transition:opacity .2s;pointer-events:none}
.dev.loaded .view:not(.act):hover::after{opacity:.92}
.folder .txt{grid-column:9/13;align-self:start;padding-top:40px}
.q{margin:24px 0 0;padding:0}
.q p{font-family:var(--display);font-weight:500;font-size:1.375rem;line-height:1.25;letter-spacing:-.01em;max-width:30ch}
.q footer{margin-top:8px;font-size:15px}
.ci{margin-top:20px;font-size:15px}
.ci b{font-family:var(--display);font-weight:500;font-size:1.75rem;line-height:1;margin-right:4px;font-variant-numeric:tabular-nums}
.ci a{text-underline-offset:4px}
.lh{margin-top:24px}
.lh p{font-size:14px;color:var(--ink);margin-top:10px}
.lh ul{list-style:none;padding:0;margin:0;display:grid;grid-template-columns:repeat(4,1fr);gap:8px}
.lh li{background:var(--ink3);color:var(--bg);padding:8px 10px}
.lh li b{display:block;font-family:var(--display);font-weight:500;font-size:1.75rem;line-height:1;font-variant-numeric:tabular-nums}
.lh li span{font-size:13px}
.lh a{text-underline-offset:4px}
.folder .txt>p{font-size:17px;line-height:1.55;max-width:46ch}
.folder .acts{display:flex;gap:12px;flex-wrap:wrap;margin-top:24px}
.folder .acts .btn{min-height:46px;padding:0 22px;font-size:15px}
.folder .acts .btn.o{background:var(--tone2);color:var(--ink)}
.folder .acts .btn.o:hover{background:var(--ink);color:var(--bg)}
.dev .view.api{background:var(--ink);padding:clamp(20px,3vw,48px)}
.dev .view.api pre{margin:0;font:15px/1.9 ui-monospace,Menlo,monospace;color:var(--bg)}

/* services */
.offer{background:var(--bg);padding:clamp(96px,12vw,200px) var(--pad) clamp(240px,26vw,420px)}
.col{max-width:620px;margin:0 auto;container-type:inline-size}
.giant{font-family:var(--display);font-weight:500;text-transform:uppercase;font-size:28cqw;line-height:.8;letter-spacing:-.02em;margin-bottom:24px;white-space:nowrap}
details.bar{background:var(--tone);margin-bottom:6px}
details.bar summary{list-style:none;display:flex;align-items:center;gap:12px;min-height:60px;padding:6px 18px;cursor:pointer;font-weight:500;font-size:17px;transition:background .2s}
details.bar summary::-webkit-details-marker{display:none}
details.bar summary:hover{background:var(--tone2)}
details.bar summary .p{margin-left:auto;font-weight:400;font-size:15px;white-space:nowrap;font-variant-numeric:tabular-nums}
details.bar summary .pl{width:18px;text-align:center;font-size:18px;line-height:1}
details.bar[open] summary .pl{transform:rotate(45deg)}
details.bar .items{padding:6px 18px 20px}
.items .it{display:flex;justify-content:space-between;gap:20px;margin-top:14px;font-size:16px}
.items .it span:last-child{color:#56303f;text-align:right}
.items .it.ex{margin-top:20px;font-weight:500}
.items .it.ex span:last-child a{color:var(--ink);text-underline-offset:4px}
.items .it.ex span:last-child a:hover{text-decoration-thickness:2px}

/* ticket */
.quote{background:var(--ink);color:var(--ink);padding:clamp(96px,12vw,200px) var(--pad);position:relative}
.ticket{--notch:28px;position:relative;display:grid;grid-template-columns:7fr 3fr;width:min(64vw + 120px,1180px);max-width:100%;margin:0 auto;background:var(--bg)}
.ticket .main{padding:40px 48px 44px}
.ticket .stub{padding:40px 28px 0;display:flex;flex-direction:column;text-align:center;border-left:6px dotted var(--ink)}
.ticket::before,.ticket::after{content:"";position:absolute;left:70%;width:var(--notch);height:var(--notch);background:var(--ink);border-radius:50%;transform:translateX(-50%)}
.ticket::before{top:calc(var(--notch) / -2)}
.ticket::after{bottom:calc(var(--notch) / -2)}
.ticket h2{font-size:clamp(2.25rem,4vw,3.5rem)}
.ticket .sub{margin:12px 0 28px;max-width:44ch}
.ticket fieldset{border:0;padding:0;margin:0 0 26px;min-width:0}
.ticket legend{font-weight:500;margin-bottom:12px;padding:0}
.opts{display:grid;grid-template-columns:1fr 1fr;gap:8px}
.opt{position:relative;display:flex;align-items:center;gap:12px;min-height:52px;padding:8px 16px;background:var(--tone);cursor:pointer;transition:background .2s}
.opt:hover{background:var(--tone2)}
.opt input{position:absolute;opacity:0;inset:0;cursor:pointer}
.opt .dot{flex:none;width:14px;height:14px;border-radius:50%;background:var(--muted)}
.opt input[type=checkbox]+.dot{border-radius:0}
.opt:has(input:checked){background:var(--ink);color:var(--bg)}
.opt:has(input:checked) .dot{background:var(--bg)}
.opt:has(input:focus-visible){outline:2px solid var(--ink);outline-offset:3px}
.opt small{margin-left:auto;font-variant-numeric:tabular-nums;font-size:15px}
.stub .price small{font-family:var(--text);font-weight:400;font-size:1rem;letter-spacing:0;margin-right:10px}
.stub .price{font-family:var(--display);font-weight:500;font-size:clamp(2.75rem,6vw,5.5rem);line-height:1;letter-spacing:-.03em;font-variant-numeric:tabular-nums}
.stub .cur{font-size:1.25rem;margin-top:6px}
.fb{font-size:14px;margin:12px 0 0;word-break:break-word}
.stub .fb{margin:14px 0 18px;color:var(--muted)}
.coupon .fb{color:var(--bg)}
.stub .note{font-size:15px;margin:22px 0 28px;color:var(--muted)}
.stub .btn{margin:auto -28px 0;min-height:60px;width:calc(100% + 56px);background:var(--ink2)}
.stub .btn:hover{background:var(--ink3)}

/* how */
.how{background:var(--bg);padding:clamp(96px,12vw,200px) var(--pad);display:grid;grid-template-columns:repeat(12,1fr);column-gap:var(--gap)}
.how .hd{grid-column:1/6}
.how h2{font-size:clamp(2.5rem,4.4vw,4.25rem)}
.how .hd p{margin-top:20px;max-width:30ch}
.slip{grid-column:7/12;background:var(--ink);color:var(--bg);padding:40px 36px 44px;clip-path:polygon(0 0,100% 0,100% calc(100% - 18px),95% 100%,90% calc(100% - 18px),85% 100%,80% calc(100% - 18px),75% 100%,70% calc(100% - 18px),65% 100%,60% calc(100% - 18px),55% 100%,50% calc(100% - 18px),45% 100%,40% calc(100% - 18px),35% 100%,30% calc(100% - 18px),25% 100%,20% calc(100% - 18px),15% 100%,10% calc(100% - 18px),5% 100%,0 calc(100% - 18px));font-variant-numeric:tabular-nums}
.slip h3{font-weight:500;font-size:16px;margin-top:28px}
.slip h3:first-child{margin-top:0}
.slip .r{display:flex;align-items:baseline;gap:8px;margin-top:12px;font-size:16px}
.slip .r i{flex:1;border-bottom:4px dotted var(--bg);transform:translateY(-4px);opacity:.7}
.slip .end{margin:36px -36px 0;padding:0 36px;min-height:56px;display:flex;align-items:center;background:var(--bg);color:var(--ink);font-weight:500}

.rules{background:var(--tone);color:var(--ink);padding:clamp(96px,12vw,200px) var(--pad)}
.rules h2{font-size:clamp(2.5rem,4.4vw,4.25rem);margin-bottom:56px}
.rules dl{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,2fr);gap:28px var(--m);max-width:1100px}
.rules dt{font-weight:500;font-size:1.25rem}
.rules dd{margin:0;max-width:60ch}
.cta{margin-top:40px;font-size:1.0625rem;max-width:46ch}
.cta a{text-underline-offset:4px}
.tel{margin-top:20px;font-size:1.25rem}
/* faq */
.faq{background:var(--ink);color:var(--ink);padding:clamp(96px,12vw,200px) var(--pad);overflow-x:clip}
.faq h2{color:var(--bg);font-size:clamp(2.5rem,4vw,4rem);max-width:1100px;margin:0 auto 72px}
.cards{max-width:1100px;margin:0 auto}
.cards details{--i:0;position:relative;background:var(--bg);margin-top:56px}
.cards details:nth-child(3n+2){background:var(--tone)}
.cards details:nth-child(3n){background:var(--tone2)}
.cards details::before{content:attr(data-tab);position:absolute;left:calc(var(--i) * 150px);top:-40px;height:40px;width:200px;display:flex;align-items:center;padding:0 0 0 22px;font-size:16px;background:inherit;clip-path:polygon(0 100%,0 12px,12px 0,calc(100% - 20px) 0,100% 100%)}
.cards summary{list-style:none;cursor:pointer;padding:26px 28px;font-size:20px;font-weight:500;display:flex;justify-content:space-between;gap:16px}
.cards summary::-webkit-details-marker{display:none}
.cards summary::after{content:"+";font-size:24px;line-height:1}
.cards details[open] summary::after{content:"–"}
.cards details p{padding:0 28px 28px;max-width:56ch;font-size:17px}

/* contact */
.contact{background:var(--bg);padding:clamp(96px,12vw,200px) var(--pad)}
.coupon{--notch:28px;position:relative;display:grid;grid-template-columns:46fr 54fr;max-width:1180px;margin:0 auto;background:var(--ink);color:var(--bg)}
.coupon::before,.coupon::after{content:"";position:absolute;left:46%;width:var(--notch);height:var(--notch);background:var(--bg);border-radius:50%;transform:translateX(-50%)}
.coupon::before{top:calc(var(--notch) / -2)}
.coupon::after{bottom:calc(var(--notch) / -2)}
.coupon .l{padding:48px;display:flex;flex-direction:column;justify-content:space-between;gap:32px}
.coupon h2{font-size:clamp(1.75rem,3vw,2.75rem);line-height:1}
.coupon .l p{font-size:16px;max-width:34ch}
.coupon form{padding:48px;border-left:5px dotted var(--bg);display:grid;gap:10px}
.coupon input,.coupon textarea{width:100%;min-height:52px;padding:14px 16px;background:var(--ink2);border:0;border-radius:0;color:var(--bg)}
.coupon textarea{min-height:120px;resize:vertical}
.coupon ::placeholder{color:#d9bfb4;opacity:1}
.coupon .btn{background:var(--ink3);min-height:56px;width:100%;border:0}
.coupon .btn:hover{background:var(--bg);color:var(--ink)}
.sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}

/* footer */
.foot{background:var(--ink);padding:120px var(--pad) 0}
.back{position:relative;max-width:1200px;margin:0 auto;background:var(--bg);padding:56px 56px 24px;min-height:420px;display:grid;grid-template-columns:1fr 1fr;gap:48px}
.back::before{content:"";position:absolute;left:0;right:0;top:-49px;height:50px;background:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='100' height='50' viewBox='0 0 100 50'%3E%3Ccircle cx='50' cy='50' r='50' fill='%23edccbe'/%3E%3C/svg%3E") repeat-x}
.back h2{font-size:32px;line-height:1.05}
.back .msg{margin-top:16px;font-size:16px;max-width:38ch}
.back address{font-style:normal;display:grid;gap:12px;align-content:start;font-size:18px}
.back address a{text-decoration:none}
.back address a:hover{text-decoration:underline;text-underline-offset:5px}
.back .stamp{position:absolute;right:56px;top:56px;width:88px;aspect-ratio:3/4;padding:6px;background:var(--bg)}
.back .stamp img{width:100%;height:100%;object-fit:cover;background:var(--ink)}
.back .imp{grid-column:1/-1;align-self:end;text-align:center;font-size:13px;color:var(--muted)}
.back .imp a{color:inherit}

/* motion */
@media (prefers-reduced-motion:no-preference){
  .js .card>*:not(.stripe):not(.me){opacity:0;animation:rise 900ms var(--ease) forwards}
  .js .card .mark,.js .card h1{opacity:1;animation:lift 900ms var(--ease) both}
  .js .card .lead{animation-delay:370ms}.js .card .btn{animation-delay:480ms}.js .card .links{animation-delay:600ms}
  @keyframes lift{from{transform:translateY(24px)}to{transform:none}}
  @keyframes rise{from{opacity:0;transform:translateY(24px)}to{opacity:1;transform:none}}
  .slide{animation:xfade 28s infinite}
  .slide:nth-child(1){animation-name:xfade0}.slide:nth-child(2){animation-delay:7s}.slide:nth-child(3){animation-delay:14s}.slide:nth-child(4){animation-delay:21s}
  @keyframes xfade0{0%{opacity:1}25%{opacity:1}31%{opacity:0}100%{opacity:0}}
  @keyframes xfade{0%{opacity:0;transform:translateY(16px)}6%{opacity:1;transform:none}25%{opacity:1}31%{opacity:0}100%{opacity:0}}
  .js [data-reveal]{opacity:0;transform:translateY(24px);transition:opacity 700ms var(--ease),transform 900ms var(--ease);transition-delay:calc(var(--d,0) * 70ms)}
  .js [data-reveal].is-in{opacity:1;transform:none}
}

@media (max-height:820px){.folder{position:relative;top:auto}}
@media (max-width:760px){.rules dl{grid-template-columns:1fr;gap:6px}.rules dd{margin-bottom:22px}}
@media (max-width:900px){
  .hero{grid-template-columns:1fr;display:flex;flex-direction:column}
  .photo{order:1;position:relative;top:0;height:48svh}
  .slide figcaption{display:none}
  .card{min-height:0;position:relative;z-index:1}
  .me{position:static;transform:rotate(-2deg);margin-top:32px;width:104px}
  .card .mark{font-size:20vw;margin-top:20px}
  .card h1{font-size:8vw}
  .card .links{margin-top:32px}
  .stripe{height:40px}
  .work header{flex-direction:column;gap:8px}
  .folder{position:relative;top:auto;min-height:0;display:block;padding:40px 20px 28px;margin-top:48px}
  .tabs{left:20px;top:-40px}.tab{height:40px;padding:0 26px 0 18px}.tab.n{font-size:20px}.tab.s{display:none}
  .folder .kind{position:static;display:block;height:auto;padding:0;background:none;color:inherit;margin-bottom:16px}
  .dev .tg button{min-height:32px}
  .dev .view{aspect-ratio:3/4}
  .folder .txt{padding-top:20px}
  .lh ul{grid-template-columns:repeat(2,1fr)}
  .ticket{display:block;width:100%}
  .ticket .main{padding:32px 20px}
  .ticket .stub{border-left:0;border-top:6px dotted var(--ink);padding:32px 20px 0}
  .ticket::before,.ticket::after{display:none}
  .opts{grid-template-columns:1fr}
  .stub .btn{margin:24px -20px 0;width:calc(100% + 40px)}
  .how{display:block}
  .slip{margin-top:40px}
  .cards details::before{width:130px;left:calc(var(--i) * 48px)}
  .coupon{display:block}
  .coupon::before,.coupon::after{display:none}
  .coupon .l{padding:32px 20px}
  .coupon form{border-left:0;border-top:5px dotted var(--bg);padding:32px 20px}
  .back{display:block;padding:40px 24px 24px}
  .back address{margin-top:32px}
  .back .stamp{display:none}
  .back .imp{margin-top:32px}
}
"""

JS = r"""
const $=s=>document.querySelector(s);
const els=document.querySelectorAll('[data-reveal]');
if('IntersectionObserver' in window){const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('is-in');io.unobserve(e.target)}}),{threshold:.1});els.forEach(e=>io.observe(e))}else els.forEach(e=>e.classList.add('is-in'));
const T=JSON.parse(document.getElementById('i18n').textContent);
const fmt=n=>n.toString().replace(/\B(?=(\d{3})+(?!\d))/g,' ');
const svcBox=$('#svc'),extraBox=$('#extras'),priceEl=$('#price'),sendEl=$('#send');
function renderQuote(){
  const sid=(document.querySelector('input[name=svc]:checked')||{}).value;
  const svc=T.services.find(s=>s.id===sid)||T.services[0];
  if(extraBox.dataset.for!==svc.id){
    extraBox.dataset.for=svc.id;
    extraBox.innerHTML=svc.extras.map((x,i)=>`<label class="opt"><input type="checkbox" value="${i}"><span class="dot"></span><span>${x[0]}</span><small>+${fmt(x[1])}</small></label>`).join('');
    extraBox.querySelectorAll('input').forEach(i=>i.addEventListener('change',renderQuote));
  }
  const picked=[...extraBox.querySelectorAll('input:checked')].map(i=>svc.extras[+i.value]);
  const total=svc.base+picked.reduce((a,x)=>a+x[1],0);
  priceEl.textContent=fmt(total);
  const body=T.intro+svc.label+T.extrasLabel+(picked.length?picked.map(x=>x[0]).join(', '):T.none)+T.priceLabel+fmt(total)+' '+T.cur+T.outro;
  sendEl.href='mailto:'+T.mail+'?subject='+encodeURIComponent(T.subject)+'&body='+encodeURIComponent(body);
}
svcBox.querySelectorAll('input').forEach(i=>i.addEventListener('change',renderQuote));
renderQuote();
const W={d:[1280,800],p:[390,800]};
function fit(dev){
  const v=dev.querySelector('.view'),f=dev.querySelector('iframe');if(!f)return;
  const mode=dev.dataset.mode||'d',[w,h]=W[mode],vw=v.clientWidth,vh=v.clientHeight;
  const s=mode==='d'?vw/w:vh/h;
  f.style.width=w+'px';f.style.height=h+'px';f.style.transform='scale('+s+')';
  f.style.left=mode==='d'?'0':Math.max(0,(vw-w*s)/2)+'px';
}
const devs=document.querySelectorAll('.dev[data-src]');
const ro='ResizeObserver' in window?new ResizeObserver(es=>es.forEach(e=>fit(e.target.closest('.dev')))):null;
const lo='IntersectionObserver' in window?new IntersectionObserver(es=>es.forEach(e=>{if(!e.isIntersecting)return;const d=e.target,f=d.querySelector('iframe');lo.unobserve(d);f.addEventListener('load',()=>d.classList.add('loaded'));f.src=d.dataset.src;fit(d)}),{rootMargin:'600px 0px'}):null;
devs.forEach(d=>{
  if(innerWidth<900){d.dataset.mode='p';d.querySelectorAll('.tg button').forEach(x=>x.classList.toggle('on',x.dataset.mode==='p'))}
  if(ro)ro.observe(d.querySelector('.view'));if(lo)lo.observe(d);
  d.querySelectorAll('.tg button').forEach(bt=>bt.addEventListener('click',()=>{d.dataset.mode=bt.dataset.mode;d.querySelectorAll('.tg button').forEach(x=>x.classList.toggle('on',x===bt));fit(d)}));
  const v=d.querySelector('.view');v.addEventListener('click',()=>v.classList.add('act'));v.addEventListener('mouseleave',()=>v.classList.remove('act'));
});
const form=$('#contactForm');
form.addEventListener('submit',e=>{
  e.preventDefault();
  const f=new FormData(form);
  const body=T.fbody.replace('{name}',f.get('name')||'').replace('{mail}',f.get('mail')||'').replace('{msg}',f.get('msg')||'');
  location.href='mailto:'+T.mail+'?subject='+encodeURIComponent(T.fsubject)+'&body='+encodeURIComponent(body);
});
"""

def esc(s): return html.escape(s, quote=True)

def lh_scores(slug):
    return json.load(open(os.path.join(HERE, "lh.json"))).get(slug)


def pid(w): return w["code"].rsplit("/", 1)[-1].lower()


def page(T, prefix):
    year = "2026"
    url = SITE + T["path"]
    other = SITE + T["other_path"]
    stripe = "".join("<i></i>" for _ in range(60))
    shots = [w for w in T["wk"] if w["img"]][:4]
    lazy = ' loading="lazy"'
    order = ["Northside Bikes", "Sukcyna", "Apartament Gąski", "Book scraper"]
    shots = [w for n in order for w in T["wk"] if w["name"] == n]
    photo = "".join('<figure class="slide"><div class="frm"><div class="bar"><span class="url">%s</span></div><img src="%s%s" alt="" width="1280" height="800"%s></div><figcaption>%s · %s</figcaption></figure>' % (esc(w["live"].replace("https://", "")), prefix, w["img"], "" if i == 0 else lazy, esc(w["name"]), esc(w["kind"])) for i, w in enumerate(shots))
    folders = ""
    for n, w in enumerate(T["wk"]):
        bar_url = w["live"].replace("https://", "") if w["live"] else w.get("term", "GitHub")
        if w["live"]:
            tog = f'<span class="tg"><button type="button" class="on" data-mode="d">{T["preview_desktop"]}</button><button type="button" data-mode="p">{T["preview_phone"]}</button></span>'
            vis = f'''<div class="dev" data-src="{w["live"]}" data-reveal>
<div class="bar"><span class="url">{esc(bar_url)}</span>{tog}</div>
<div class="view" data-hint="{esc(T["preview_hint"])}"><img class="poster" src="{prefix}{w["img"]}" alt="{esc(w["alt"])}" width="1280" height="800" loading="lazy"><iframe title="{esc(w["name"])}" loading="lazy" tabindex="-1"></iframe></div>
</div>'''
        elif w["img"]:
            vis = f'''<div class="dev" data-reveal>
<div class="bar"><span class="url">{esc(bar_url)}</span></div>
<div class="view"><img class="poster" src="{prefix}{w["img"]}" alt="{esc(w["alt"])}" width="1280" height="800" loading="lazy"></div>
</div>'''
        else:
            vis = '''<div class="dev" data-ui data-reveal>
<div class="bar"><span class="url">api · Express + MongoDB</span></div>
<div class="view api"><pre><code>POST   /api/auth/register\nPOST   /api/auth/login\nGET    /api/tasks\nPATCH  /api/tasks/:id\nGET    /api/notes\nGET    /api/stats/summary</code></pre></div>
</div>'''
        sc = lh_scores(w["lh"]) if w.get("lh") else None
        lh = ""
        if sc:
            cells = "".join(f'<li><b>{v}</b><span>{esc(c)}</span></li>' for v, c in zip(sc, T["lh_cats"]))
            lh = f'''<div class="lh"><ul>{cells}</ul><p>{T["lh_label"]}. <a href="https://pagespeed.web.dev/analysis?url={w["live"]}&form_factor=mobile">{T["lh_check"]}</a></p></div>'''
        tests = f'<p class="ci"><b>{w["tests"]}</b> {esc(T["tests_l"])}. <a href="{w["code"]}/actions/workflows/test.yml">{T["tests_check"]}</a></p>' if w.get("tests") else ""
        quote = f'<blockquote class="q"><p>„{esc(w["quote"])}”</p><footer>{esc(w["quote_by"])}</footer></blockquote>' if w.get("quote") else ""
        acts = ""
        if w["live"]:
            acts += f'<a class="btn" href="{w["live"]}">{T["live"]}</a>'
        acts += f'<a class="btn {"o" if w["live"] else ""}" href="{w["code"]}">{T["code"]}</a>'
        folders += f'''<article class="folder" id="{pid(w)}" style="--n:{n}">
<div class="tabs"><span class="tab n">{esc(w["name"])}</span><span class="tab s">{esc(w["tab2"])}</span></div>
<span class="kind">{esc(w["kind"])}</span>
{vis}
<div class="txt" data-reveal style="--d:2"><p>{esc(w["text"])}</p>{quote}{tests}{lh}<div class="acts">{acts}</div></div>
</article>'''
    bars = ""
    svc = T["svc"][:3] + [T["svc"][4], T["svc"][3]]
    for i, s in enumerate(svc):
        items = "".join(f'<div class="it"><span>{esc(a)}</span><span>{esc(b)}</span></div>' for a, b in s["items"])
        names = {w["name"]: w for w in T["wk"]}
        links = ", ".join(f'<a href="#{pid(names[x])}">{esc(x)}</a>' for x in s.get("ex", []))
        if links:
            items += f'<div class="it ex"><span>{esc(T["ex_label"])}</span><span>{links}</span></div>'
        bars += f'<details class="bar"{" open" if i==0 else ""} data-reveal style="--d:{i}"><summary><span>{esc(s["t"])}</span><span class="p">{esc(s["p"])}</span><span class="pl" aria-hidden="true">+</span></summary><div class="items">{items}</div></details>'
    svc_opts = "".join(f'<label class="opt"><input type="radio" name="svc" value="{s["id"]}"{" checked" if i==0 else ""}><span class="dot"></span><span>{esc(s["label"])}</span></label>' for i, s in enumerate(T["q_services"]))
    how = ""
    for head, rows in T["how"]:
        how += f"<h3>{esc(head)}</h3>" + "".join(f'<div class="r"><span>{esc(a)}</span><i></i><span>{esc(b)}</span></div>' for a, b in rows)
    rules_html = "".join(f"<dt>{esc(a)}</dt><dd>{esc(c)}</dd>" for a, c in T["rules"])
    faq = "".join(f'<details data-tab="{esc(tab)}" style="--i:{i % 5}"{" open" if i==0 else ""} data-reveal><summary>{esc(q)}</summary><p>{esc(a)}</p></details>' for i, (tab, q, a) in enumerate(T["faq"]))
    i18n = dict(
        services=[dict(id=s["id"], label=s["label"], base=s["base"], extras=s["extras"]) for s in T["q_services"]],
        mail=MAIL, subject=T["q_subject"], intro=T["q_body_intro"], extrasLabel=T["q_body_extras"], none=T["q_body_none"],
        priceLabel=T["q_body_price"], cur=T["q_cur"], outro=T["q_body_outro"], fsubject=T["f_subject"], fbody=T["f_body"])
    ld = {
        "@context": "https://schema.org", "@type": "ProfessionalService", "name": T["jsonld_name"],
        "url": SITE, "email": MAIL, "founder": {"@type": "Person", "name": T["full_name"], "image": SITE + "img/marcin.webp"}, "description": T["jsonld_desc"], "areaServed": "PL", "priceRange": "od 150 zł",
        "knowsAbout": ["web development", "web scraping", "automation"], "inLanguage": [T["lang"]],
        "makesOffer": [{"@type": "Offer", "itemOffered": {"@type": "Service", "name": s["label"]}, "priceSpecification": {"@type": "PriceSpecification", "price": s["base"], "priceCurrency": "PLN", "minPrice": s["base"]}} for s in T["q_services"]],
    }
    og = SITE + "img/og.jpg"
    return f'''<!DOCTYPE html>
<html lang="{T["lang"]}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(T["title"])}</title>
<meta name="description" content="{esc(T["desc"])}">
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="pl" href="{SITE}">
<link rel="alternate" hreflang="en" href="{SITE}en/">
<link rel="alternate" hreflang="x-default" href="{SITE}">
<meta property="og:type" content="website">
<meta property="og:locale" content="{T["ogloc"]}">
<meta property="og:title" content="{esc(T["title"])}">
<meta property="og:description" content="{esc(T["desc"])}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{og}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#351a2b">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' fill='%23351a2b'/%3E%3Ctext x='16' y='24' font-size='22' font-family='Georgia,serif' text-anchor='middle' fill='%23edccbe'%3EM%3C/text%3E%3C/svg%3E">
<script>document.documentElement.classList.add('js')</script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bodoni+Moda:ital,opsz,wght@0,6..96,500&family=Jost:wght@400;500&display=swap" rel="stylesheet" media="print" onload="this.media='all'">
<noscript><link href="https://fonts.googleapis.com/css2?family=Bodoni+Moda:ital,opsz,wght@0,6..96,500&family=Jost:wght@400;500&display=swap" rel="stylesheet"></noscript>
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
<style>{CSS}</style>
</head>
<body>
<a class="skip" href="#main">{T["skip"]}</a>
<header class="hero">
  <div class="card">
    <div class="stripe" aria-hidden="true">{stripe}</div>
    <figure class="me"><img src="{prefix}img/marcin.webp" alt="{esc(T["full_name"])}" width="240" height="300"></figure>
    <p class="mark display">Marcin</p>
    <h1 class="display">{esc(T["h1a"])}<br>{esc(T["h1b"])}</h1>
    <p class="lead">{esc(T["lead"])}</p>
    <a class="btn" href="#wycena">{esc(T["cta"])}</a>
    <nav class="links" aria-label="{T["nav_aria"]}">
      <a href="#prace">{T["nav_work"]}</a><a href="#jak">{T["nav_how"]}</a><a href="#pytania">{T["nav_faq"]}</a><a href="{other}" hreflang="{"en" if T["lang"]=="pl" else "pl"}" lang="{"en" if T["lang"]=="pl" else "pl"}" aria-label="{T["other_label"]}, {esc(T["other_name"])}">{T["other_label"]}</a>
    </nav>
  </div>
  <div class="photo" aria-hidden="true">{photo}</div>
</header>
<main id="main">
<section class="work" id="prace" aria-labelledby="h-work">
  <header><h2 class="display" id="h-work">{T["work_h"]}</h2><p>{T["work_note"]}</p></header>
  {folders}
</section>
<section class="offer" aria-label="{T["offer_aria"]}">
  <div class="col"><h2 class="giant" data-reveal style="font-size:{min(28, round(160 / len(T["offer_h"]), 1))}cqw">{T["offer_h"]}</h2>{bars}<p class="cta" data-reveal>{T["offer_cta"]} <a href="#kontakt">{T["offer_cta_link"]}</a></p></div>
</section>
<section class="quote" id="wycena" aria-labelledby="h-quote">
  <div class="ticket" data-reveal>
    <div class="main">
      <h2 class="display" id="h-quote">{T["quote_h"]}</h2>
      <p class="sub">{T["quote_sub"]}</p>
      <fieldset id="svc"><legend>{T["q_what"]}</legend><div class="opts">{svc_opts}</div></fieldset>
      <fieldset><legend>{T["q_extras"]}</legend><div class="opts" id="extras"></div></fieldset>
    </div>
    <div class="stub">
      <p class="price" aria-live="polite"><small>{T["q_from"]}</small><span id="price">990</span></p>
      <p class="cur">{T["q_cur"]}</p>
      <p class="note">{T["q_note"]}</p>
      <a class="btn" id="send" href="mailto:{MAIL}">{T["q_send"]}</a>
      <p class="fb">{T["fallback"]} <a href="mailto:{MAIL}">{MAIL}</a></p>
    </div>
  </div>
</section>
<section class="how" id="jak" aria-labelledby="h-how">
  <div class="hd" data-reveal><h2 class="display" id="h-how">{T["how_h"]}</h2><p>{T["how_p"]}</p></div>
  <div class="slip" data-reveal style="--d:2">{how}<div class="end">{T["how_end"]}</div></div>
</section>
<section class="rules" id="zasady" aria-labelledby="h-rules">
  <h2 class="display" id="h-rules" data-reveal>{T["rules_h"]}</h2>
  <dl data-reveal style="--d:1">{rules_html}</dl>
</section>
<section class="faq" id="pytania" aria-labelledby="h-faq">
  <h2 class="display" id="h-faq">{T["faq_h"]}</h2>
  <div class="cards">{faq}</div>
</section>
<section class="contact" id="kontakt" aria-labelledby="h-contact">
  <div class="coupon" data-reveal>
    <div class="l"><h2 class="display" id="h-contact">{T["contact_h"]}</h2><p>{T["contact_p"]}</p><p class="tel">{T["call_note"]}</p></div>
    <form id="contactForm">
      <label class="sr" for="f1">{T["f_name"]}</label><input id="f1" name="name" placeholder="{T["f_name"]}" autocomplete="name" required>
      <label class="sr" for="f2">{T["f_mail"]}</label><input id="f2" name="mail" type="email" placeholder="{T["f_mail"]}" autocomplete="email" required>
      <label class="sr" for="f3">{T["f_msg"]}</label><textarea id="f3" name="msg" placeholder="{T["f_msg"]}" required></textarea>
      <button class="btn" type="submit">{T["f_send"]}</button>
      <p class="fb">{T["fallback"]} <a href="mailto:{MAIL}">{MAIL}</a></p>
    </form>
  </div>
</section>
</main>
<footer class="foot">
  <div class="back">
    <div class="stamp" aria-hidden="true"><img src="{prefix}img/marcin.webp" alt="" width="240" height="300" loading="lazy"></div>
    <div><h2 class="display">{T["foot_h"]}</h2><p class="msg">{T["foot_p"]}</p></div>
    <address><a href="mailto:{MAIL}">{MAIL}</a><a href="https://github.com/Marven151">{T["foot_gh"]}</a></address>
    <p class="imp">{T["foot_imprint"].format(year=year)} · <a href="{SITE}informacja/">{T["info_link"]}</a></p>
  </div>
</footer>
<script type="application/json" id="i18n">{json.dumps(i18n, ensure_ascii=False)}</script>
<script>{JS}</script>
</body>
</html>'''

out = os.path.dirname(HERE)
os.makedirs(out + "/en", exist_ok=True)
open(out + "/index.html", "w", encoding="utf-8").write(page(PL, ""))
open(out + "/en/index.html", "w", encoding="utf-8").write(page(EN, "../"))
os.makedirs(out + "/informacja", exist_ok=True)
open(out + "/informacja/index.html", "w", encoding="utf-8").write(open(os.path.join(HERE, "info_page.html"), encoding="utf-8").read())
open(out + "/robots.txt", "w").write(f"User-agent: *\nAllow: /\nSitemap: {SITE}sitemap.xml\n")
open(out + "/sitemap.xml", "w").write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n<url><loc>{SITE}</loc></url>\n<url><loc>{SITE}en/</loc></url>\n<url><loc>{SITE}informacja/</loc></url>\n</urlset>\n')
print("built")
