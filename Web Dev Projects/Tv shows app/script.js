let data;
let val;
const addToFav = (id) => {
    console.log('hi', id);
    const item = data.filter((item) => item.show.id === id);
    const image = item[0].show.image?.medium || item[0].show.image?.original || 'picsum.photos/400';
    const favItem = `
    <div class="flex bg-white text-white flex-col space-y-2 bg-gray-900 w-fit text-white text-center pb-4 rounded shadow-xl">
      <div class="border-4 border-red-600 w-fit rounded-t">
        <img src=${image} class="h-80"></img>
      </div>
      <div class="text-xl font-extrabold">${item[0].show.name}</div>
      <div onclick="removeFromFavPage(${id})" class="hover:cursor-pointer">
        remove ❤️
      </div>
    </div>
    `;
    localStorage.setItem(id, favItem);
    addCards(val);
}

const removeFromFav = (id) => {
    localStorage.removeItem(id);
    addCards(val);
}

const removeFromFavPage = (id) => {
    localStorage.removeItem(id);
    location.reload();
}


const showDetails = (id) => {
    console.log('hi');
    document.getElementById('is-detail').classList.add('hidden');
    const isFav = localStorage.getItem(id) ? true : false;
    const item = data.filter((item) => item.show.id === id);
    const image = item[0].show.image?.medium || item[0].show.image?.original || 'picsum.photos/400';
    const details = `
    <div>
        <div class="container-main flex flex-col items-center justify-center mt-24">
          <div class="upper-box bg-red-700 h-40 rounded-t w-1/2"></div>
          <div class="lower bg-white w-1/2 flex flex-col justify-center items-center space-y-4 pb-4">
            <img
              src=${image}
              class='-mt-24 border-4 h-72 w-fit border-black'
            />
            <div class="text-black text-3xl font-extrabold  text-center">
            ${item[0].show.name}
            </div>
            <div class="flex flex-col">
                <button onclick="removeFromFav(${id})">
                  💔
                </button>
                <button onclick="addToFav(${id})">
                  add to fav ❤️
                </button>
            </div>
          </div>
        </div>
      </div>
    `;
    document.getElementById('detail').innerHTML = details;
}

const searchCard = (image, title, id) => {
    const isFav = localStorage.getItem(id) ? true : false;
    console.log(title, image);
    if (isFav) {
        return (`
        <div class="text-white bg-white flex flex-row justify-between space-x-10 w-auto py-3 bg-gray-900 rounded-md">
              <div class="px-4">
                <img src=${image} class="h-36" />
              </div>
              <div class="flex flex-col justify-around text-center">
                <div>${title}</div>
                <div class="">
                    <button onclick="showDetails(${id})"
                      class="border-2 border-white rounded-md px-24 bg-orange-500 hover:text-orange-500 hover:bg-white hover:border-orange-500">
                      Details 💪
                    </button>
                </div>
                <div>
                    <button onclick="removeFromFav(${id})" class="border-2 border-white rounded-md px-14 bg-red-500 hover:bg-white hover:text-red-500 hover:border-red-500"
                    >Remove from my Favourites 🖤
                    </button>
                </div>
              </div>
              <hr class="bg-white h-2"></hr>
            </div>
        `)
    }
    return (`
<div class="text-white bg-white flex flex-row justify-between space-x-10 w-auto py-3 bg-gray-900 rounded-md">
      <div class="px-4">
        <img src=${image} class="h-36" />
      </div>
      <div class="flex flex-col justify-around text-center">
        <div>${title}</div>
        <div class="">
            <button onclick="showDetails(${id})" class="border-2 border-white rounded-md px-24 bg-orange-500 hover:text-orange-500 hover:bg-white hover:border-orange-500">
              Details 💪
            </button>
        </div>
        <div>
            <button
            onclick="addToFav(${id})"
              class="border-2 border-white rounded-md px-14 bg-green-500 hover:bg-white hover:text-green-500 hover:border-green-500"
            >Add to my Favourites 🧡
            </button>
        </div>
      </div>
      <hr class="bg-white h-2"></hr>
    </div>
`)
};

const searchUrl = 'https://api.tvmaze.com/search/shows?q=';

const addCards = async (val) => {
    const res = await fetch(`${searchUrl}${val}`);
    data = await res.json();
    // console.log(data);
    const cardContainers = document.getElementById('cards');
    cardContainers.innerHTML = '';
    data.forEach(element => {
        console.log(element.show.id);
        const image = element.show.image?.medium || element.show.image?.original || 'picsum.photos/400';
        const title = element.show.name;
        const id = element.show.id;
        const card = searchCard(image, title, id);
        cardContainers.innerHTML += card;
    });
}

const mainSearch = document.getElementById('main-search');
mainSearch.addEventListener('input', (e) => {
    val = e.target.value;
    addCards(val);
})