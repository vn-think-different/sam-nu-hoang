"""Check generated HTML and local social assets without relying on JavaScript."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit
import json,xml.etree.ElementTree as ET
from PIL import Image
root=Path(__file__).resolve().parents[1]/'dist'
origin='https://samnuhoang.vercel.app'
class Head(HTMLParser):
 def __init__(self):super().__init__();self.meta={};self.canonical=[];self.json=[];self.in_json=False;self.buffer=''
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='meta':
   k=a.get('property',a.get('name'))
   if k:self.meta.setdefault(k,[]).append(a.get('content',''))
  if tag=='link' and a.get('rel')=='canonical':self.canonical.append(a['href'])
  if tag=='script' and a.get('type')=='application/ld+json':self.in_json=True;self.buffer=''
 def handle_data(self,data):
  if self.in_json:self.buffer+=data
 def handle_endtag(self,tag):
  if tag=='script' and self.in_json:self.json.append(json.loads(self.buffer));self.in_json=False
indexed=set();images=set();article_count=0
for p in root.rglob('*.html'):
 h=Head();raw=p.read_text();h.feed(raw)
 assert 'T\u01b0u' not in raw and 'T\u01afU' not in raw,(p,'old brand spelling')
 assert len(h.canonical)==1,(p,'canonical count')
 url=h.canonical[0];assert url.startswith(origin+'/'),url
 assert 'sam-nu-hoang.dewy-crumb-9497.chatgpt.site' not in raw,p
 for key in ['description','robots','og:title','og:description','og:type','og:url','og:image','og:image:width','og:image:height','og:image:alt','twitter:card']:
  assert len(h.meta.get(key,[]))==1 and h.meta[key][0],(p,key)
 assert h.meta['og:url'][0]==url
 imurl=h.meta['og:image'][0];assert imurl.startswith(origin+'/assets/social/')
 file=root/urlsplit(imurl).path.lstrip('/')
 with Image.open(file) as im:assert im.size==(int(h.meta['og:image:width'][0]),int(h.meta['og:image:height'][0])),p
 images.add(file)
 assert h.json and h.json[0]['@context']=='https://schema.org'
 if 'noindex' not in h.meta['robots'][0]:indexed.add(url)
 for node in h.json[0]['@graph']:
  if node['@type']=='BlogPosting':article_count+=1;assert node['headline'] and node['author']['url'].startswith(origin)
  if node['@type']=='Product':assert not any(k in node for k in ['offers','aggregateRating','review']),p
sitemap={e.text for e in ET.parse(root/'sitemap.xml').findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}loc')}
assert sitemap==indexed,(sitemap^indexed)
robots=(root/'robots.txt').read_text();assert 'Disallow: /' not in robots and origin+'/sitemap.xml' in robots
assert article_count==len(json.loads((root.parent/'articles.json').read_text()))
print(f'SEO verified: {len(list(root.rglob("*.html")))} pages, {len(indexed)} indexable URLs, {article_count} article schemas, {len(images)} social images. No fictional offers/reviews.')
