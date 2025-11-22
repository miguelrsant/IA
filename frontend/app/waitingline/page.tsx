export default function Page() { 
  return (
    <div className="waitingline">
      <h1 className="waiting-taylor">TAYLOR</h1>
      <p>
        Cadastre seu e-mail para receber novidades e atualizações da plataforma
        enquanto estamos em desenvolvimento.
      </p>
      <div className="cadastro-taylor">
        <form>
          <input type="text" name="name" placeholder="Joãozinho" required />
          <input
            type="email"
            name="email"
            placeholder="joãozinho@email.com"
            required
          />
          <button type="submit">Cadastrar</button>
        </form>
      </div>
    </div>
  );
}
