import React from 'react';
import { useEffect, useState } from 'react';
import './App.css';

function App() {
  const [date, setDate] = useState(null);
  useEffect(() => {
    async function getDate() {
      const res = await fetch('/api/date');
      const newDate = await res.text();
      setDate(newDate);
    }
    getDate();
  }, []);
  return (
    <main>
      <h2>Bem vindo ao IsqneSite!<h2>
      <br />
      <h2>Usando a API do .Go, a hora é:</h2>
      <p>{date ? date : 'Carregando a data...'}</p>
    </main>
  );
}

export default App;
