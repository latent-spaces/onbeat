const { chromium } = await import(process.argv[2]);
const b = await chromium.launch({ args: ['--single-process'] });
const p = await b.newPage({ viewport: { width: 1080, height: 1350 } });
await p.goto('file://' + process.cwd() + '/card.html');
for (const id of ['s1','s2','s3']) await p.locator('#'+id).screenshot({ path: id + '.png' });
await b.close();
