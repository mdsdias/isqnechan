<script>
  let midias = [
    {
      name: "Twitter",
      url: "https://twitter.com/Legumiih",
    },
    {
      name: "Github",
      url: "https://github.com/legumii",
    },
    {
      name: "Discord",
      url: "https://discord.com/users/783058100482867234",
    },
  ];
  let src = "https://avatars.githubusercontent.com/u/79223936?v=4";
</script>

<div class="font-sans flex grid">
  <h1 class="text-4xl tracking-tighter font-light" align="center">Hello World, I am Isqne!</h1>
  <div class="inline-flex items-center" align="middle">
    <img alt="img" {src} class="avatar" />
    {#each midias as get}
      <div class="midias">
        <h2><a href={get.url} class="font-semibold text-2xl" target="_blank">{get.name}</a></h2>
      </div>
    {/each}
  </div>
</div>

<style>
  .midias {
    display: inline-table;
    padding: 2rem;
  }

  .avatar {
    width: 200px;
    height: auto;
    border-radius: 50%;
  }
</style>
