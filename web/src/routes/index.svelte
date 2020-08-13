<style>
  .Home {
    background-image: url(waves.svg);
  }
</style>

<svelte:head>
  <title>News Feed</title>
</svelte:head>

<div class="Home min-h-screen bg-contain bg-bottom bg-no-repeat">
  <div class="container xl:px-40 mt-24 mx-auto flex items-center">
    <section class="grid grid-cols-8 gap-4">
      <div class="col-span-3">
        <h2 class="font-semibold text-gray-900 text-6xl leading-none mb-6">
          Following news that matters
        </h2>
        <p class="font-thin text-gray-500 w-64 mb-6">
          Never miss the news that really matters to you, again.
        </p>
        <p>
          <a
            class="bg-orange-500 text-orange-100 px-12 py-4 rounded-md"
            href="/register">
            Get started for free
          </a>
        </p>
      </div>
      <div class="col-span-5">
        <img
          class="w-full"
          src="https://images.unsplash.com/photo-1499750310107-5fef28a66643?ixlib=rb-1.2.1&auto=format&fit=crop&w=600&h=338&q=80"
          alt="Newsfeed" />
      </div>
    </section>
  </div>
</div>
