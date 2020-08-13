<script>
  import Browser from "../components/Browser.svelte";
  import { user } from "../store/user";
</script>

<aside class="Menu bg-gray-200 col-span-2">
  <div class="h-screen sticky top-0 px-8 py-16">
    <a class="font-bold uppercase" href="/profile" rel="prefetch">Profile</a>
    <br />
    <br />
    <h3 class="font-bold uppercase">Feeds</h3>
    <ul class="leading-10">
      {#each $user.news_sites as newsSite}
        <li>
          <i class="fa fa-chevron-down mr-2" />
          <a href={`feed/${newsSite}`} rel="prefetch">{newsSite}</a>
        </li>
      {:else}
        <p>No subscriptions</p>
      {/each}
    </ul>
    <p class="mt-4">
      <button
        class="font-semibold text-orange-500 border border-orange-500 px-8 py-1
        rounded-md hover:bg-orange-500 hover:text-orange-100">
        Add a news provider
      </button>
    </p>
  </div>
</aside>
