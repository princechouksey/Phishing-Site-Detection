import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { detectPhishing } from '../services/api';

const URLInput = () => {
  const [url, setUrl] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const navigate = useNavigate();
  console.log(url)

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (url === '') return;

    setLoading(true);
    setError('');
    try {
      const response = await detectPhishing(url);
      console.log(response)
      navigate('/results', { state: { result: response.data } });
    } catch (error) {
      setError('Failed to detect phishing.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <input
          type="url"
          placeholder="Enter URL to scan"
          className="w-full px-4 py-2 mb-4 border border-gray-300 rounded"
          value={url}
          onChange={(e) => setUrl(e.target.value)}
        />
        <button
          type="submit"
          className="w-full bg-blue-500 text-white py-2 rounded"
          disabled={loading}
        >
          {loading ? 'Detecting...' : 'Detect Phishing'}
        </button>
      </form>
      {error && <div className="text-red-500">{error}</div>}
    </div>
  );
};

export default URLInput;
