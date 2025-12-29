import React from 'react';

export default function LandingPage() {
  return (
    <div className="min-h-screen flex flex-col bg-beac-light">
      {/* Header */}
      <header className="bg-beac-primary text-white py-6 shadow-md">
        <div className="container mx-auto flex items-center space-x-4 px-4">
          <img src="/bms-logo.svg" alt="BMS Logo" className="h-14" />
          <div>
            <h1 className="text-2xl font-bold">BMS</h1>
            <p className="text-sm text-beac-light">Banking Management System - BEAC</p>
          </div>
        </div>
      </header>
      {/* Main */}
      <main className="flex-1 flex flex-col items-center justify-center text-center px-4">
        <h2 className="text-3xl md:text-5xl font-bold text-beac-secondary mt-12 mb-4">Anticipez. Décidez. Protégez la stabilité monétaire.</h2>
        <p className="text-lg md:text-xl text-gray-700 mb-8 max-w-2xl">La plateforme intelligente de la BEAC pour la surveillance, la prévision et la gestion proactive des crises économiques et monétaires.</p>
        <div className="flex flex-col md:flex-row gap-4 mb-12">
          <a href="/dashboard" className="bg-beac-primary text-white px-8 py-3 rounded-lg font-semibold shadow hover:bg-beac-secondary transition">Accéder au Dashboard</a>
          <a href="#features" className="bg-white border border-beac-primary text-beac-primary px-8 py-3 rounded-lg font-semibold shadow hover:bg-beac-light transition">En savoir plus</a>
        </div>
        {/* Features */}
        <section id="features" className="mt-8 grid grid-cols-1 md:grid-cols-3 gap-8 max-w-5xl w-full">
          <div className="bg-white rounded-xl shadow p-6 flex flex-col items-center dashboard-card">
            <i className="fas fa-chart-line text-3xl text-beac-primary mb-3"></i>
            <h3 className="font-bold text-lg mb-2">Analyse Prédictive</h3>
            <p className="text-gray-600">Modèles IA avancés pour anticiper l’inflation, la croissance, les risques de crise…</p>
          </div>
          <div className="bg-white rounded-xl shadow p-6 flex flex-col items-center dashboard-card">
            <i className="fas fa-bell text-3xl text-red-500 mb-3"></i>
            <h3 className="font-bold text-lg mb-2">Alertes & Recommandations</h3>
            <p className="text-gray-600">Détection automatique des signaux faibles et recommandations de politiques optimales.</p>
          </div>
          <div className="bg-white rounded-xl shadow p-6 flex flex-col items-center dashboard-card">
            <i className="fas fa-users text-3xl text-beac-primary mb-3"></i>
            <h3 className="font-bold text-lg mb-2">Gouvernance Collaborative</h3>
            <p className="text-gray-600">Partage d’informations, suivi des réformes et collaboration entre institutions partenaires.</p>
          </div>
        </section>
      </main>
      {/* Footer */}
      <footer className="bg-beac-secondary text-white py-6 mt-12">
        <div className="container mx-auto flex flex-col md:flex-row justify-between items-center px-4">
          <div className="mb-4 md:mb-0 flex items-center space-x-2">
            <img src="/bms-logo.svg" alt="BMS Logo" className="h-10" />
            <span className="text-xs text-beac-light">Banking Management System - BEAC</span>
          </div>
          <div className="text-sm text-beac-light text-center md:text-right">
            <p>BMS - Plateforme Prédictive et Intelligente de Gestion des Crises Économiques et Monétaires</p>
            <p className="mt-1">© 2023 BEAC. Tous droits réservés.</p>
          </div>
        </div>
      </footer>
    </div>
  );
}