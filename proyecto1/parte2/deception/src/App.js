import React, { useState } from 'react';
import './App.css';

function App() {
  const [formData, setFormData] = useState({
    Titulo: '',
    Descripcion: '',
    Label: ''
  });
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError(null);
    
    try {
      const response = await fetch('http://localhost:8000/predict', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });
      
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      
      const data = await response.json();
      setResult(data);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Deception Detection</h1>
        <p>Test our fake news detection system</p>
      </header>
      
      <main className="App-main">
        <form onSubmit={handleSubmit} className="deception-form">
          <div className="form-group">
            <label htmlFor="Titulo">Title:</label>
            <input
              type="text"
              id="Titulo"
              name="Titulo"
              value={formData.Titulo}
              onChange={handleChange}
              required
              placeholder="Enter the news title"
            />
          </div>
          
          <div className="form-group">
            <label htmlFor="Descripcion">Description:</label>
            <textarea
              id="Descripcion"
              name="Descripcion"
              value={formData.Descripcion}
              onChange={handleChange}
              required
              placeholder="Enter the news description"
            />
          </div>

          <div className="form-group">
            <label htmlFor="Label">Label:</label>
            <input
              type="text"
              id="Label"
              name="Label"
              value={formData.Label}
              onChange={handleChange}
              required
              placeholder="Enter the label (fake/real)"
            />
          </div>

          <button type="submit" disabled={loading}>
            {loading ? 'Analyzing...' : 'Analyze News'}
          </button>
        </form>

        {error && <div className="error">{error}</div>}
        
        {result && (
          <div className="result">
            <h2>Analysis Result:</h2>
            <pre>{JSON.stringify(result, null, 2)}</pre>
          </div>
        )}
      </main>
    </div>
  );
}

export default App;
