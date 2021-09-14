<script>
  let texts = true
  let projetos = [
  {
      "name":"Grabbertool",
      "desc":"Ferramenta para puxar dados de pessoas fisicas"
  },
  {
    "name":"BuscaPlacaAPI",
    "desc":"Uma API POST Simples usando a biblioteca Flask; A API não contem muitos dados mais breve pretendo trazer mais"
  }
  ]
  let range = 5
 function txts(event) {
    if (texts) {
      texts = false;
    } else {
      texts = true;
    }
  }
</script>

<button on:click={txts}>
  Projetos
</button>

<h1>Hello World, I am Isqne!</h1>
{#if texts}
  <h4>
    {#each projetos as get}
      <h2>Nome: {get.name}</h2>
      <h3>Descrição: {get.desc}</h3>
    {/each}
  </h4>
{/if}
