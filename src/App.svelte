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

<div class="font-sans flex flex-col space-y-50 items-center">
  <h1 class="text-4xl tracking-tighter font-light">
    Hello World, I am Isqne!
  </h1>
  <div class="flex-auto items-center">
    <div class="flex h-600 w-600">
      <span
        class="animate-ping absolute inline-flex h-full w-full rounded-full bg-sky-400 opacity-75"
      />
      <span class="relative inline-flex bg-sky-500 w-500 h-500"
        ><img alt="img" {src} class="rounded-full" /></span
      >
    </div>
    <div class="flex flex-col">
      {#each midias as get}
        <h2 class="text-4xl tracking-tighter font-light bg-sky-500 w-auto">
          <a href={get.url} target="_blank">{get.name}</a>
        </h2>
      {/each}
    </div>
  </div>
</div>
