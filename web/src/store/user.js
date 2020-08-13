import { writable } from 'svelte/store';

const USER = {
  username: null,
  email: null,
  news_sites: [],
};

function getUser() {
  const { subscribe, update, set } = writable(USER)

  return {
    subscribe,
    set: data => set({ ...data }),
    update: data => update(user => ({ ...user, ...data })),
    addNews: newsName => update(user => ({
      ...user,
      news_sites: [...new Set(user.news_sites.concat(newsName))],
    })),
    removeNews: newsName => update(user => ({
      ...user,
      news_sites: [...user.news_sites.filter(n => n !== newsName)],
    })),
    reset: () => set(USER),
  };
};

export const user = getUser();
