const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch(); const pg = await b.newPage();
  await pg.goto('file://' + __dirname + '/algo-aventures.html'); await pg.waitForTimeout(800);
  const of = await pg.evaluate(() => [...document.querySelectorAll('.page')].map((p, i) => { const c = p.querySelector('.content'); return c.scrollHeight > c.clientHeight + 2 ? `p${i + 1}: +${c.scrollHeight - c.clientHeight}px` : null }).filter(Boolean));
  console.log('overflow:', of.join(' | ') || 'none');
  await pg.pdf({ path: __dirname + '/Algo-Aventures.pdf', width: '210mm', height: '297mm', printBackground: true, preferCSSPageSize: true });
  if (process.argv[2]) {
    const n = process.argv[2] === 'all' ? null : process.argv[2].split(',').map(Number);
    await pg.setViewportSize({ width: 900, height: 1200 });
    const els = await pg.$$('.page');
    const list = n || els.map((_, i) => i + 1);
    for (const i of list) await els[i - 1].screenshot({ path: __dirname + `/shots/p${String(i).padStart(2, '0')}.png` });
  }
  await b.close();
})();
