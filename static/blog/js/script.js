const postsContainerElement = document.getElementById("posts");
const searchButtonElement = document.getElementById("searchButton");
const searchInputElement = document.getElementById("searchInput");
const searchResultElement = document.getElementById("searchResult");
const showAllPostsBtnElement = document.getElementById("showAll");

function createPostHTML(post) {
  return `
  <div class="post">
    <h1>${post.title}</h1>
    <span>Price: ${post.price}$</span>
    <span>Publisher: ${post.publisher}</span>
    <div class="aButtonContainer">
      <a href="http://127.0.0.1:8000/posts/${post.id}" class="aButton">Show Post</a>
      <a href="http://127.0.0.1:8000/posts/update/${post.id}" class="aButton">Update Post</a>
    </div>
  </div>
  `;
}

async function loadPosts() {
  try {
    const response = await fetch("http://127.0.0.1:8000/api/posts");
    const posts = await response.json();
    let result = "";
    searchResultElement.innerHTML = "";
    searchInputElement.value = "";
    for (const post of posts) {
      result += createPostHTML(post);
    }
    postsContainerElement.innerHTML = result;
  } catch (error) {
    console.error(error);
  }
}
async function searchPost() {
  try {
    const response = await fetch(
      `http://127.0.0.1:8000/api/posts/search?title=${encodeURIComponent(searchInputElement.value)}`,
    );
    const posts = await response.json();
    let result = "";

    if (posts) {
      const searchBarElement = document.createElement("i");
      searchBarElement.className = "fa-duotone fa-solid fa-magnifying-glass";

      const searchSpanElement = document.createElement("span");
      searchSpanElement.innerHTML = `The results for search term "${searchInputElement.value}"`;

      searchResultElement.innerHTML = "";
      searchResultElement.append(searchBarElement, searchSpanElement);
      for (const post of posts) {
        result += createPostHTML(post);
      }
    } else {
      searchResultElement.innerHTML = `Nothing found with search term '${searchInputElement.value}'`;
    }

    postsContainerElement.innerHTML = result;
  } catch (err) {
    console.error(err);
  }
}

document.addEventListener("DOMContentLoaded", loadPosts);

searchInputElement.addEventListener("keypress", function (event) {
  if (event.key == "Enter") {
    event.preventDefault();
    searchButtonElement.click();
  }
});
searchButtonElement.addEventListener("click", searchPost);
showAllPostsBtnElement.addEventListener("click", loadPosts);
