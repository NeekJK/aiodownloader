import requests

def download_tiktok_video(url, save_path):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
    }

    try:
        print(f"Downloading from: {url}")

        response = requests.get(url, headers=headers, stream=True)
        response.raise_for_status()  # Check for HTTP errors

        with open(save_path, 'wb') as video_file:
            for chunk in response.iter_content(chunk_size=1024):
                video_file.write(chunk)

        print(f"Download complete: {save_path}")

    except requests.RequestException as e:
        print(f"Error downloading video: {e}")

if __name__ == "__main__":
    video_urls = [
        "https://v16-webapp-prime.tiktok.com/video/tos/useast2a/tos-useast2a-pve-0068/oMQcIgBJRpdbAzDnhFDNfuK2kNgEJERQJ9lvBe/?a=1988&bti=ODszNWYuMDE6&ch=0&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C&cv=1&br=3172&bt=1586&cs=0&ds=6&ft=-Csk_mc3PD12NeqgCE-UxgRFSY6e3wv25NcAp&mime_type=video_mp4&qs=0&rc=PGY2NDU3ZGhmZGg8OzZmOUBpM3F1aGo5cmw4dzMzNzczM0BgMjQ1Yl80Nl8xLWAvNDUyYSM2cW01MmRjM2tgLS1kMTZzcw%3D%3D&btag=e00088000&expire=1740072770&l=202502190132051A7ADD863A5B76788947&ply_type=2&policy=2&signature=6d65191ff905f31fa4160febb6910dcc&tk=tt_chain_token",
        "https://v16-webapp-prime.tiktok.com/video/tos/alisg/tos-alisg-pve-0037c001/ocaIz1i6aBmRqqoRCoxYGLwIBfA2iAQY5A2zQE/?a=1988&bti=ODszNWYuMDE6&ch=0&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C&cv=1&br=2020&bt=1010&cs=0&ds=6&ft=I~da4oA-D12Nvze3~eIxROOSHlBF-UjNSfopiX&mime_type=video_mp4&qs=0&rc=cnF8b2hsc2d3SkBwaHIxaDFybndmaTs4PDNmZzk2ZTw1NTg3aEBpM3JlZG05cmY0eDMzODczNEBjRl5Nc3FePmJKYSNvYF90aHFmOiM2NTM2NGAzXy8xYF8tXjRfYSNhZjBnMmRjZWlgLS1kMS1zcw%3D%3D&btag=e000b8000&expire=1740072951&l=20250219013536FC1B448F2B50C1742DAE&ply_type=2&policy=2&signature=a4c90be407f39257c38e71130c5bbc30&tk=tt_chain_token"
    ]

    for index, url in enumerate(video_urls, start=1):
        save_path = f"tiktok_video_{index}.mp4"
        download_tiktok_video(url, save_path)
