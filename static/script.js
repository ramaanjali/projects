const input = document.getElementById("movie");
const suggestionBox = document.getElementById("suggestions");

input.addEventListener("input", async () => {
    const query = input.value;
    if (query.length < 2) {
        suggestionBox.innerHTML = "";
        return;
    }

    const res = await fetch(`/suggest?q=${query}`);
    const data = await res.json();

    suggestionBox.innerHTML = "";
    data.forEach(movie => {
        const li = document.createElement("li");
        li.textContent = movie;
        li.onclick = () => {
            input.value = movie;
            suggestionBox.innerHTML = "";
        };
        suggestionBox.appendChild(li);
    });
});
