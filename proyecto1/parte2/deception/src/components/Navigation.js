import React from 'react';
import { Link, useLocation } from 'react-router-dom';
import './Navigation.css';

function Navigation() {
  const location = useLocation();

  return (
    <nav className="navigation">
      <div className="nav-brand">
        <h1>Deception Detection</h1>
      </div>
      <div className="nav-links">
        <Link 
          to="/" 
          className={location.pathname === '/' ? 'active' : ''}
        >
          Single Article Analysis
        </Link>
        <Link 
          to="/batch-analysis" 
          className={location.pathname === '/batch-analysis' ? 'active' : ''}
        >
          Batch Analysis
        </Link>
      </div>
    </nav>
  );
}

export default Navigation; 