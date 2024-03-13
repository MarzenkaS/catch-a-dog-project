const editButtons = document.getElementsByClassName("btn-edit");
const commentText = document.getElementById("id_body");
const commentForm = document.getElementById("commentForm");
const submitButton = document.getElementById("submitButton");

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

const likeButton = document.getElementByClassName("btn-like");

/* Initializes edit functionality for the provided edit buttons */
for (let button of editButtons) {
  button.addEventListener("click", (e) => {
    let commentId = e.target.getAttribute("comment_id");
    let commentContent = document.getElementById(`comment${commentId}`).innerText;
    commentText.value = commentContent;
    submitButton.innerText = "Update";
    commentForm.setAttribute("action", `edit_comment/${commentId}`);
  });
}

/* Initializes deletion functionality for the provided delete buttons */
for (let button of deleteButtons) {
  button.addEventListener("click", (e) => {
    let commentId = e.target.getAttribute("comment_id");
    deleteConfirm.href = `delete_comment/${commentId}`;
    deleteModal.show();
  });
}

/* Giving functionality to a like button */
function number_of_likes() {
    likeButton.addEventListener("click", (e) => {
        // Update the number of likes for the review
        let updatedLikesCount = review.likes.count();
        // Update the display of the number of likes on the button
        likeButton.innerText = Likes(updatedLikesCount);
    });
}

         
