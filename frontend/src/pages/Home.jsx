import React from 'react';
import URLInput from '../components/URLinput';

const Home = () => {
  return (
    <div className="max-w-md mx-auto p-4 bg-white rounded shadow-lg">
      <h2 className="text-xl font-bold mb-4">Phishing Site Detection</h2>
      <URLInput />
    </div>
  );
};

export default Home;
