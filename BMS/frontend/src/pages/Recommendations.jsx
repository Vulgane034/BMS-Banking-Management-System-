import React, { useState } from 'react';
import axios from 'axios';

export default function Recommendations() {
  const [recs, setRecs] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const fetchRecommendations = async () => {
    setLoading(true);
    setError('');
    try {
      // Appel à l'API backend qui utilise Gemini CLI
      const res = await axios.get('/api/gemini-recommendation');
      setRecs(res.data.recommendations);
    } catch (err) {
      setError('Erreur lors de la récupération des recommandations IA.');
    }
    setLoading(false);
  };

  return (
    <div className="max-w-2xl mx-auto py-8">
      <h2 className="text-2xl font-bold mb-4 text-beac-secondary">Recommandations IA (Gemini)</h2>
      <button
        onClick={fetchRecommendations}
        className="bg-beac-primary text-white px-6 py-2 rounded hover:bg-beac-secondary transition mb-6"
        disabled={loading}
      >
        {loading ? 'Chargement...' : 'Générer les recommandations'}
      </button>
      {error && <div className="text-red-500 mb-4">{error}</div>}
      <ul className="space-y-4">
        {recs.map((rec, idx) => (
          <li key={idx} className="bg-beac-light p-4 rounded shadow dashboard-card">
            <span className="text-lg">💡</span> {rec}
          </li>
        ))}
      </ul>
    </div>
  );
}