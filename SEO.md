# SEO và chia sẻ liên kết

Tên miền chuẩn: https://samnuhoang.vercel.app . Đổi một lần qua biến `SITE_URL` khi chạy `build.py` nếu chuyển tên miền. Không dùng địa chỉ bản ChatGPT Site làm canonical của Vercel.

Đã triển khai:
- Metadata trong HTML gốc: tiêu đề, mô tả, canonical, robots, Open Graph, Twitter large image. Không cần chạy JavaScript để bot đọc.
- Ảnh chia sẻ trang chủ JPEG 1200×630 tại `/assets/social/sam-nu-hoang-v1.jpg`; bài tư liệu có ảnh riêng và đúng kích thước khai báo. Không đưa giá giả định vào banner.
- robots.txt cho phép crawl; sitemap.xml chỉ gồm trang indexable. Trang 404 và trang tải bộ nhận diện vẫn noindex,follow.
- JSON-LD WebSite, LocalBusiness, WebPage, BreadcrumbList, BlogPosting; Product cho các mẫu rượu. Không có Offer/giá/nồng độ/tồn kho/đánh giá giả định trong structured data. Vì chưa có giá được xác nhận, chưa đặt mục tiêu hiển thị rich result bán hàng.
- Biểu tượng PNG, Apple touch icon và manifest nhận diện; không tuyên bố offline/PWA.
- Nút chia sẻ hệ thống khi trình duyệt hỗ trợ; sao chép URL canonical để gửi Zalo/Messenger. Không tự gửi tin nhắn.

Kiểm tra trước triển khai:
```
python build.py
python scripts/check-seo.py
node scripts/verify-static.mjs
node --check dist/assets/share.js
```

Việc cần tài khoản chủ sở hữu (chưa thực hiện):
1. Thêm URL-prefix property `https://samnuhoang.vercel.app/` vào Google Search Console, xác minh bằng tệp HTML hoặc thẻ meta do Google cấp. Không tự tạo mã xác minh.
2. Gửi sitemap `https://samnuhoang.vercel.app/sitemap.xml`, yêu cầu kiểm tra URL trang chủ sau xác minh.
3. Nếu dùng GA4, cung cấp Measurement ID thật để triển khai đo lường; hiện chưa chèn mã theo dõi giả hoặc gửi dữ liệu người dùng tới bên thứ ba.

Zalo/Messenger có thể lưu kết quả preview trước đó. Metadata mới không sửa ngược các tin nhắn cũ và không bảo đảm mọi ứng dụng hiển thị cùng bố cục. Có thể dùng Facebook Sharing Debugger (https://developers.facebook.com/tools/debug/) với tài khoản phù hợp để yêu cầu đọc lại URL. Chưa thực hiện thao tác này thay người dùng.

Nguồn kỹ thuật:
- https://ogp.me/
- https://developers.google.com/search/docs/crawling-indexing/robots/intro
- https://developers.google.com/search/docs/appearance/structured-data/article
- https://developers.google.com/search/docs/appearance/structured-data/product-snippet

Ảnh banner được dựng bằng công cụ tạo ảnh tích hợp, dựa trên logo và ảnh sản phẩm đã được cung cấp. Brief: banner bordeaux/vàng champagne, thương hiệu Đỗ Thị Tuyết — Sâm Nữ Hoàng, trống gỗ sồi và bình hồ lô; loại bỏ mọi củ, quả hoặc nguyên liệu trang trí ngoài hai mẫu bao bì.
