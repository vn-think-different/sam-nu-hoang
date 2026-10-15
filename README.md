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
