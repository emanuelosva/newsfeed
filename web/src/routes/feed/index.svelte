<script>
  import Browser from "../../components/Browser.svelte";
  import ArticleWrapper from "../../components/Menu.svelte";
  import Menu from "../../components/Menu.svelte";
</script>

<svelte:head>
  <title>Feed</title>
</svelte:head>

<div class="Feed App h-screen mx-auto grid grid-cols-12">
  <Menu />
  <main class="flex-grow col-span-9 p-16">
    <Browser />
    <p
      class="font-semibold text-orange-500 border border-orange-500 px-8 py-1
      rounded-md hover:bg-orange-500 hover:text-orange-100">
      Get tne news!!! -- Choose one from your list
    </p>
  </main>
</div>
