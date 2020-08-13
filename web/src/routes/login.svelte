<script>
  import { goto } from "@sapper/app";
  import { serverRequest, apiError } from "../utils/apiRequest";
  import { user } from "../store/user";

  let email;
  let password;

  let statusMessage;

  const login = async () => {
    const body = { email, password };
    try {
      const { data } = await serverRequest("/server/login", "POST", body);
      user.update(data);
      await goto("/feed");
    } catch (error) {
      statusMessage = apiError(error);
    }
  };
</script>

<style>
  .errorLogin {
    font-size: 16px;
    color: brown;
  }
</style>

<svelte:head>
  <title>Login</title>
</svelte:head>

<div class="Login App h-screen mx-auto grid grid-cols-12">
  <aside
    class="hidden md:block md:col-span-4 bg-cover bg-center"
    style=" background-image:
    url(https://images.unsplash.com/photo-1593642532400-2682810df593?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80);
    " />
  <main class="flex col-span-12 md:col-span-8 items-center">
    <div class="mx-auto w-2/3 md:w-1/2 xl:max-w-md">
      <h1 class="text-2xl text-center font-bold">Sign in to Newsfeed</h1>
      <button
        class="w-full bg-blue-500 hover:bg-blue-700 text-white font-semibold
        py-3 px-4 rounded focus:outline-none focus:shadow-outline"
        type="button">
        Sign in with Google
      </button>
      <div class="relative text-center">
        <span
          class="absolute font-thin bg-white text-gray-500 px-4 -ml-6 -mt-2">
          Or
        </span>
        <hr class="my-10" />
      </div>
      <form action="">
        {#if statusMessage}
          <p class="errorLogin">{statusMessage}</p>
        {/if}
        <div class="mb-4">
          <label
            class="block text-gray-700 text-sm font-bold mb-2"
            for="email" />
          <input
            required
            class="h-12 shadow appearance-none border rounded w-full py-2 px-3
            text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            id="email"
            type="email"
            placeholder="Username or email"
            bind:value={email} />
        </div>

        <div class="mb-6">
          <label
            class="block text-gray-700 text-sm font-bold mb-2"
            for="password" />
          <input
            required
            class="h-12 shadow appearance-none border border-orange-400 rounded
            w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none
            focus:shadow-outline"
            id="password"
            type="password"
            placeholder="**********"
            bind:value={password} />
          <p class="text-blue-500 text-xs">
            <a class="text-orange-500" href="/get-password">
              Forgot your password?
            </a>
          </p>
        </div>

        <div class="mb-4">
          <p>
            Not a member?
            <a class="text-orange-500" href="/signup">Sign up</a>
          </p>
        </div>

        <div>
          <button
            class="w-1/2 text-center bg-orange-400 hover:bg-orange-700
            text-white font-bold py-3 px-4 rounded focus:outline-none
            focus:shadow-outline"
            type="button"
            on:click={login}>
            Sign in
          </button>
        </div>
      </form>
    </div>
  </main>
</div>
