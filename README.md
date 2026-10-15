# Sâm Nữ Hoàng — Ngự Vị Nữ Hoàng Tưu

Website tĩnh tiếng Việt của hộ kinh doanh cá thể Đỗ Thị Tuyết. Hotline 0972 686 765. Địa chỉ do chủ dự án cung cấp: Số 19A, ngõ 17, thôn Trung Thượng, xã Đại Hùng, Ứng Hòa, Hà Nội.

## Cấu trúc

21 trang: trang chủ, giới thiệu hộ kinh doanh, vùng trồng, bốn danh mục sản phẩm, năm trang quy cách rượu, thư viện 48 ảnh, kiến thức, liên hệ và bốn trang hỗ trợ/chính sách; có trang 404.

- `content.json`: nội dung hộ kinh doanh, diện tích trồng, các dòng sản phẩm và năm nhóm bao bì rượu.
- `image-inventory.json`: đối chiếu 48 ảnh sản phẩm và 2 ảnh ghi chép với tên gốc.
- `build.py`: dựng HTML, sitemap, robots; `python build.py` (Python 3 và Pillow).
- `dist/`: nội dung triển khai trên máy chủ tĩnh, không cần Node hoặc thư viện JavaScript ở runtime.
- `dist/assets/`: ảnh WebP thực tế, CSS, JavaScript và phông Noto có ký tự tiếng Việt.

Khi có ảnh gốc trong workspace, trình dựng tối ưu lại ảnh. Khi không có, giữ nguyên các ảnh đã đóng gói. Chạy `python -m http.server 8000 --directory dist` để xem cục bộ. Workflow GitHub Pages chạy bằng tay khi Pages đã được cấu hình với nguồn GitHub Actions.

## Trải nghiệm

- Tìm kiếm không dấu và lọc gỗ sồi/thủy tinh trong bộ sưu tập.
- Ảnh chính, ảnh nhỏ, phóng to, ảnh trước/sau, phím mũi tên và Escape.
- Danh sách quan tâm lưu đúng nhóm quy cách; giữ tương thích dữ liệu cũ.
- Tải danh sách dạng văn bản; gọi hotline trực tiếp. Chưa có thanh toán hoặc gửi đơn tự động.
- Chuyển động xuất hiện khi cuộn và tương tác ảnh; tắt theo `prefers-reduced-motion`. Nội dung vẫn hiển thị khi JavaScript bị tắt.
- Giao diện responsive, menu di động, điều hướng bằng bàn phím, metadata và dữ liệu LocalBusiness.

## Nguồn và giới hạn nội dung

Tổng vùng trồng 3 ha: 2 ha tại Sóc Sơn, 1 ha tại Ứng Hòa, Hà Nội, theo chủ dự án. Không đưa ra chứng nhận, tuổi sâm, công dụng chữa bệnh hoặc thông số sản phẩm chưa có hồ sơ.

Năm nhóm bao bì rượu: trống gỗ sồi, bình thủy tinh dáng trống, bình thủy tinh đa giác, bình hồ lô, chai thủy tinh. Nhiều góc ảnh không tương đương nhiều mã hàng. Dung tích, nồng độ cồn, giá, cấu hình sẵn có và giao nhận được xác nhận qua hotline.

Ảnh và hồ sơ chi tiết của sâm tươi, sâm khô, cao sâm sẽ bổ sung sau. Email, mã số đăng ký hộ kinh doanh và hồ sơ chất lượng chưa được cung cấp. Bài viết báo chí chỉ dẫn nguồn gốc. Xem `ASSET_SOURCES.md`.

## Bản duyệt mới: nhận diện bordeaux / champagne / ivory

30 trang, 8 bài biên soạn, danh mục 52 nguồn từ CSV, 5 nhóm bao bì rượu, 48 ảnh gốc và các ảnh sản phẩm đã xử lý. Logo tải tại `/thuong-hieu/`.

- `articles.json`: bài viết, mục lục, nguồn và liên kết liên quan.
- `prototype-catalog.json`: quy cách, giá và ABV giả định để duyệt.
- `design.py`: bố cục mới và trang biên tập.
- `dist/assets/luxury.css`, `luxury.js`: responsive, chuyển động giảm khi người dùng chọn reduced-motion, chọn quy cách/số lượng, dự toán lưu cục bộ, tải TXT.
- `source-index.json`: chỉ mục từ CSV, không chứa các tệp cá nhân ngoài hồ sơ.
- `PRICE_SOURCES.md`, `editorial-image-sources.json`: cơ sở giá và nguồn ảnh.

Build: `python build.py` (Pillow cần cài). Tệp `prepare_editorial.py` là bản khởi tạo dữ liệu; không chạy lại sau khi sửa JSON thủ công.

Giới hạn: đây là bản duyệt riêng tư/noindex, chưa xác nhận giá và thông số; cao sâm là hình bao bì đề xuất. Không có xử lý thanh toán hay gửi đơn. Logo PNG cần vector hóa sau khi duyệt để in ấn. Các ảnh xử lý AI không dùng để đọc thành phần nhãn.

## Vercel

`vercel.json` phục vụ trực tiếp website đã tạo trong `dist/`. Không cần cài Python/Pillow trên Vercel. Build Command chạy `node scripts/verify-static.mjs` để phát hiện đầu ra thiếu, sau đó Vercel xuất bản thư mục `dist`.

Trong Vercel: Root Directory để trống (gốc repo), Framework Preset = Other; các thiết lập build/output lấy từ `vercel.json`. Production Branch = main. Nếu đang xem deployment cũ 1c688a0, tạo deployment từ commit mới thay vì redeploy lại commit cũ.
