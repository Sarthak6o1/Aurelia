import React, { useState, useCallback } from 'react';
import './App.css';
import ProductList from './components/ProductList';
import VideoList from './components/VideoList';
// Removed SummaryBox import

const API_URL = "http://localhost:8000/api";

function App() {
  const [query, setQuery] = useState('');
  const [minPrice, setMinPrice] = useState('');
  const [maxPrice, setMaxPrice] = useState('');
  const [minSizeValue, setMinSizeValue] = useState('');
  const [maxSizeValue, setMaxSizeValue] = useState('');
  const [sizeUnit, setSizeUnit] = useState('');

  const [results, setResults] = useState(null);
  // Removed summaryText, audioUrl, isAudioLoading states
  
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  // Removed fetchAudio function and useEffect hook

  const handleSearch = useCallback(async (e) => {
    e.preventDefault();
    setLoading(true);
    setError(null);
    setResults(null);
    // Removed summary/audio state resets

    const params = new URLSearchParams();
    params.append('q', query);
    if (minPrice) params.append('min_price', minPrice);
    if (maxPrice) params.append('max_price', maxPrice);
    if (minSizeValue) params.append('min_size_value', minSizeValue);
    if (maxSizeValue) params.append('max_size_value', maxSizeValue);
    if (sizeUnit) params.append('size_unit', sizeUnit);

    try {
      const response = await fetch(`${API_URL}/search?${params.toString()}`);
      
      if (!response.ok) {
        const errData = await response.json();
        throw new Error(errData.detail || `HTTP Error: ${response.status}`);
      }
      
      const data = await response.json();
      setResults(data);
      // Removed setSummaryText call
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  }, [query, minPrice, maxPrice, minSizeValue, maxSizeValue, sizeUnit]);

  return (
    <div className="App">
      <header className="App-header">
        <h1>Product Discovery Engine</h1>
        <form onSubmit={handleSearch} className="search-form">
          <input
            type="text"
            className="search-input"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            placeholder="Search for products..."
            required
          />
          <div className="filter-group">
            <input
              type="number"
              className="filter-input"
              value={minPrice}
              onChange={(e) => setMinPrice(e.target.value)}
              placeholder="Min Price ($)"
              step="0.01"
            />
            <input
              type="number"
              className="filter-input"
              value={maxPrice}
              onChange={(e) => setMaxPrice(e.target.value)}
              placeholder="Max Price ($)"
              step="0.01"
            />
          </div>
          <div className="filter-group">
            <input
              type="number"
              className="filter-input"
              value={minSizeValue}
              onChange={(e) => setMinSizeValue(e.target.value)}
              placeholder="Min Size"
              step="0.1"
            />
            <input
              type="number"
              className="filter-input"
              value={maxSizeValue}
              onChange={(e) => setMaxSizeValue(e.target.value)}
              placeholder="Max Size"
              step="0.1"
            />
            <select
              className="filter-input"
              value={sizeUnit}
              onChange={(e) => setSizeUnit(e.target.value)}
            >
              <option value="">All Units</option>
              <option value="ounce">Ounce (oz)</option>
              <option value="pcs">Pieces (pcs)</option>
            </select>
          </div>
          <button type="submit" disabled={loading}>
            {loading ? 'Searching...' : 'Search'}
          </button>
        </form>

        {error && <div className="error-message">Failed to fetch results: {error}</div>}
        
        {/* Removed SummaryBox component */}
        
        {results && (
          <div className="results-container">
            <ProductList products={results.products} />
            <VideoList videos={results.videos} />
          </div>
        )}
      </header>
    </div>
  );
}

export default App;