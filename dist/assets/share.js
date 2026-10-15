(()=>{
 const url=document.querySelector('link[rel="canonical"]')?.href||location.href.split(/[?#]/)[0];
 const title=document.querySelector('meta[property="og:title"]')?.content||document.title;
 const text=document.querySelector('meta[name="description"]')?.content||'';
 const message=t=>document.querySelectorAll('.share-status').forEach(x=>x.textContent=t);
 async function copy(){
  try{await navigator.clipboard.writeText(url);message('Đã sao chép. Bạn có thể dán vào Zalo hoặc Messenger.');}
  catch{message('Sao chép liên kết bên dưới:');document.querySelectorAll('.share-controls').forEach(el=>{let input=el.querySelector('input');if(!input){input=document.createElement('input');input.readOnly=true;input.setAttribute('aria-label','Liên kết trang');el.append(input);}input.value=url;input.focus();input.select();});}
 }
 document.querySelectorAll('[data-copy-link]').forEach(b=>b.addEventListener('click',copy));
 document.querySelectorAll('[data-native-share]').forEach(b=>{if(!navigator.share){b.hidden=true;return;}b.addEventListener('click',async()=>{try{await navigator.share({title,text,url});}catch(e){if(e.name!=='AbortError')await copy();}});});
})();
