import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navigation from './components/Navigation';
import SingleArticleAnalysis from './components/SingleArticleAnalysis';
import BatchAnalysis from './components/BatchAnalysis';
import './App.css';

function App() {
  return (
    <div className="App">
      <Router>
        <Navigation />
        <main className="App-main">
          <Routes>
            <Route path="/" element={<SingleArticleAnalysis />} />
            <Route path="/batch-analysis" element={<BatchAnalysis />} />
          </Routes>
        </main>
      </Router>
    </div>
  );
}

export default App;
