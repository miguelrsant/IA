export default function Home() {
  return (
    <div className="home">
      <div className="home-page">
        <div className="business">
          <img src="/bussine-engrenagem.png" alt="Engrenagem" />
          <p>Business Super Intelligence Platform</p>
        </div>
        <div className="texto-home">
          <h1 className="taylor-principal">TAYLOR</h1>
          <h1 className="taylor-secundario">Transforme dados em decisões estratégicas</h1>
          <p className="taylor-paragrafo">Plataforma avançada de automação operacional e análise inteligente com IA. Automatize rotinas, gere insights e acompanhe seu negócio em tempo real.</p>
        </div>
        <div className="btn-home"><p>Começar agora →</p></div>
      </div>
      <div className="vantagens">
        <div className="cards-home">
          <h1 className="cards-h1">99%</h1>
          <p className="cards-p">Redução do tempo</p>
        </div>
        <div className="cards-home">
          <h1 className="cards-h1">24/7</h1>
          <p className="cards-p">Análise automática</p>
        </div>
        <div className="cards-home">
          <h1 className="cards-h1">100%</h1>
          <p className="cards-p">Personalizável</p>
        </div>
      </div>
    </div>
  );
}
