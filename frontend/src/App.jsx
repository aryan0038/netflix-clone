import { useState, useEffect } from 'react'
import { Play, Info, Plus, Search, X, Trash } from 'lucide-react'
import './App.css'

function App() {
  const [movies, setMovies] = useState([])
  const [featuredMovie, setFeaturedMovie] = useState(null)
  const [showForm, setShowForm] = useState(false)
  const [playingMovie, setPlayingMovie] = useState(null)
  const [searchTerm, setSearchTerm] = useState("") // Tracks search text
  const [newMovie, setNewMovie] = useState({ title: "", genre: "", image: "", trailer: "", rating: 0, content_type: "movie" })

  useEffect(() => {
    fetch('https://netflix-backend-sujal.vercel.app/movies')
      .then(res => res.json())
      .then(data => {
        setMovies(data)
        if (data.length > 0) {
          const random = data[Math.floor(Math.random() * data.length)]
          setFeaturedMovie(random)
        }
      })
  }, [])

  const getYouTubeEmbed = (url) => {
    if (!url) return "";
    let videoId = url.split('v=')[1];
    if (!videoId) return url;
    const ampersandPosition = videoId.indexOf('&');
    if (ampersandPosition !== -1) {
      videoId = videoId.substring(0, ampersandPosition);
    }
    return `https://www.youtube.com/embed/${videoId}?autoplay=1`;
  }

  const handleAddMovie = () => {
    fetch('http://127.0.0.1:8000/movies', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ ...newMovie, id: Date.now() })
    })
    .then(res => res.json())
    .then(saved => {
      setMovies([...movies, saved])
      setShowForm(false)
    })
  }

  // Helper to filter content for rows
  const getContent = (type, genre = null) => {
    return movies.filter(m => {
      if (genre) return m.content_type === type && m.genre === genre;
      return m.content_type === type;
    });
  }

  // Helper for the Search Bar
  const searchResults = movies.filter(m => 
    m.title.toLowerCase().includes(searchTerm.toLowerCase())
  );

  return (
    <div className="app">
      <nav className="navbar">
        <div className="logo">NETFLIX</div>
        <div className="nav-right">
          {/* SEARCH INPUT */}
          <div className="search-box">
            <Search className="icon-btn" size={20} style={{marginRight: '10px'}} />
            <input 
              type="text" 
              placeholder="Titles, people, genres" 
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              style={{background:'transparent', border:'none', color:'white', outline:'none'}}
            />
          </div>
          <Plus className="icon-btn" size={24} onClick={() => setShowForm(true)} />
        </div>
      </nav>

      {/* CONDITIONAL RENDERING: SEARCH vs HOME */}
      {searchTerm.length > 0 ? (
        // --- SEARCH MODE ---
        <div className="search-container" style={{paddingTop: '100px', paddingLeft: '40px'}}>
          <h2 style={{marginBottom: '20px'}}>Results for "{searchTerm}"</h2>
          <div style={{display: 'flex', flexWrap: 'wrap', gap: '20px'}}>
            {searchResults.map(movie => (
               <div key={movie.id} className="poster-wrapper" style={{width: '200px'}}>
                  <img 
                    className="row-poster"
                    src={movie.image} 
                    alt={movie.title}
                    style={{width: '100%'}}
                    onClick={() => setPlayingMovie(movie)}
                  />
               </div>
            ))}
            {searchResults.length === 0 && <p>No movies found.</p>}
          </div>
        </div>
      ) : (
        // --- HOME MODE (Hero + Rows) ---
        <>
          {featuredMovie && (
            <header className="hero">
              <img src={featuredMovie.backdrop} className="hero-background" alt="banner" />
              <div className="hero-content">
                <h1 className="hero-title">{featuredMovie.title}</h1>
                <div className="hero-buttons">
                  <button className="btn btn-play" onClick={() => setPlayingMovie(featuredMovie)}>
                    <Play fill="black" size={20} /> Play
                  </button>
                  <button className="btn btn-more">
                    <Info size={20} /> More Info
                  </button>
                </div>
              </div>
            </header>
          )}

          <div className="rows-container">
            <Row title="Trending Movies" movies={getContent("movie")} allMovies={movies} setMovies={setMovies} onPlay={setPlayingMovie} />
            <Row title="Binge-Worthy TV Shows" movies={getContent("series")} allMovies={movies} setMovies={setMovies} onPlay={setPlayingMovie} />
            <Row title="Action Movies" movies={getContent("movie", "Action")} allMovies={movies} setMovies={setMovies} onPlay={setPlayingMovie} />
            <Row title="Sci-Fi Series" movies={getContent("series", "Sci-Fi")} allMovies={movies} setMovies={setMovies} onPlay={setPlayingMovie} />
          </div>
        </>
      )}

      {/* MODALS */}
      {showForm && (
        <>
          <div className="modal-backdrop" onClick={() => setShowForm(false)}></div>
          <div className="add-movie-modal">
            <div style={{display:'flex', justifyContent:'space-between', marginBottom:'20px'}}>
              <h2>Add Content</h2>
              <X style={{cursor:'pointer'}} onClick={() => setShowForm(false)} />
            </div>
            <div className="form-group">
              <input placeholder="Title" onChange={e => setNewMovie({...newMovie, title: e.target.value})} />
              <input placeholder="Genre" onChange={e => setNewMovie({...newMovie, genre: e.target.value})} />
              <input placeholder="Image URL" onChange={e => setNewMovie({...newMovie, image: e.target.value})} />
              <input placeholder="Trailer URL" onChange={e => setNewMovie({...newMovie, trailer: e.target.value})} />
              <select 
                style={{width: '100%', padding: '12px', background: '#333', color: 'white', border: 'none', marginBottom: '10px', borderRadius: '4px'}}
                onChange={e => setNewMovie({...newMovie, content_type: e.target.value})}
              >
                <option value="movie">Movie</option>
                <option value="series">TV Series</option>
              </select>
              <button className="btn btn-play" style={{width:'100%', justifyContent:'center'}} onClick={handleAddMovie}>Save</button>
            </div>
          </div>
        </>
      )}

      {playingMovie && (
        <>
          <div className="modal-backdrop" onClick={() => setPlayingMovie(null)}></div>
          <div className="video-modal">
             <button className="video-close-btn" onClick={() => setPlayingMovie(null)}>Close X</button>
             <iframe 
               className="video-frame"
               src={getYouTubeEmbed(playingMovie.trailer)} 
               title="Trailer"
               allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
               allowFullScreen
             ></iframe>
          </div>
        </>
      )}
    </div>
  )
}

const Row = ({ title, movies, allMovies, setMovies, onPlay }) => {
  const handleDelete = (id) => {
    fetch(`http://127.0.0.1:8000/movies/${id}`, { method: 'DELETE' })
      .then(() => setMovies(allMovies.filter(movie => movie.id !== id)))
      .catch(err => console.error("Failed to delete:", err))
  }

  return (
    <div className="row">
      <h2 className="row-title">{title}</h2>
      <div className="row-posters">
        {movies.map(movie => (
          <div key={movie.id} className="poster-wrapper">
            <img 
              className="row-poster"
              src={movie.image} 
              alt={movie.title}
              onClick={() => onPlay(movie)}
            />
            <button className="delete-btn" onClick={(e) => {
              e.stopPropagation();
              if(confirm("Delete this?")) handleDelete(movie.id);
            }}>
              <Trash size={16} />
            </button>
          </div>
        ))}
      </div>
    </div>
  )
}

export default App