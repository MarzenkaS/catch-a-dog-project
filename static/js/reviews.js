const editReviewButtons = document.getElementsByClassName("btn-edit-review");
const reviewText = document.getElementsByClassName("id_content");
const reviewForm = document.getElementById("reviewForm");
const submitReviewButton = document.getElementById("submitButtonReview");

const deleteModalReview = new bootstrap.Modal(document.getElementById("deleteModalReview"));
const deleteReviewButtons = document.getElementsByClassName("btn-delete-review");
const deleteConfirmReview = document.getElementById("deleteConfirmReview");

/* Initializes edit functionality for the provided edit buttons */
for (let button of editReviewButtons) {
  button.addEventListener("click", (e) => {
    let reviewId = e.target.getAttribute("review_id");
    let reviewContent = document.getElementById(`review${reviewId}`).innerText;
    reviewText.value = reviewContent;
    submitButton.innerText = "Update";
    reviewForm.setAttribute("action", `edit_review/${reviewId}`);
  });
}


/* Initializes deletion functionality for the provided delete buttons */
for (let button of deleteReviewButtons) {
  button.addEventListener("click", (e) => {
    let reviewId = e.target.getAttribute("review_id");
    deleteConfirm.href = `delete_review/${reviewId}`;
    deleteModal.show();
  });
}
       
