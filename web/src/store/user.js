import { writable } from 'svelte/store';

const USER = {
  username: null,
  news_sites: ['new_york_times', 'bbc'],
};

function getUser() {
  const { subscribe, update, set } = writable(USER)

  return {
    subscribe,
    set: data => set({ ...data }),
    update: data => update(user => ({ ...user, ...data })),
    addNews: newsName => update(user => {
      if (user.news_sites.includes(newsName)) return user;
      else return user.news_sites.unshift(newsName);
    }),
    removeNews: newsName => user.update(user => {
      if (!user.news_sites.includes(newsName)) return user
      const index = user.news_sites.indexOf(newsName);
      return user.news_sites.slice(0, index);
    }),
    reset: () => set(USER),
  };
};

export const user = getUser();
