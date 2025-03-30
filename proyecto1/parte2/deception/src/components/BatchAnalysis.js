import React, { useState } from 'react';
import * as XLSX from 'xlsx';
import Papa from 'papaparse';
import './BatchAnalysis.css';

function BatchAnalysis() {
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [results, setResults] = useState(null);
  const [uploadProgress, setUploadProgress] = useState(0);

  // Required fields for the API
  const requiredFields = ['ID', 'Label', 'Titulo', 'Descripcion', 'Fecha'];

  const validateHeaders = (headers) => {
    const missingFields = requiredFields.filter(field => !headers.includes(field));
    if (missingFields.length > 0) {
      throw new Error(`Missing required fields: ${missingFields.join(', ')}`);
    }
  };

  const transformData = (data) => {
    return data.map(row => ({
      ID: row.ID || '',
      Label: parseInt(row.Label),
      Titulo: row.Titulo || '',
      Descripcion: row.Descripcion || '',
      Fecha: row.Fecha || '',
    }));
  };

  const transformDataToBatchFormat = (data) => {
    // Initialize arrays for each field
    const batchData = {
      ID: [],
      Label: [],
      Titulo: [],
      Descripcion: [],
      Fecha: []
    };

    // Populate arrays with data from each row
    data.forEach(row => {
      // Convert to string and handle null/undefined for string fields
      batchData.ID.push(String(row.ID || ''));
      batchData.Titulo.push(String(row.Titulo || ''));
      batchData.Descripcion.push(String(row.Descripcion || ''));
      batchData.Fecha.push(String(row.Fecha || ''));
      
      // Convert to integer and handle null/undefined for Label
      batchData.Label.push(parseInt(row.Label) || 0);
    });

    // Validate that we have at least one row of data
    if (batchData.Titulo.length === 0) {
      throw new Error('No valid data rows found in the file');
    }

    // Log the first row for debugging
    console.log('First row of transformed data:', {
      ID: batchData.ID[0],
      Label: batchData.Label[0],
      Titulo: batchData.Titulo[0],
      Descripcion: batchData.Descripcion[0],
      Fecha: batchData.Fecha[0]
    });

    return batchData;
  };

  const handleFileChange = (e) => {
    const selectedFile = e.target.files[0];
    if (!selectedFile) return;

    // Check file type
    const fileType = selectedFile.name.split('.').pop().toLowerCase();
    if (!['csv', 'xlsx', 'xls'].includes(fileType)) {
      setError('Please upload a CSV or Excel file');
      return;
    }

    setFile(selectedFile);
    setError(null);
  };

  const processFile = async (file) => {
    return new Promise((resolve, reject) => {
      if (file.name.endsWith('.csv')) {
        Papa.parse(file, {
          complete: (results) => {
            try {
              // Split the header by semicolon and clean up any whitespace
              const headers = results.data[0].map(header => 
                header.trim().split(';')[0]
              );
              
              // Validate headers
              validateHeaders(headers);

              // Process rows (skip header)
              const rows = results.data.slice(1).map(row => {
                // Split row by semicolon if it's a string
                const values = Array.isArray(row) ? row : row.split(';');
                const obj = {};
                headers.forEach((header, index) => {
                  obj[header] = values[index]?.trim() || '';
                });
                return obj;
              });

              // Transform data for API
              const transformedData = transformData(rows);
              resolve(transformedData);
            } catch (error) {
              reject(error);
            }
          },
          error: (error) => reject(error),
          delimiter: ";", // Set delimiter to semicolon
          header: false
        });
      } else {
        const reader = new FileReader();
        reader.onload = (e) => {
          try {
            const data = e.target.result;
            const workbook = XLSX.read(data, { type: 'array' });
            const sheetName = workbook.SheetNames[0];
            const worksheet = workbook.Sheets[sheetName];
            const rows = XLSX.utils.sheet_to_json(worksheet);

            // Validate headers
            const headers = Object.keys(rows[0] || {});
            validateHeaders(headers);

            // Transform data for API
            const transformedData = transformData(rows);
            resolve(transformedData);
          } catch (error) {
            reject(error);
          }
        };
        reader.onerror = (error) => reject(error);
        reader.readAsArrayBuffer(file);
      }
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!file) {
      setError('Please select a file');
      return;
    }

    setLoading(true);
    setError(null);
    setResults(null);
    setUploadProgress(0);

    try {
      // Process the file
      console.log('Starting file processing...');
      const rows = await processFile(file);
      console.log('File processed, first row:', rows[0]);
      setUploadProgress(50);

      // Transform data into the expected format
      console.log('Transforming data...');
      const transformedData = transformDataToBatchFormat(rows);
      console.log('Transformed data:', transformedData);
      console.log('Sample sizes:', {
        ID: transformedData.ID.length,
        Label: transformedData.Label.length,
        Titulo: transformedData.Titulo.length,
        Descripcion: transformedData.Descripcion.length,
        Fecha: transformedData.Fecha.length
      });

      // Send the data to the API
      console.log('Sending request to API...');
      const response = await fetch('http://localhost:8000/train', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(transformedData),
      });

      if (!response.ok) {
        const errorData = await response.json();
        console.log('API Error Response:', errorData);
        throw new Error(errorData.detail || 'Failed to process batch');
      }

      const [accuracy, f1, precision, recall, report, confMatrix] = await response.json();
      
      setResults({
        accuracy: accuracy,
        f1: f1,
        precision: precision,
        recall: recall,
        report: report,
        confusionMatrix: confMatrix
      });
      
      setUploadProgress(100);
    } catch (err) {
      console.error('Error details:', err);
      setError(err.message || 'An unexpected error occurred');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="batch-analysis">
      <h2>Batch Analysis</h2>
      <p>Upload a file containing multiple news articles for analysis</p>
  
      
      <form onSubmit={handleSubmit} className="upload-form">
        <div className="file-upload">
          <input
            type="file"
            accept=".csv,.xlsx,.xls"
            onChange={handleFileChange}
            className="file-input"
            id="file-upload"
          />
          <label htmlFor="file-upload" className="file-label">
            {file ? file.name : 'Choose a file'}
          </label>
        </div>

        {file && (
          <button type="submit" disabled={loading}>
            {loading ? 'Processing...' : 'Analyze Files'}
          </button>
        )}

        {loading && (
          <div className="progress-bar">
            <div 
              className="progress-fill"
              style={{ width: `${uploadProgress}%` }}
            />
            <span className="progress-text">{Math.round(uploadProgress)}%</span>
          </div>
        )}
      </form>

      {error && <div className="error">{error}</div>}
      
      {results && (
        <div className="results">
          <h3>Analysis Results</h3>
          
          <div className="metrics-grid">
            <div className="metric-card">
              <h4>Accuracy</h4>
              <p>{(results.accuracy * 100).toFixed(2)}%</p>
            </div>
            <div className="metric-card">
              <h4>F1 Score</h4>
              <p>{(results.f1 * 100).toFixed(2)}%</p>
            </div>
            <div className="metric-card">
              <h4>Precision</h4>
              <p>{(results.precision * 100).toFixed(2)}%</p>
            </div>
            <div className="metric-card">
              <h4>Recall</h4>
              <p>{(results.recall * 100).toFixed(2)}%</p>
            </div>
          </div>

          <div className="detailed-results">
            <h4>Classification Report</h4>
            <pre>{results.report}</pre>
            
            <h4>Confusion Matrix</h4>
            <div className="confusion-matrix">
              <table>
                <thead>
                  <tr>
                    <th></th>
                    <th>Predicted Fake</th>
                    <th>Predicted Real</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td><strong>Actual Fake</strong></td>
                    <td>{results.confusionMatrix[0][0]}</td>
                    <td>{results.confusionMatrix[0][1]}</td>
                  </tr>
                  <tr>
                    <td><strong>Actual Real</strong></td>
                    <td>{results.confusionMatrix[1][0]}</td>
                    <td>{results.confusionMatrix[1][1]}</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

export default BatchAnalysis; 