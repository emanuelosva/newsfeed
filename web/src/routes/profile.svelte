<script>
  import { user } from "../store/user";
  import { goto } from "@sapper/app";
  import { serverRequest, apiError } from "../utils/apiRequest";

  let name = user.username || "Stan Lee";
  let subscriptions = [
    { name: "El universal", key: "el_universal" },
    { name: "BBC", key: "bbc" },
    { name: "The New York Times", key: "new_york_times" },
  ];

  let statusMessage;

  const subscribe = async (name) => {
    try {
      const email = window.sessionStorage.getItem("email");
      const body = { email, news_name: name };
      const { data, status } = await serverRequest(
        "/server/subscribe",
        "POST",
        body
      );
      user.addNews(name);
      statusMessage = "Success - Go to your feed";
      await goto("/profile#subscriptions");
    } catch (error) {
      statusMessage = apiError(error);
    }
  };

  const unsubscribe = async (name) => {
    try {
      const email = window.sessionStorage.getItem("email");
      const body = { email, news_name: name };
      const { data, status } = await serverRequest(
        "/server/unsubscribe",
        "DELETE",
        body
      );
      user.removeNews(name);
      statusMessage = "Success - Unsubscribed";
      await goto("/profile#subscriptions");
    } catch (error) {
      statusMessage = apiError(error);
    }
  };
</script>

<svelte:head>
  <title>Profile</title>
</svelte:head>

<div class="Profile App h-screen mx-auto grid grid-cols-12">
  <aside class="bg-gray-200 col-span-2">
    <div class="h-screen sticky top-0 px-8 py-16">
      <h3 class="font-bold uppercase">News Providers</h3>
      <ul class="leading-10">
        <li>
          <i class="fa fa-chevron-down mr-2" />
          <a
            href="https://www.bbc.com/mundo"
            target="_blank"
            rel="noopener noreferrer">
            BBC
          </a>
        </li>
        <li>
          <i class="fa fa-chevron-down mr-2" />
          <a
            href="https://www.nytimes.com/es/"
            target="_blank"
            rel="noopener noreferrer">
            New York Times
          </a>

        </li>
        <li>
          <i class="fa fa-chevron-down mr-2" />
          <a
            href="https://www.eluniversal.com.mx/"
            target="_blank"
            rel="noopener noreferrer">
            El Universal
          </a>
        </li>
      </ul>
      <p class="mt-4">
        <a
          class="font-semibold text-orange-500 uppercase"
          href="/feed"
          rel="prefetch">
          Go to your feed
        </a>
      </p>
    </div>
  </aside>
  <main class="flex-grow col-span-9 p-16">
    <div>
      <section>
        <h3 class="font-semibold text-4xl">Manage account</h3>
        <div class="mb-5 text-center">
          <div
            class="mx-auto w-32 h-32 mb-2 border rounded-full relative
            bg-gray-100 mb-4 shadow-inset">
            <img
              id="image"
              class="object-cover w-full h-32 rounded-full"
              src="https://www.gravatar.com/avatar/e77a4e18cccdc0e7ecc6235afae39a5f?s=300"
              alt={name} />
          </div>
          <label
            for="fileInput"
            type="button"
            class="cursor-pointer inine-flex justify-between items-center
            focus:outline-none border py-2 px-4 rounded-lg shadow-sm text-left
            text-gray-600 bg-white hover:bg-gray-100 font-medium">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              class="inline-flex flex-shrink-0 w-6 h-6 -mt-1 mr-1"
              viewBox="0 0 24 24"
              stroke-width="2"
              stroke="currentColor"
              fill="none"
              stroke-linecap="round"
              stroke-linejoin="round">
              <rect x="0" y="0" width="24" height="24" stroke="none" />
              <path
                d="M5 7h1a2 2 0 0 0 2 -2a1 1 0 0 1 1 -1h6a1 1 0 0 1 1 1a2 2 0 0
                0 2 2h1a2 2 0 0 1 2 2v9a2 2 0 0 1 -2 2h-14a2 2 0 0 1 -2 -2v-9a2
                2 0 0 1 2 -2" />
              <circle cx="12" cy="13" r="3" />
            </svg>
            Browse Photo
          </label>
          <div class="mx-auto w-48 text-gray-500 text-xs text-center mt-1">
            Click to add profile picture
          </div>
          <input
            name="photo"
            id="fileInput"
            accept="image/*"
            class="hidden"
            type="file" />
        </div>
        <div class="mb-5">
          <label for="firstname" class="font-bold mb-1 text-gray-700 block">
            Your name
          </label>
          <input
            id="firstname"
            type="text"
            class="w-full px-4 py-3 rounded-lg shadow-sm focus:outline-none
            focus:shadow-outline text-gray-600 font-medium"
            bidn:value={$user.username} />
        </div>
        <div class="mb-5">
          <label for="lastname" class="font-bold mb-1 text-gray-700 block">
            Your last name
          </label>
          <input
            id="lastname"
            type="text"
            class="w-full px-4 py-3 rounded-lg shadow-sm focus:outline-none
            focus:shadow-outline text-gray-600 font-medium"
            value="Castro" />
        </div>
        <div class="mb-5">
          <label for="email" class="font-bold mb-1 text-gray-700 block">
            Email
          </label>
          <input
            type="email"
            class="w-full px-4 py-3 rounded-lg shadow-sm focus:outline-none
            focus:shadow-outline text-gray-600 font-medium"
            value="israel.castro@gmail.com" />
        </div>
      </section>
      <section>
        <div class="w-full">
          <h3 class="font-bold mb-1 text-gray-700 block">My suscriptions</h3>
          <p id="subscriptions">Get a new subscription</p>
          {#if statusMessage}
            <br />
            <p class="font-semibold text-orange-500">{statusMessage}</p>
          {/if}
          <br />
          {#each subscriptions as sub}
            {#if $user.news_sites.includes(sub.key)}
              <button
                on:click={() => unsubscribe(sub.key)}
                class="font-semibold text-orange-500 uppercase border block m-3
                border-orange-500 px-8 py-2 rounded-md hover:bg-orange-500
                hover:text-orange-100">
                {sub.name} -
                <span style="font-size: 10px;">Unsusbcribe</span>
              </button>
            {:else}
              <button
                on:click={() => subscribe(sub.key)}
                class="font-semibold text-orange-500 uppercase border block m-3
                border-green-500 px-8 py-2 rounded-md hover:bg-green-500
                hover:text-orange-100">
                {sub.name} -
                <span style="font-size: 10px;">Add subscription</span>
              </button>
            {/if}
          {/each}
        </div>
      </section>
    </div>
  </main>
</div>
