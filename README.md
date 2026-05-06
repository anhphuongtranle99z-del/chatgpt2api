# ChatGPT2API - Bản Việt hóa

Fork này là bản Việt hóa giao diện và thông báo người dùng của `basketikun/chatgpt2api`.

> Lưu ý: Dự án dựa trên việc nghiên cứu/reverse engineer các endpoint web của ChatGPT. Chỉ dùng cho mục đích học tập, nghiên cứu cá nhân và phi thương mại. Việc sử dụng có thể gây rủi ro bị giới hạn, tạm khóa hoặc khóa tài khoản. Không dùng tài khoản quan trọng.

## Tính năng chính

- Giao diện web tiếng Việt.
- API tương thích OpenAI cho tạo ảnh và sửa ảnh.
- Quản lý nhiều tài khoản/access token.
- Trang vẽ ảnh trực tiếp, lịch sử ảnh, quản lý ảnh.
- Cấu hình proxy, backup, Sub2API/CPA, user key.

## Chạy bằng Docker

Fork này đã cấu hình `docker-compose.yml` để build từ source local, vì vậy người dùng sẽ chạy đúng bản Việt hóa.

```bash
git clone https://github.com/anhphuongtranle99z-del/chatgpt2api.git
cd chatgpt2api
docker compose up -d --build
```

Địa chỉ sau khi chạy:

- Web UI: `http://localhost:3000`
- API: `http://localhost:3000/v1`
- Thư mục dữ liệu: `./data`

Trước khi public server, hãy đổi `auth-key` trong `config.json`, hoặc cấu hình biến môi trường `CHATGPT2API_AUTH_KEY`.

## Chạy local để dev

Backend:

```bash
uv sync
uv run main.py
```

Frontend dev:

```bash
cd web
npm install
npm run dev
```

Mặc định frontend dev gọi backend tại `http://127.0.0.1:8000`.

## Cách dùng nhanh

1. Mở web UI.
2. Đăng nhập bằng `auth-key` trong `config.json`.
3. Vào `Quản lý tài khoản` để import access token.
4. Vào `Vẽ ảnh` để tạo/sửa ảnh.
5. Khi gọi API, thêm header:

```http
Authorization: Bearer <auth-key>
```

Ví dụ:

```bash
curl http://localhost:3000/v1/models \
  -H "Authorization: Bearer <auth-key>"
```

## Ghi chú về Docker image

`docker-compose.yml` của fork này build image local `chatgpt2api-vietnamese:latest`.
Nếu bạn đổi code, chạy lại:

```bash
docker compose up -d --build
```

## Nguồn gốc

Dự án gốc: https://github.com/basketikun/chatgpt2api
