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

<div class="font-sans grid">
  <h1 class="text-4xl tracking-tighter font-light">
    Hello World, I am Isqne!
  </h1>
  <div class="flex-auto items-center">
    <div class="flex h-auto w-400">
      <img alt="img" {src} class="rounded-full" />
    </div>
    <div class="flex flex-col items-center">
      {#each midias as get}
        <h2 class="text-4xl tracking-tighter font-light">
          <a href={get.url} target="_blank">{get.name}</a>
        </h2>
      {/each}
    </div>
  </div>
</div>
