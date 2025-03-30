import React, { useState } from 'react';
import './SingleArticleAnalysis.css';

function SingleArticleAnalysis() {
  const [formData, setFormData] = useState({
    Titulo: '',
    Descripcion: '',
    Label: 0
  });
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleChange = (e) => {
    const value = e.target.value;
    if (e.target.name === 'Label') {
      if (value === '' || value === '0' || value === '1') {
        setFormData({
          ...formData,
          [e.target.name]: value === '' ? 0 : Number(value)
        });
      }
    } else {
      setFormData({
        ...formData,
        [e.target.name]: value
      });
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (formData.Label !== 0 && formData.Label !== 1) {
      setError('Label must be either 0 (fake) or 1 (real)');
      return;
    }
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
    <div className="single-article-analysis">
      <h2>Single Article Analysis</h2>
      <p>Enter the details of a news article to analyze its authenticity</p>
      
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
            type="number"
            id="Label"
            name="Label"
            value={formData.Label}
            onChange={handleChange}
            required
            min="0"
            max="1"
            placeholder="Enter 0 for fake or 1 for real"
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
    </div>
  );
}

export default SingleArticleAnalysis; 