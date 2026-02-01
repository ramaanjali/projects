let selectedItems = [];

function updateFavoriteFood(checkbox) {
    const favoriteFoodInput = document.getElementById("favorite-food");

    if (checkbox.checked) {
        if (selectedItems.length < 10) {
            selectedItems.push(checkbox.value);
        } else {
            checkbox.checked = false;
            alert("You can only select up to 10 items.");
        }
    } else {
        selectedItems = selectedItems.filter(item => item !== checkbox.value);
    }

    favoriteFoodInput.value = selectedItems.join(", ");
}