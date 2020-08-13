<script>
  import Article from "../components/Article.svelte";
  import { apiRequest, apiError } from "../utils/apiRequest";

  let statusMessage;
  let statusError;

  const getNews = (newsName) => {
    try {
      const { data, status } = apiRequest(`/news?=news_name${newsName}`, "GET");
    } catch (error) {
      statusError = true;
      statusMessage = apiError(error);
    }
  };
</script>

<svelte:head>
  <title>Feed</title>
</svelte:head>

<div class="Feed App h-screen mx-auto grid grid-cols-12">
  <aside class="bg-gray-200 col-span-2">
    <div class="h-screen sticky top-0 px-8 py-16">
      <h3 class="font-bold uppercase">Feeds</h3>
      <ul class="leading-10">
        <li>
          <i class="fa fa-chevron-down mr-2" />
          <button>BBC</button>
        </li>
        <li>
          <i class="fa fa-chevron-down mr-2" />
          <button>New York Times</button>
        </li>
        <li>
          <i class="fa fa-chevron-down mr-2" />
          <button>El Universal</button>
        </li>
      </ul>
      <p class="mt-4">
        <button>Add a news provider</button>
      </p>
    </div>
  </aside>
  <main class="flex-grow col-span-9 p-16">
    <section class="flex relative border shadow px-8 py-4 mb-8 items-center">
      <svg
        class="text-gray-600 h-4 w-4 fill-current"
        xmlns="http://www.w3.org/2000/svg"
        xmlns:xlink="http://www.w3.org/1999/xlink"
        version="1.1"
        id="Capa_1"
        x="0px"
        y="0px"
        viewBox="0 0 56.966 56.966"
        style="enable-background: new 0 0 56.966 56.966;"
        xml:space="preserve"
        width="512px"
        height="512px">
        <path
          d="M55.146,51.887L41.588,37.786c3.486-4.144,5.396-9.358,5.396-14.786c0-12.682-10.318-23-23-23s-23,10.318-23,23
          s10.318,23,23,23c4.761,0,9.298-1.436,13.177-4.162l13.661,14.208c0.571,0.593,1.339,0.92,2.162,0.92
          c0.779,0,1.518-0.297,2.079-0.837C56.255,54.982,56.293,53.08,55.146,51.887z
          M23.984,6c9.374,0,17,7.626,17,17s-7.626,17-17,17
          s-17-7.626-17-17S14.61,6,23.984,6z" />
      </svg>
      <input
        class="h-10 px-5 pr-16 rounded-lg text-sm focus:outline-none w-full"
        type="search"
        name="search"
        placeholder="Search" />
    </section>
    <section class="grid grid-cols-2 lg:grid-cols-3 gap-6">
      <Article />
      <Article />
      <Article />
      <Article />
    </section>
  </main>
</div>
