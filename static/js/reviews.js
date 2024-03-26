const editBtnsReview = document.getElementsByClassName("editReviewButtons");
const reviewText = document.getElementsByClassName("reviewText");
const reviewForm = document.getElementById("reviewForm");
const submitButtonReview = document.getElementById("submitButtonReview");

const deleteModalReview = new bootstrap.Modal(document.getElementById("deleteModalReview"));
const deleteReviewButtons = document.getElementsByClassName("deleteReviewButtons");
const deleteConfirmReview = document.getElementById("deleteConfirmReview");

/* Initializes edit functionality for the provided edit buttons */
for (let editReviewButton of editBtnsReview) {
  editReviewButton.addEventListener("click", (e) => {
    let reviewId = e.target.getAttribute("review_id");
    let reviewContent = document.getElementById(`review${reviewId}`).textContent;
    console.log(reviewContent);
    console.log(reviewText);
    submitButtonReview.value = "Update";
    reviewForm.setAttribute("action", `edit_review/${reviewId}`);
  });
}

/* Initializes deletion functionality for the provided delete buttons */
for (let deleteReviewButton of deleteReviewButtons) {
  deleteReviewButton.addEventListener("click", (e) => {
    let reviewId = e.target.getAttribute("review_id");
    deleteConfirmReview.href = `delete_review/${reviewId}`;
    deleteModalReview.show();
  });
}