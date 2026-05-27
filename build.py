import base64

with open('assets/collage_b64.txt') as f:
    COLLAGE_B64 = f.read().strip()

# Convert INFOGRAF logo header PNG to base64 for header display
with open('assets/infograf-logo-header.png','rb') as f:
    LOGO_B64 = base64.b64encode(f.read()).decode('ascii')

HTML = r'''<!DOCTYPE html>
<html lang="sr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>INFOGRAF GOTI – Email Signature Generator</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Source+Sans+3:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
  :root{
    --text:#303030;
    --muted:#6B7280;
    --accent:#EA976E;
    --bg:#F7F8FA;
    --card:#FFFFFF;
    --border:#E5E7EB;
    --black:#0F172A;
  }
  *{box-sizing:border-box}
  html,body{margin:0;padding:0}
  body{
    font-family:'Source Sans 3','Source Sans Pro',-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,sans-serif;
    background:var(--bg);
    color:var(--text);
    line-height:1.5;
    min-height:100vh;
  }
  header{
    background:#fff;
    padding:24px 32px;
    display:flex;
    align-items:center;
    gap:24px;
    border-bottom:2px solid var(--accent);
  }
  header .brand{display:flex;align-items:center}
  header .brand img{height:42px;width:auto;display:block}
  header h1{margin:0;font-size:20px;font-weight:700;letter-spacing:.2px;color:var(--text);line-height:1.2}
  header h1 small{display:block;font-weight:400;font-size:13px;opacity:.7;margin-top:4px;color:var(--muted)}
  main{
    max-width:1320px;
    margin:0 auto;
    padding:32px;
    display:grid;
    grid-template-columns:380px 1fr;
    gap:28px;
  }
  @media (max-width:980px){
    main{grid-template-columns:1fr;padding:20px}
  }
  .card{
    background:var(--card);
    border:1px solid var(--border);
    border-radius:12px;
    padding:24px;
    box-shadow:0 1px 2px rgba(15,23,42,.04);
  }
  .card h2{
    margin:0 0 4px;
    font-size:15px;
    font-weight:700;
    color:var(--text);
    text-transform:uppercase;
    letter-spacing:.5px;
  }
  .card .sub{font-size:13px;color:var(--muted);margin-bottom:20px}
  .field{margin-bottom:16px}
  .field label{
    display:block;
    font-size:13px;
    font-weight:600;
    color:var(--text);
    margin-bottom:6px;
  }
  .field input{
    width:100%;
    border:1px solid var(--border);
    border-radius:8px;
    padding:10px 12px;
    font-size:15px;
    font-family:inherit;
    color:var(--text);
    background:#fff;
    transition:border-color .15s,box-shadow .15s;
  }
  .field input:focus{
    outline:none;
    border-color:var(--accent);
    box-shadow:0 0 0 3px rgba(234,151,110,.18);
  }
  .field input:invalid:not(:placeholder-shown){border-color:#dc2626}
  .hint{font-size:12px;color:var(--muted);margin-top:4px}
  .actions{display:flex;gap:10px;margin-top:20px;flex-wrap:wrap}
  button{
    font-family:inherit;font-size:14px;font-weight:600;
    padding:11px 18px;border-radius:8px;border:none;cursor:pointer;
    transition:transform .05s,background .15s,box-shadow .15s;
  }
  button:active{transform:translateY(1px)}
  .btn-primary{background:var(--text);color:#fff;flex:1;min-width:140px}
  .btn-primary:hover{background:#000}
  .btn-secondary{background:#fff;color:var(--text);border:1.5px solid var(--text)}
  .btn-secondary:hover{background:#F1F5F9}
  .status{margin-top:14px;font-size:13px;min-height:18px;color:var(--muted);transition:color .15s}
  .status.ok{color:#059669;font-weight:600}
  .status.err{color:#dc2626;font-weight:600}

  .preview-wrap{display:flex;flex-direction:column;gap:20px}
  .preview-frame{background:#fff;border:1px solid var(--border);border-radius:12px;padding:32px;overflow:auto}
  .preview-label{display:flex;justify-content:space-between;align-items:center;margin-bottom:12px}
  .preview-label h2{margin:0;font-size:15px;font-weight:700;color:var(--text);text-transform:uppercase;letter-spacing:.5px}
  .preview-label .tag{
    font-size:11px;padding:4px 8px;background:rgba(234,151,110,.15);
    color:var(--accent);border-radius:999px;font-weight:700;letter-spacing:.3px;
  }
  .instructions{background:#fff;border:1px solid var(--border);border-radius:12px;padding:24px}
  .instructions h2{margin:0 0 12px;font-size:15px;font-weight:700;color:var(--text);text-transform:uppercase;letter-spacing:.5px}
  .instructions ol{margin:0;padding-left:20px;color:var(--text);font-size:14px}
  .instructions ol li{margin-bottom:8px}
  .instructions ol li b{color:var(--text)}
  .instructions code{background:#F1F5F9;padding:2px 6px;border-radius:4px;font-size:13px;color:var(--text)}
  footer{text-align:center;padding:24px;font-size:12px;color:var(--muted);line-height:1.8}
  footer a{color:var(--text);text-decoration:none}
  footer a:hover{text-decoration:underline}
  footer .credit{display:block;margin-top:4px;font-size:11px;opacity:.75;letter-spacing:.3px}
  footer .credit a{color:var(--muted);font-weight:600}
  footer .credit a:hover{color:var(--accent)}
</style>
</head>
<body>

<header>
  <div class="brand"><img src="data:image/png;base64,__LOGO_B64__" alt="INFOGRAF GOTI"></div>
  <h1>
    Email Signature Generator
    <small>INFOGRAF GOTI · computers &amp; networking</small>
  </h1>
</header>

<main>
  <!-- LEFT: FORM -->
  <section class="card" aria-label="Forma za unos">
    <h2>Vaši podaci</h2>
    <p class="sub">Popunite polja. Pregled se ažurira u realnom vremenu.</p>

    <div class="field">
      <label for="name">Ime i prezime</label>
      <input id="name" type="text" placeholder="npr. TEODORA SREDOJEVIĆ" autocomplete="name" required>
      <div class="hint">Velikim slovima, kao na dizajnu</div>
    </div>

    <div class="field">
      <label for="position">Pozicija</label>
      <input id="position" type="text" placeholder="npr. Head of creative department" autocomplete="organization-title" required>
    </div>

    <div class="field">
      <label for="mobile">Mobilni telefon</label>
      <input id="mobile" type="text" placeholder="+381/ 63 47 80 26" autocomplete="tel" required>
    </div>

    <div class="field">
      <label for="email">Email</label>
      <input id="email" type="email" placeholder="ime.prezime@info-graf.rs" autocomplete="email" required>
    </div>

    <div class="actions">
      <button class="btn-primary" id="copyBtn" type="button">Kopiraj potpis</button>
      <button class="btn-secondary" id="resetBtn" type="button">Reset</button>
    </div>
    <div class="status" id="status" role="status" aria-live="polite"></div>
  </section>

  <!-- RIGHT: PREVIEW + INSTRUCTIONS -->
  <section class="preview-wrap">
    <div>
      <div class="preview-label">
        <h2>Pregled potpisa</h2>
        <span class="tag">LIVE</span>
      </div>
      <div class="preview-frame" id="previewFrame"></div>
    </div>

    <div class="instructions">
      <h2>Kako se ubacuje u Outlook</h2>
      <ol>
        <li>Popunite podatke i kliknite <b>„Kopiraj potpis"</b>.</li>
        <li>Outlook: <code>File → Options → Mail → Signatures…</code></li>
        <li>Kliknite <b>„New"</b>, dajte ime potpisu (npr. „INFOGRAF").</li>
        <li>U editor kliknite i pritisnite <code>Ctrl + V</code> (Mac: <code>Cmd + V</code>).</li>
        <li>Save. Po želji postavite kao default za nove mejlove i odgovore.</li>
      </ol>
    </div>
  </section>
</main>

<footer>
  © INFOGRAF GOTI · <a href="https://www.info-graf.rs" target="_blank" rel="noopener">www.info-graf.rs</a>
  <span class="credit">Created by <a href="https://studio53.rs" target="_blank" rel="noopener">Studio 53</a></span>
</footer>

<script>
(function(){
  // ===== Firmenstammdaten (FIX) =====
  var COMPANY = {
    officeTel:  '+381/ 21 551-311',
    website:    'www.info-graf.rs',
    websiteUrl: 'https://www.info-graf.rs',
    address:    'Joakima Vujića 16, 21000 Novi Sad, Serbia'
  };

  var DEFAULTS = {
    name:     'TEODORA SREDOJEVIĆ',
    position: 'Head of creative department',
    mobile:   '+381/ 63 47 80 26',
    email:    'teodora.sredojevic@info-graf.rs'
  };

  var COLLAGE = 'data:image/jpeg;base64,__COLLAGE_B64__';

  var STORAGE_KEY = 'infograf_signature_v1';
  var $ = function(id){ return document.getElementById(id); };
  var fields = ['name','position','mobile','email'];

  function load(){
    var saved = {};
    try{ saved = JSON.parse(localStorage.getItem(STORAGE_KEY) || '{}'); }catch(e){}
    fields.forEach(function(k){
      $(k).value = (saved[k] && saved[k] !== '') ? saved[k] : DEFAULTS[k];
    });
  }
  function save(){
    var d = {}; fields.forEach(function(k){ d[k] = $(k).value; });
    try{ localStorage.setItem(STORAGE_KEY, JSON.stringify(d)); }catch(e){}
  }
  function esc(s){
    return String(s == null ? '' : s)
      .replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;')
      .replace(/"/g,'&quot;').replace(/'/g,'&#39;');
  }

  // Inline SVG icons (small, work in modern email clients)
  var ICON_MAIL = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#303030" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align:middle;display:inline-block;"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/></svg>';
  var ICON_PHONE = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#303030" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align:middle;display:inline-block;"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.12.96.34 1.9.66 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.91.32 1.85.54 2.81.66A2 2 0 0 1 22 16.92z"/></svg>';
  var ICON_GLOBE = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#303030" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align:middle;display:inline-block;"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>';
  var ICON_PIN  = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#303030" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align:middle;display:inline-block;"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>';

  function buildSignatureHTML(d){
    var fontStack = "'Source Sans 3','Source Sans Pro',Calibri,Arial,sans-serif";
    var TEXT = '#303030', MUTED = '#6B7280', ACCENT = '#EA976E';

    var name     = esc(d.name)     || esc(DEFAULTS.name);
    var position = esc(d.position) || esc(DEFAULTS.position);
    var mobile   = esc(d.mobile)   || esc(DEFAULTS.mobile);
    var email    = esc(d.email)    || esc(DEFAULTS.email);
    var officeTel = esc(COMPANY.officeTel);
    var website   = esc(COMPANY.website);
    var websiteUrl = esc(COMPANY.websiteUrl);
    var address   = esc(COMPANY.address);

    var mobileHref = 'tel:' + mobile.replace(/[^+0-9]/g,'');
    var officeHref = 'tel:' + officeTel.replace(/[^+0-9]/g,'');

    function row(icon, content){
      return '<tr><td style="padding:3px 0;font-family:'+fontStack+';font-size:14px;color:'+TEXT+';line-height:1.5;vertical-align:middle;">' +
        '<span style="display:inline-block;width:20px;vertical-align:middle;">'+icon+'</span>' +
        '<span style="vertical-align:middle;">'+content+'</span>' +
      '</td></tr>';
    }

    return ''+
    '<table cellpadding="0" cellspacing="0" border="0" style="border-collapse:collapse;font-family:'+fontStack+';">' +
      '<tr>' +
        // LEFT: collage image
        '<td style="vertical-align:middle;padding:0 24px 0 0;">' +
          '<img src="'+COLLAGE+'" alt="INFOGRAF Partners" width="250" style="display:block;border:0;outline:none;width:250px;height:auto;">' +
        '</td>' +
        // RIGHT: contact info
        '<td style="vertical-align:middle;padding:0;font-family:'+fontStack+';">' +
          '<table cellpadding="0" cellspacing="0" border="0" style="border-collapse:collapse;font-family:'+fontStack+';">' +
            '<tr><td style="font-family:'+fontStack+';font-size:22px;font-weight:700;color:'+TEXT+';line-height:1.2;padding:0 0 4px 0;letter-spacing:.5px;">'+name+'</td></tr>' +
            '<tr><td style="font-family:'+fontStack+';font-size:14px;font-weight:400;color:'+MUTED+';line-height:1.2;padding:0 0 14px 0;">'+position+'</td></tr>' +
            '<tr><td style="padding:0;">' +
              '<table cellpadding="0" cellspacing="0" border="0" style="border-collapse:collapse;">' +
                row(ICON_MAIL,  '<a href="mailto:'+email+'" style="color:'+TEXT+';text-decoration:none;">'+email+'</a>') +
                row(ICON_PHONE, '<a href="'+mobileHref+'" style="color:'+TEXT+';text-decoration:none;">'+mobile+'</a>') +
                row(ICON_GLOBE, '<a href="'+websiteUrl+'" style="color:'+ACCENT+';text-decoration:none;font-weight:600;">'+website+'</a>') +
                row(ICON_PHONE, '<a href="'+officeHref+'" style="color:'+TEXT+';text-decoration:none;">'+officeTel+'</a>') +
                row(ICON_PIN,   '<span style="color:'+TEXT+';">'+address+'</span>') +
              '</table>' +
            '</td></tr>' +
          '</table>' +
        '</td>' +
      '</tr>' +
    '</table>';
  }

  function buildPlainText(d){
    return [
      d.name || DEFAULTS.name,
      d.position || DEFAULTS.position,
      '',
      (d.email || DEFAULTS.email),
      'Mob: ' + (d.mobile || DEFAULTS.mobile),
      'Web: ' + COMPANY.website,
      'Tel: ' + COMPANY.officeTel,
      COMPANY.address
    ].join('\n');
  }

  function currentData(){
    return {
      name: $('name').value.trim(),
      position: $('position').value.trim(),
      mobile: $('mobile').value.trim(),
      email: $('email').value.trim()
    };
  }
  function render(){
    $('previewFrame').innerHTML = buildSignatureHTML(currentData());
    save();
  }

  function setStatus(msg, type){
    var el = $('status');
    el.textContent = msg || '';
    el.className = 'status' + (type ? (' '+type) : '');
    if(msg){
      clearTimeout(el._t);
      el._t = setTimeout(function(){ el.textContent=''; el.className='status'; }, 4000);
    }
  }
  function validate(d){
    if(!d.name) return 'Unesite ime i prezime.';
    if(!d.position) return 'Unesite poziciju.';
    if(!d.mobile) return 'Unesite mobilni telefon.';
    if(!d.email) return 'Unesite email.';
    if(!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(d.email)) return 'Email nije validan.';
    return null;
  }

  async function copySignature(){
    var d = currentData();
    var err = validate(d);
    if(err){ setStatus(err, 'err'); return; }
    var html = buildSignatureHTML(d);
    var text = buildPlainText(d);
    try{
      if(navigator.clipboard && window.ClipboardItem){
        var item = new ClipboardItem({
          'text/html':  new Blob([html], {type:'text/html'}),
          'text/plain': new Blob([text], {type:'text/plain'})
        });
        await navigator.clipboard.write([item]);
        setStatus('✓ Potpis kopiran. Sada u Outlook-u → Ctrl+V', 'ok');
        return;
      }
    }catch(e){}
    try{
      var div = document.createElement('div');
      div.contentEditable = 'true';
      div.style.position = 'fixed'; div.style.left='-9999px'; div.style.top='0';
      div.innerHTML = html;
      document.body.appendChild(div);
      var range = document.createRange();
      range.selectNodeContents(div);
      var sel = window.getSelection();
      sel.removeAllRanges(); sel.addRange(range);
      var ok = document.execCommand('copy');
      sel.removeAllRanges();
      document.body.removeChild(div);
      if(ok) setStatus('✓ Potpis kopiran. Sada u Outlook-u → Ctrl+V', 'ok');
      else setStatus('Kopiranje nije uspelo. Probajte ručno iz pregleda.', 'err');
    }catch(e2){
      setStatus('Greška: '+e2.message, 'err');
    }
  }
  function resetForm(){
    fields.forEach(function(k){ $(k).value = DEFAULTS[k]; });
    render();
    setStatus('Vraćeno na default vrednosti.', 'ok');
  }

  load(); render();
  fields.forEach(function(k){ $(k).addEventListener('input', render); });
  $('copyBtn').addEventListener('click', copySignature);
  $('resetBtn').addEventListener('click', resetForm);
})();
</script>
</body>
</html>
'''

HTML = HTML.replace('__LOGO_B64__', LOGO_B64).replace('__COLLAGE_B64__', COLLAGE_B64)
with open('index.html','w') as f:
    f.write(HTML)
import os
print('index.html:', os.path.getsize('index.html'), 'bytes')
