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
    },

    # --- ANIME & ANIMATION ---
    {"title": "Spider-Man: Into the Spider-Verse", "genre": "Animation", "image": "https://image.tmdb.org/t/p/original/iiZZdoQBEYBv6id8su7ImL0oCbD.jpg", "trailer": "https://www.youtube.com/watch?v=g4Hbz2jLxvQ", "rating": 8.4, "content_type": "movie"},
    {"title": "Your Name", "genre": "Animation", "image": "https://image.tmdb.org/t/p/original/q719jXXEzOoYaps6babgKnONONX.jpg", "trailer": "https://www.youtube.com/watch?v=s0wTdCQoc2k", "rating": 8.5, "content_type": "movie"},
    {"title": "Spirited Away", "genre": "Animation", "image": "https://image.tmdb.org/t/p/original/39wmItIWsg5sZqryyJqOqFtSJqa.jpg", "trailer": "https://www.youtube.com/watch?v=ByXuk9QqQkk", "rating": 8.5, "content_type": "movie"},
    {"title": "Demon Slayer", "genre": "Animation", "image": "https://image.tmdb.org/t/p/original/xUfRZu2mi8jH6SzQEYdB9AmCNFi.jpg", "trailer": "https://www.youtube.com/watch?v=VQGCKyvzIM4", "rating": 8.7, "content_type": "series"},
    {"title": "Attack on Titan", "genre": "Animation", "image": "https://image.tmdb.org/t/p/original/hTP1DtLGFamjfu8WqjnuQdPuy61.jpg", "trailer": "https://www.youtube.com/watch?v=MGRm4IzK1SQ", "rating": 8.9, "content_type": "series"},

    # --- HORROR & THRILLER ---
    {"title": "It", "genre": "Horror", "image": "https://image.tmdb.org/t/p/original/9E2y5Q7WlCVNEhP5GiVTJhEhx1o.jpg", "trailer": "https://www.youtube.com/watch?v=FnCdOQsX5kc", "rating": 7.3, "content_type": "movie"},
    {"title": "The Conjuring", "genre": "Horror", "image": "https://image.tmdb.org/t/p/original/wVYREutTvI2tmxr6tuFeWJqa6x.jpg", "trailer": "https://www.youtube.com/watch?v=k10ETZ41q5o", "rating": 7.5, "content_type": "movie"},
    {"title": "A Quiet Place", "genre": "Horror", "image": "https://image.tmdb.org/t/p/original/nA7gP338mFjW66i8P0jQ3g7jQ3.jpg", "trailer": "https://www.youtube.com/watch?v=WR7cc5t7tv8", "rating": 7.4, "content_type": "movie"},
    {"title": "Get Out", "genre": "Thriller", "image": "https://image.tmdb.org/t/p/original/tFXcEccSQMf3lfhfXKSU9iRBpa3.jpg", "trailer": "https://www.youtube.com/watch?v=DzfpyUB60YY", "rating": 7.7, "content_type": "movie"},
    {"title": "Parasite", "genre": "Thriller", "image": "https://image.tmdb.org/t/p/original/7IiTTgloJzvGI1TAYymCfbfl3vT.jpg", "trailer": "https://www.youtube.com/watch?v=5xH0HfJHsaY", "rating": 8.5, "content_type": "movie"},

    # --- COMEDY ---
    {"title": "The Hangover", "genre": "Comedy", "image": "https://image.tmdb.org/t/p/original/ulzhLuWrPK07P1YkdWQLZnQh1JL.jpg", "trailer": "https://www.youtube.com/watch?v=tcdUhdOlz9M", "rating": 7.3, "content_type": "movie"},
    {"title": "Superbad", "genre": "Comedy", "image": "https://image.tmdb.org/t/p/original/ek8e8txUyUwd2Bnqhw67G88h0bH.jpg", "trailer": "https://www.youtube.com/watch?v=4eaZ_48ZYog", "rating": 7.6, "content_type": "movie"},
    {"title": "The Office", "genre": "Comedy", "image": "https://image.tmdb.org/t/p/original/qWnJzyZhyy74gJPM6eQLtXOIc2s.jpg", "trailer": "https://www.youtube.com/watch?v=LHOtME2DL4g", "rating": 8.9, "content_type": "series"},
    {"title": "Friends", "genre": "Comedy", "image": "https://image.tmdb.org/t/p/original/f496cm9enuEsZkSPzCwnTESEK5s.jpg", "trailer": "https://www.youtube.com/watch?v=hDNNmeeJs1Q", "rating": 8.4, "content_type": "series"},
    {"title": "Brooklyn Nine-Nine", "genre": "Comedy", "image": "https://image.tmdb.org/t/p/original/hgRMKCnNGpTwfVvJ7eQ49r99cM.jpg", "trailer": "https://www.youtube.com/watch?v=sEOuJ4z5aTc", "rating": 8.2, "content_type": "series"},

    # --- CLASSICS ---
    {"title": "The Godfather", "genre": "Crime", "image": "https://image.tmdb.org/t/p/original/3bhkrj58Vtu7enYsRolD1fZdja1.jpg", "trailer": "https://www.youtube.com/watch?v=sY1S34973zA", "rating": 8.7, "content_type": "movie"},
    {"title": "Pulp Fiction", "genre": "Crime", "image": "https://image.tmdb.org/t/p/original/d5iIlFn5s0ImszYzBPb8JPIfbXD.jpg", "trailer": "https://www.youtube.com/watch?v=s7EdQ4FqbhY", "rating": 8.5, "content_type": "movie"},
    {"title": "Fight Club", "genre": "Drama", "image": "https://image.tmdb.org/t/p/original/pB8BM7pdSp6B6Ih7QZ4DrQ3PmJK.jpg", "trailer": "https://www.youtube.com/watch?v=qtRKdVHc-cE", "rating": 8.4, "content_type": "movie"},
    {"title": "Forrest Gump", "genre": "Drama", "image": "https://image.tmdb.org/t/p/original/arw2vcBveWOVZr6pxd9XTd1TdQa.jpg", "trailer": "https://www.youtube.com/watch?v=bLvqoHBptjg", "rating": 8.8, "content_type": "movie"},
    {"title": "The Shawshank Redemption", "genre": "Drama", "image": "https://image.tmdb.org/t/p/original/q6y0Go1tsGEsmtFryDOJo3dEmqu.jpg", "trailer": "https://www.youtube.com/watch?v=6hB3S9bIaco", "rating": 8.7, "content_type": "movie"}
]

print(f"🚀 Seeding {len(data_db)} items...")

for item in data_db:
    item["id"] = None
    
    # --- AUTO-FIX MISSING BACKDROPS ---
    # This prevents errors for the new movies that don't have a backdrop
    if "backdrop" not in item:
        item["backdrop"] = item["image"]
        
    try:
        requests.post(API_URL, json=item)
        print(f"✅ Added: {item['title']}")
    except Exception as e:
        print(f"❌ Error: {e}")

print("\n✨ Done! Refresh your website now.")