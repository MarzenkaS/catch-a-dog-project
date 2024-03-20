const editButtons = document.getElementsByClassName("btn-edit");
const commentText = document.getElementByClassName("review");
const commentForm = document.getElementById("reviewForm");
const submitButton = document.getElementById("submitButton");

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

/* Initializes edit functionality for the provided edit buttons */
for (let button of editButtons) {
  button.addEventListener("click", (e) => {
    let review = e.target.getAttribute("review");
    let reviewContent = document.getElementById(`review${review}`).innerText;
    reviewText.value = reviewContent;
    submitButton.innerText = "Update";
    reviewForm.setAttribute("action", `edit_review/${review}`);
  });
}

/* Initializes deletion functionality for the provided delete buttons */
for (let button of deleteButtons) {
  button.addEventListener("click", (e) => {
    let review = e.target.getAttribute("review");
    deleteConfirm.href = `delete_review/${review}`;
    deleteModal.show();
  });
}
       
