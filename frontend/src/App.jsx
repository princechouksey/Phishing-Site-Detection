import React from 'react';
import { Route, Routes } from 'react-router-dom';
import Home from './pages/Home';
import Results from './pages/Results';

function App() {
  return (
    <div className="min-h-screen bg-gray-100 flex items-center justify-center">
      <div className="container mx-auto">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/results" element={<Results />} />
        </Routes>
      </div>
    </div>
  );
}

export default App;
