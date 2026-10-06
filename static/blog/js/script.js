const postsContainerElement = document.getElementById("posts");

async function loadPosts() {
  try {
    const response = await fetch("http://127.0.0.1:8000/api/posts");
    const posts = await response.json();
    let result = "";
    for (const post of posts) {
      result += `
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
    postsContainerElement.innerHTML += result;
  } catch (error) {
    console.error(error);
  }
}

document.addEventListener("DOMContentLoaded", loadPosts);
