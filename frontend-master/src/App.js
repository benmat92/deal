import React, { useEffect, useState } from 'react';
import './App.css';
import Deals from './components/Deals';
import DealLoadingComponent from './components/DealLoading';

function App() {
  const DealLoading = DealLoadingComponent(Deals);
  const [appState, setAppState] = useState({
    loading: false,
    deals: null,
  });
  useEffect(() => {
    setAppState({ loading: true });
    const apiUrl = 'http://127.0.0.1:8000/deals/';
    fetch(apiUrl)
      .then((data) => data.json())
      .then((deals) => {
        setAppState({ loading: false, deals: deals });
      });
  }, [setAppState]);
  return (
    <div className="App">
      <h1>Latest Deals</h1>
      <DealLoading isLoading={appState.loading} deals={appState.deals} />
    </div>
  );
}

export default App;
