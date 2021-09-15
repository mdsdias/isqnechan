<div id="preloader">
  <div class="jumper"></div>
  <div class="jumper"></div>
  <div class="jumper"></div>
</div>
<script>
  let midias = [
    {
      name: "Twitter",
      id: "@Isqneeh",
      url: "https://twitter.com/isqneeh",
    },
    {
      name: "Github",
      id: "Isqneeh",
      url: "https://github.com/isqneeh",
    },
    {
      name: "Discord",
      id: "Isqne#0719",
      url: "https://discord.com/users/783058100482867234",
    },
  ];
  let src = "https://avatars.githubusercontent.com/u/79223936?v=4";
</script>

<div class="slides flex-slider flex-container" align="middle">
  <h1 class="clearfix" align="center">Hello World, I am Isqne!</h1>
  <img alt="img" {src} class="avatar flexslider" />
  {#each midias as get}
    <div class="flex-container">
      <h2>{get.name}</h2>
      <h2><a href={get.url} target="_blank">{get.id}</a></h2>
    </div>
  {/each}
</div>
<style>
  .avatar {
    width: 200px;
    height: auto;
    border-radius: 50%;
  }
</style>
