# ChatGPT2API - Ban Viet hoa

Fork nay la ban Viet hoa giao dien va thong bao nguoi dung cua `basketikun/chatgpt2api`.

> Luu y: Du an dua tren viec nghien cuu/reverse engineer cac endpoint web cua ChatGPT. Chi dung cho muc dich hoc tap, nghien cuu ca nhan va phi thuong mai. Viec su dung co the gay rui ro bi gioi han, tam khoa hoac khoa tai khoan. Khong dung tai khoan quan trong.

## Tinh nang chinh

- Giao dien web tieng Viet.
- API tuong thich OpenAI cho tao anh va sua anh.
- Quan ly nhieu tai khoan/access token.
- Trang ve anh truc tiep, lich su anh, quan ly anh.
- Cau hinh proxy, backup, Sub2API/CPA, user key.

## Chay bang Docker

Fork nay da cau hinh `docker-compose.yml` de build tu source local, vi vay nguoi dung se chay dung ban Viet hoa.

```bash
git clone https://github.com/anhphuongtranle99z-del/chatgpt2api.git
cd chatgpt2api
docker compose up -d --build
```

Dia chi sau khi chay:

- Web UI: `http://localhost:3000`
- API: `http://localhost:3000/v1`
- Thu muc du lieu: `./data`

Truoc khi public server, hay doi `auth-key` trong `config.json`, hoac cau hinh bien moi truong `CHATGPT2API_AUTH_KEY`.

## Chay local de dev

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

Mac dinh frontend dev goi backend tai `http://127.0.0.1:8000`.

## Cach dung nhanh

1. Mo web UI.
2. Dang nhap bang `auth-key` trong `config.json`.
3. Vao `Quan ly tai khoan` de import access token.
4. Vao `Ve anh` de tao/sua anh.
5. Khi goi API, them header:

```http
Authorization: Bearer <auth-key>
```

Vi du:

```bash
curl http://localhost:3000/v1/models \
  -H "Authorization: Bearer <auth-key>"
```

## Ghi chu ve Docker image

`docker-compose.yml` cua fork nay build image local `chatgpt2api-vietnamese:latest`.
Neu ban doi code, chay lai:

```bash
docker compose up -d --build
```

## Nguon goc

Du an goc: https://github.com/basketikun/chatgpt2api
