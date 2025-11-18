"use client";

type BackendResponse = {
  data: any;
};

import { useEffect, useState } from "react";

export default function Page() {
  const [responseInfo, setResponseInfo] = useState<BackendResponse | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [isLoading, setIsLoading] = useState(true);
  useEffect(() => {
    fetch("http://localhost:8000/status/")
      .then(async (res) => {
        if (!res.ok) {
          throw new Error(`Erro na rede: ${res.status} ${res.statusText}`);
        }
        const body = await res.json();
        setResponseInfo({
          data: body,
        });
      })
      .catch((err) => {
        console.error("Falha no fetch:", err);
        setError(err.message);
      })
      .finally(() => {
        setIsLoading(false); 
      });
  }, []);


  if (isLoading) {
    return <div><h1>Carregando dados do backend...</h1></div>;
  }

  if (error) {
    return <div><h1>Erro ao buscar dados</h1><p>{error}</p></div>;
  }

  return (
    <div>
      <h1>Resposta do Backend</h1>
      <pre>{JSON.stringify(responseInfo, null, 2)}</pre>
    </div>
  );
}