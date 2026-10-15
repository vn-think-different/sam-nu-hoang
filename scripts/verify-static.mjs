import { existsSync, readdirSync, readFileSync } from 'node:fs';
import path from 'node:path';
const root = path.resolve('dist');
if (!existsSync(path.join(root, 'index.html'))) throw new Error('Missing dist/index.html. Run python build.py and commit dist before deploying.');
function walk(dir) {
  return readdirSync(dir, { withFileTypes: true }).flatMap(e => e.isDirectory() ? walk(path.join(dir, e.name)) : [path.join(dir, e.name)]);
}
const pages = walk(root).filter(p => p.endsWith('.html'));
let checked = 0;
for (const page of pages) {
  const html = readFileSync(page, 'utf8');
  for (const m of html.matchAll(/(?:href|src)="([^"#]+)"/g)) {
    const url = m[1];
    if (/^(?:[a-z]+:|\/\/)/i.test(url)) continue;
    const target = path.resolve(path.dirname(page), decodeURIComponent(url.split(/[?#]/)[0]));
    if (!target.startsWith(root + path.sep) && target !== root) throw new Error(`Link escapes dist: ${url}`);
    if (!existsSync(target)) throw new Error(`Missing asset or page: ${url} in ${path.relative(root, page)}`);
    checked++;
  }
}
console.log(`Static website ready: ${pages.length} HTML pages, ${checked} local references verified. Output: dist`);
