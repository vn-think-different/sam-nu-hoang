"""Server-rendered SEO and social metadata, shared by every generated page."""
import os
from datetime import datetime
SITE_URL=os.environ.get('SITE_URL','https://samnuhoang.vercel.app').rstrip('/')
SITE_NAME='Sâm Nữ Hoàng Đỗ Thị Tuyết'
NOINDEX={'404','thuong-hieu'}
def canonical(slug):return SITE_URL+('/404.html' if slug=='404' else '/'+(slug+'/' if slug else ''))
def seo_image(slug):
 if slug.startswith('kien-thuc/'):
  key=ARTMAP[slug.split('/')[-1]]['image']
  path=A/'social'/f'{key}.jpg'
  if path.exists():
   with Image.open(path) as im:w,h=im.size
   return SITE_URL+f'/assets/social/{key}.jpg',w,h,ARTMAP[slug.split('/')[-1]]['caption']
 return SITE_URL+'/assets/social/sam-nu-hoang-v1.jpg',1200,630,'Sâm Nữ Hoàng Đỗ Thị Tuyết — Ngự Vị Nữ Hoàng Tưu, trống gỗ sồi và bình hồ lô'
def seo_graph(slug,title,description):
 url=canonical(slug);image_url,w,h,alt=seo_image(slug)
 business={'@type':'LocalBusiness','@id':SITE_URL+'/#business','name':SITE_NAME,'legalName':B['name'],'url':SITE_URL+'/','image':SITE_URL+'/assets/social/sam-nu-hoang-v1.jpg','logo':{'@type':'ImageObject','url':SITE_URL+'/assets/logo-original.png'},'telephone':'+84972686765','address':{'@type':'PostalAddress','streetAddress':'Số 19A, ngõ 17, thôn Trung Thượng, xã Đại Hùng','addressLocality':'Ứng Hòa','addressRegion':'Hà Nội','addressCountry':'VN'}}
 graph=[business,{'@type':'WebSite','@id':SITE_URL+'/#website','url':SITE_URL+'/','name':SITE_NAME,'alternateName':'Sâm Nữ Hoàng','inLanguage':'vi-VN','publisher':{'@id':SITE_URL+'/#business'}}]
 page={'@type':'WebPage','@id':url+'#webpage','url':url,'name':title,'description':description,'inLanguage':'vi-VN','isPartOf':{'@id':SITE_URL+'/#website'},'primaryImageOfPage':{'@type':'ImageObject','url':image_url,'width':w,'height':h}}
 if slug=='gioi-thieu':page['@type']='AboutPage'
 elif slug=='lien-he':page['@type']='ContactPage'
 elif slug in ['san-pham','san-pham/ruou-sam','kien-thuc','thu-vien']:page['@type']='CollectionPage'
 if slug and slug!='404':
  crumbs=[{'@type':'ListItem','position':1,'name':'Trang chủ','item':SITE_URL+'/'}]
  bits=slug.split('/')
  for i in range(len(bits)):
   key='/'.join(bits[:i+1]);label=pages[key][0].split(' | ')[0] if key in pages else bits[i]
   crumbs.append({'@type':'ListItem','position':len(crumbs)+1,'name':label,'item':canonical(key)})
  graph.append({'@type':'BreadcrumbList','@id':url+'#breadcrumb','itemListElement':crumbs});page['breadcrumb']={'@id':url+'#breadcrumb'}
 if slug.startswith('kien-thuc/'):
  a=ARTMAP[slug.split('/')[-1]];published=datetime.strptime(a['date'],'%d/%m/%Y').strftime('%Y-%m-%d')+'T00:00:00+07:00'
  graph.append({'@type':'BlogPosting','@id':url+'#article','mainEntityOfPage':{'@id':url+'#webpage'},'headline':a['title'],'description':a['intro'],'image':[image_url],'datePublished':published,'inLanguage':'vi-VN','articleSection':a['tag'],'author':{'@type':'Organization','name':SITE_NAME,'url':SITE_URL+'/gioi-thieu/'},'publisher':{'@id':SITE_URL+'/#business'},'citation':[x['url'] for x in a['sources']]})
 elif slug.startswith('san-pham/ruou-sam/'):
  key=slug.split('/')[-1];w=families[key]
  graph.append({'@type':'Product','@id':url+'#product','name':'Ngự Vị Nữ Hoàng Tưu — '+w['name'],'description':w['desc'],'image':[SITE_URL+f'/assets/photo-{w["cover"]:02d}.webp'],'brand':{'@type':'Brand','name':'Ngự Vị Nữ Hoàng Tưu'},'url':url})
  # Never publish hypothetical price, stock, ABV or invented reviews as structured facts.
 graph.append(page)
 return {'@context':'https://schema.org','@graph':graph}
def seo_head(slug,title,description):
 url=canonical(slug);img,w,h,alt=seo_image(slug);article=slug.startswith('kien-thuc/')
 tags=[('property','og:title',title),('property','og:description',description),('property','og:type','article' if article else 'website'),('property','og:site_name',SITE_NAME),('property','og:locale','vi_VN'),('property','og:url',url),('property','og:image',img),('property','og:image:secure_url',img),('property','og:image:type','image/jpeg'),('property','og:image:width',w),('property','og:image:height',h),('property','og:image:alt',alt),('name','twitter:card','summary_large_image'),('name','twitter:title',title),('name','twitter:description',description),('name','twitter:image',img),('name','twitter:image:alt',alt),('name','robots','noindex,follow' if slug in NOINDEX else 'index,follow,max-image-preview:large'),('name','application-name',SITE_NAME)]
 if article:
  a=ARTMAP[slug.split('/')[-1]];tags += [('property','article:published_time',datetime.strptime(a['date'],'%d/%m/%Y').strftime('%Y-%m-%d')+'T00:00:00+07:00'),('property','article:section',a['tag'])]
 return '\n'.join(f'<meta {kind}="{key}" content="{e(value)}">' for kind,key,value in tags)+f'\n<link rel="canonical" href="{url}"><link rel="icon" type="image/png" sizes="64x64" href="{base}assets/favicon-64.png"><link rel="apple-touch-icon" sizes="180x180" href="{base}assets/apple-touch-icon.png"><link rel="manifest" href="{base}site.webmanifest">'
def share_controls():
 return '<div class="share-controls" aria-label="Chia sẻ trang"><span>Chia sẻ</span><button type="button" data-native-share>Chia sẻ trang ↗</button><button type="button" data-copy-link>Sao chép liên kết</button><span class="share-status" role="status" aria-live="polite"></span></div>'
