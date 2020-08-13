<script>
  import { goto } from "@sapper/app";
  import { user } from "../store/user";
  import { serverRequest } from "../utils/apiRequest";

  const logout = async () => {
    const { data } = await serverRequest("/server/logout", "POST");
    user.reset();
    await goto("/");
  };
</script>

<header class="container mx-auto">
  <nav class="flex justify-between h-16 items-center">
    <h1 class="text-xl font-bold text-gray-800">
      {#if $user.username}
        <a href="/feed">Newsfeed</a>
      {:else}
        <a href="/">Newsfeed</a>
      {/if}
    </h1>
    <ul class="flex">
      <li>
        {#if $user.username}
          <a
            href="/profile"
            rel="prefetch"
            class="font-thin text-gray-500 mr-4">
            {$user.username}
          </a>
        {:else}
          <a class="font-thin text-gray-500 mr-4" href="/signup" rel="prefetch">
            Register
          </a>
        {/if}
      </li>
      <li>
        {#if $user.username}
          <button
            on:click={logout}
            class="font-semibold text-orange-500 uppercase border
            border-orange-500 px-8 py-2 rounded-md hover:bg-orange-500
            hover:text-orange-100">
            Logout
          </button>
        {:else}
          <a
            class="font-semibold text-orange-500 uppercase border
            border-orange-500 px-8 py-2 rounded-md hover:bg-orange-500
            hover:text-orange-100"
            href="/login"
            rel="prefetch">
            Login
          </a>
        {/if}
      </li>
    </ul>
  </nav>
</header>
