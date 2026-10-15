# Sâm Nữ Hoàng

Website tĩnh tiếng Việt giới thiệu doanh nghiệp, sâm tươi, sâm khô, rượu sâm và cao sâm. Giao diện đáp ứng theo kích thước màn hình; không cần cài đặt thư viện JavaScript.

## Cấu trúc

- `dist/index.html`: trang chủ.
- `dist/gioi-thieu/`: giới thiệu doanh nghiệp.
- `dist/san-pham/`: bộ lọc bốn danh mục và trang chi tiết từng danh mục.
- `dist/kien-thuc/`: liên kết tới nguồn xuất bản gốc.
- `dist/lien-he/`: thông tin liên hệ và danh sách quan tâm cục bộ.
- Các trang hướng dẫn mua hàng, giao hàng/đổi trả, quyền riêng tư và điều khoản.
- `content.json`: nội dung danh mục, nguồn tham khảo và chính sách.
- `build.py`: dựng lại HTML từ nội dung; chạy `python build.py` (Python 3 và Pillow).

Các ảnh WebP đã tối ưu nằm trong `dist/assets/`. Khi không có bộ ảnh gốc trong workspace, trình dựng giữ nguyên các ảnh đã đóng gói. CSS và JavaScript được lưu trực tiếp trong thư mục assets.

## Chạy và triển khai

Chạy `python -m http.server 8000 --directory dist` để xem cục bộ. Mọi máy chủ website tĩnh đều có thể phục vụ thư mục `dist/`. Workflow GitHub Pages có thể chạy bằng tay khi chủ repo đã bật Pages với nguồn GitHub Actions. Liên kết tài nguyên dùng đường dẫn tương đối để hỗ trợ cả website gốc và đường dẫn repo.

## Các phần cần bổ sung trước khi bán hàng

1. Tên pháp nhân, mã số doanh nghiệp, địa chỉ, số điện thoại/Zalo, email.
2. Ảnh sâm tươi, sâm khô, cao sâm; mã hàng, giá, khối lượng, tồn kho.
3. Thành phần, nguồn nguyên liệu, bảo quản, hướng dẫn sử dụng và hồ sơ chất lượng.
4. Dung tích, nồng độ cồn và nhãn chính thức của Ngự Vị Nữ Hoàng Tưu.
5. Chính sách giao hàng, đổi trả, thanh toán và quy trình tiếp nhận đơn được doanh nghiệp phê duyệt.

Chưa có checkout, thanh toán, gửi yêu cầu hoặc lưu đơn trên máy chủ. Danh sách quan tâm và ghi chú chỉ lưu trong localStorage; tệp tải về chưa được gửi tới doanh nghiệp. Không có giá giả, số điện thoại mẫu, chứng nhận hoặc công dụng chữa bệnh tự tạo.

## Nguồn nội dung

Chỉ sử dụng các ảnh rượu do chủ dự án cung cấp ở thư mục gốc của bộ dữ liệu. Các bài viết báo chí được dẫn liên kết tới nguồn; không đóng gói toàn văn, ảnh báo chí hoặc các tệp thu thập vào kho công khai. Xem `ASSET_SOURCES.md` để đối chiếu ảnh.
