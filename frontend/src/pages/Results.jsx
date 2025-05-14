import React, { useEffect, useState } from 'react';
import { useLocation } from 'react-router-dom';

const Results = () => {
  const location = useLocation();
  const [result, setResult] = useState(null);

  useEffect(() => {
    if (location.state?.result) {
      setResult(location.state.result);
    }
  }, [location]);

  return (
    <div className="min-h-screen bg-gray-100 flex items-center justify-center">
      <div className="max-w-2xl w-full p-6 bg-white rounded-xl shadow-md">
        <h2 className="text-2xl font-bold text-center mb-6 text-gray-800">🔍 Phishing Detection Result</h2>

        {result ? (
          <>
            <div className="mb-4">
              <h3 className="text-lg font-semibold text-gray-700">Website URL:</h3>
              <p className="text-blue-600 underline break-words">{result.metadata.url}</p>
            </div>

            <div className="mb-4">
              <h3 className="text-lg font-semibold text-gray-700">Phishing Verdict:</h3>
              <p className={`text-lg font-bold ${
                result.phishing_verdict.verdict === "Safe"
                  ? "text-green-600"
                  : "text-red-600"
              }`}>
                {result.phishing_verdict.verdict}
              </p>
            </div>

            <div className="mb-4">
              <h3 className="text-lg font-semibold text-gray-700">Phishing Score:</h3>
              <p className="text-gray-900">{result.phishing_verdict.phishing_score}</p>
            </div>

            <div>
              <h3 className="text-lg font-semibold text-gray-700">Explanation:</h3>
              <p className="text-gray-700">{result.phishing_verdict.explanation}</p>
            </div>
          </>
        ) : (
          <p className="text-gray-600">Loading results...</p>
        )}
      </div>
    </div>
  );
};

export default Results;
