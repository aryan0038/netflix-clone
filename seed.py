import requests

API_URL = "http://127.0.0.1:8000/movies"

data_db = [
    {
        "title": "The Dark Knight",
        "genre": "Action",
        "image": "https://image.tmdb.org/t/p/original/qJ2tW6WMUDux911r6m7haRef0WH.jpg",
        "backdrop": "https://image.tmdb.org/t/p/original/hkBaDkMWbLaf8B1lsWsKX7Ew3Xq.jpg",
        "trailer": "https://www.youtube.com/watch?v=EXeTwQWrcwY",
        "rating": 9.8,
        "content_type": "movie"
    },
    {
        "title": "Avengers: Endgame",
        "genre": "Action",
        "image": "https://image.tmdb.org/t/p/original/or06FN3Dka5tukK1e9sl16pB3iy.jpg",
        "backdrop": "https://image.tmdb.org/t/p/original/7RyHsO4yDXtBv1zUU3mTpHeQ0d5.jpg",
        "trailer": "https://www.youtube.com/watch?v=TcMBFSGVi1c",
        "rating": 9.5,
        "content_type": "movie"
    },
    {
        "title": "Top Gun: Maverick",
        "genre": "Action",
        "image": "https://image.tmdb.org/t/p/original/62HCnUTziyWcpDaBO2i1DX17ljH.jpg",
        "backdrop": "https://image.tmdb.org/t/p/original/AaV1YIdWKnjAIAOe8UUKBFm327v.jpg",
        "trailer": "https://www.youtube.com/watch?v=giXco2jaZ_4",
        "rating": 9.1,
        "content_type": "movie"
    },
    {
        "title": "The Matrix",
        "genre": "Action",
        "image": "https://image.tmdb.org/t/p/original/f89U3ADr1oiB1s9GkdPOEpXUk5H.jpg",
        "backdrop": "https://image.tmdb.org/t/p/original/l4QHerTSbMI7qgvasqxP36m0QA9.jpg",
        "trailer": "https://www.youtube.com/watch?v=m8e-FF8MsqU",
        "rating": 9.9,
        "content_type": "movie"
    },
    {
        "title": "Interstellar",
        "genre": "Sci-Fi",
        "image": "https://image.tmdb.org/t/p/original/gEU2QniL6E8ahDaX06e8q288UL.jpg",
        "backdrop": "https://image.tmdb.org/t/p/original/pbrkL804c8yAv3zBZR4QPEafpAR.jpg",
        "trailer": "https://www.youtube.com/watch?v=zSWdZVtXT7E",
        "rating": 9.7,
        "content_type": "movie"
    },
    {
        "title": "Breaking Bad",
        "genre": "Crime",
        "image": "https://image.tmdb.org/t/p/original/ggFHVNu6YYI5L9pCfOacjizRGt.jpg",
        "backdrop": "https://image.tmdb.org/t/p/original/tsRy63Mu5CU8etx154Isgo5RY7S.jpg",
        "trailer": "https://www.youtube.com/watch?v=HhesaQXLuRY",
        "rating": 9.9,
        "content_type": "series"
    },
    {
        "title": "Stranger Things",
        "genre": "Sci-Fi",
        "image": "https://image.tmdb.org/t/p/original/49WJfeN0moxb9IPfGn8AIqMGskD.jpg",
        "backdrop": "https://image.tmdb.org/t/p/original/56v2KjBlU4XaOv9rVYkOD8VG4ow.jpg",
        "trailer": "https://www.youtube.com/watch?v=b9EkMc79ZSU",
        "rating": 9.6,
        "content_type": "series"
    },
    {
        "title": "Squid Game",
        "genre": "Thriller",
        "image": "https://image.tmdb.org/t/p/original/dDlEmu3EZ0Pgg93K2SVNLCjCSvE.jpg",
        "backdrop": "https://image.tmdb.org/t/p/original/yF1eOkaYvwiORauRCPWznV9xVvi.jpg",
        "trailer": "https://www.youtube.com/watch?v=oqxAJKy0ii4",
        "rating": 9.1,
        "content_type": "series"
    },
     {
        "title": "The Mandalorian",
        "genre": "Sci-Fi",
        "image": "https://image.tmdb.org/t/p/original/eU1i6eHXlzMOlEq0ku1Rzq7Y4wA.jpg",
        "backdrop": "https://image.tmdb.org/t/p/original/6Lw54zxm6BAEKJeGlabyzzR5Juu.jpg",
        "trailer": "https://www.youtube.com/watch?v=aOC8E8z_ifw",
        "rating": 8.9,
        "content_type": "series"
    },
    {
        "title": "Blade Runner 2049",
        "genre": "Sci-Fi",
        "image": "https://image.tmdb.org/t/p/original/gajva2L0rPYkEWjzgFlBXCAVBE5.jpg",
        "backdrop": "https://image.tmdb.org/t/p/original/ilRyazdMJwN05exqhwK4tMKBYZs.jpg",
        "trailer": "https://www.youtube.com/watch?v=gCcx85zbxz4",
        "rating": 9.1,
        "content_type": "movie"
    }
]

print(f"🚀 Seeding {len(data_db)} 4K items...")

for item in data_db:
    item["id"] = None
    try:
        requests.post(API_URL, json=item)
        print(f"✅ Added: {item['title']}")
    except Exception as e:
        print(f"❌ Error: {e}")

print("\n✨ Done! Refresh your website now.")