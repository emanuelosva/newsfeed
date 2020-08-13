<script>
  import { apiRequest } from "../utils/apiRequest";
  import { goto } from "@sapper/app";
  let username;
  let email;
  let password;

  let statusError;
  let statusMessage;

  const signup = async () => {
    try {
      const body = { username, email, password };
      const { data, status } = await apiRequest("/users/signup", "POST", body);
      await goto("/profile");
    } catch (error) {
      if (error.data) {
        statusError = error.response.status;
        statusMessage = error.data.message;
      } else {
        statusError = 500;
      }
    }
  };
</script>

<svelte:head>
  <title>Signup</title>
</svelte:head>

<div class="App h-screen mx-auto grid grid-cols-12">
  <aside
    class="hidden md:block md:col-span-4 bg-cover bg-center"
    style=" background-image:
    url(https://images.unsplash.com/photo-1593642532400-2682810df593?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80);
    " />
  <main class="flex col-span-12 md:col-span-8 items-center">
    <div class="mx-auto w-2/3 md:w-1/2 xl:max-w-md">
      <h1 class="text-2xl text-center font-bold">Sign up to Newsfeed</h1>
      <form action="">

        <div class="mb-4">
          <label
            class="block text-gray-700 text-sm font-bold mb-2"
            for="username" />
          <input
            class="h-12 shadow appearance-none border rounded w-full py-2 px-3
            text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            id="username"
            type="text"
            placeholder="Full name"
            bind:value={username} />
        </div>

        <div class="mb-4">
          <label
            class="block text-gray-700 text-sm font-bold mb-2"
            for="email" />
          <input
            class="h-12 shadow appearance-none border rounded w-full py-2 px-3
            text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            id="email"
            type="email"
            placeholder="email"
            bind:value={email} />
        </div>

        <div class="mb-6">
          <label
            class="block text-gray-700 text-sm font-bold mb-2"
            for="password" />
          <input
            class="h-12 shadow appearance-none border border-orange-400 rounded
            w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none
            focus:shadow-outline"
            id="password"
            type="password"
            placeholder="******************"
            bind:value={password} />
          <p class="text-blue-500 text-xs italic">Please choose a password.</p>
        </div>

        <div class="mx-auto block ">
          <button
            on:click={signup}
            class="w-full bg-orange-400 hover:bg-blue-700 text-white font-bold
            py-2 px-4 rounded focus:outline-none focus:shadow-outline"
            type="button">
            Create my Account
          </button>

          <div class="mt-4">
            <span class="inline">
              Existing user?
              <a class="text-orange-500" href="/login">Login</a>
            </span>
          </div>
        </div>
      </form>
    </div>
  </main>
</div>
