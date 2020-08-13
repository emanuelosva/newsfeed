<script context="module">
  export async function preload({ params, query }) {
    const newsName = params.slug;
    const url = `https://newsfeedapi.vercel.app/news?news_name=${newsName}`;
    const res = await this.fetch(url);
    const data = await res.json();
    return { newsList: data.data.info, newsName };
  }
</script>

<script>
  import Browser from "../../components/Browser.svelte";
  import Article from "../../components/Article.svelte";
  import Menu from "../../components/Menu.svelte";

  export let newsName;
  export let newsList;
</script>

<svelte:head>
  <title>Feed</title>
</svelte:head>

<div class="Feed App h-screen mx-auto grid grid-cols-12">
  <Menu />
  <main class="flex-grow col-span-9 p-16">
    <Browser />
    <section class="ArticleWrapper grid grid-cols-2 lg:grid-cols-3 gap-6">
      {#each newsList as _news}
        <Article data={_news} newsProvider={newsName} />
      {:else}
        <p>Loading...</p>
      {/each}
    </section>
  </main>
</div>
