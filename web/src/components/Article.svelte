<script>
  export let data;
  export let newsProvider;
</script>

<article class="Article relative rounded border shadow-md overflow-hidden">
  <a
    href={data.link_article}
    rel="external noopener noreferrer"
    target="_blank">
    <figure class="object-cover">
      <img class="w-full" src={data.link_image} alt={data.title} />
    </figure>
    <span
      class="absolute top-0 px-4 py-1 mt-4 bg-orange-400 bg-opacity-75
      text-white text-xs uppercase">
      {newsProvider}
    </span>
    <div class="p-4">
      <h2 class="text-base font-bold leading-snug tracking-tight">
        {data.title}
      </h2>
      <hr class="w-10 border-t-4 border-orange-400 my-4" />
      <p class="text-xs">{data.summary}</p>
    </div>
  </a>
</article>
