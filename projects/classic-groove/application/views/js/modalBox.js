// Album page

function openNewalbum() {
  let newAlbum = document.querySelector("#new-album");
  newAlbum.style.display = "block";
}
function openRestockalbum() {
  let restockAlbum = document.querySelector("#restock-album");
  restockAlbum.style.display = "block";
}

function closeEditalbum() {
  let editAlbum = document.querySelector("#edit-album");
  editAlbum.style.display = "none";
}

function closeDetailalbum() {
  let detailalbum = document.querySelector("#detail-album");
  detailalbum.style.display = "none";
}
function closeNewalbum() {
  let newAlbum = document.querySelector("#new-album");
  newAlbum.style.display = "none";
}
function closeRestockalbum() {
  let restockAlbum = document.querySelector("#restock-album");
  restockAlbum.style.display = "none";
}

// Order page

function closeEditorder() {
  let editOrder = document.querySelector("#edit-order");
  editOrder.style.display = "none";
}

function closeDetailorder() {
  let detailOrder = document.querySelector("#detail-order");
  detailOrder.style.display = "none";
}

// Account page

function openEditAccount() {
  let editAccount = document.querySelector("#edit-account");
  editAccount.style.display = "block";
}
function openDetailAccount() {
  let detailAccount = document.querySelector("#detail-account");
  detailAccount.style.display = "block";
}
function openNewAccount() {
  let newAccount = document.querySelector("#new-account");
  newAccount.style.display = "block";
}

function closeEditAccount() {
  let editAccount = document.querySelector("#edit-account");
  editAccount.style.display = "none";
}
function closeDetailAccount() {
  let detailAccount = document.querySelector("#detail-account");
  detailAccount.style.display = "none";
}
function closeNewAccount() {
  let newAccount = document.querySelector("#new-account");
  newAccount.style.display = "none";
}

// Distributor page

const openAddExistingSong = () => {
  document.querySelector("#add_exist_song").style.display = "block";
  updateSuggestions();
};
const closeAddExistingSong = () => {
  document.querySelector("#add_exist_song").style.display = "none";
};

const openAddAlbum = () => {
  document.querySelector("#add_exist_album").style.display = "block";
  updateSuggestionsAlbum();
};
const closeAddAlbum = () => {
  document.querySelector("#add_exist_album").style.display = "none";
};

const closeNewSupply = () => {
  document.querySelector("#new-supply").style.display = "none";
};
const closeDetailSupply = () => {
  document.querySelector("#detail-supply").style.display = "none";
};
