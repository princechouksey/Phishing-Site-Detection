import React from 'react';

const ResultDisplay = ({ result }) => {
  return (
    <div className="mt-4">
      {result ? (
        <div>
          <h3 className="font-semibold">Phishing Verdict:</h3>
          <p>{result.verdict}</p>
        </div>
      ) : (
        <p>Loading...</p>
      )}
    </div>
  );
};

export default ResultDisplay;
