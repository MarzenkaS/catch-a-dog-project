
const editButtonsComments = document.getElementsByClassName("editButtons");
const commentText = document.getElementsByClassName("commentText");
const commentForm = document.getElementById("commentForm");
const submitButtonComment = document.getElementById("submitButtonComment");

const deleteModalComment = new bootstrap.Modal(document.getElementById("deleteModalComment"));
const deleteCommentButtons = document.getElementsByClassName("deleteCommentButtons");
const deleteConfirmComment = document.getElementById("deleteConfirmComment");

/* Initializes edit functionality for the provided edit buttons */
for (let editButtonComment of editButtonsComments) {
  editButtonComment.addEventListener("click", (e) => {
    let commentId = e.target.getAttribute("comment_id");
    let commentContent = document.getElementById(`comment${commentId}`).textContent;
    commentText.value = commentContent;
    submitButtonComment.textContent = "Update";
    commentForm.setAttribute("action", `edit_comment/${commentId}`);
  });
}

/* Initializes deletion functionality for the provided delete buttons */
for (let deleteCommentButton of deleteCommentButtons) {
  deleteCommentButton.addEventListener("click", (e) => {
    let commentId = e.target.getAttribute("comment_id");
    deleteConfirmComment.href = `delete_comment/${commentId}`;
    deleteModalComment.show();
  });
}


// const editButtons = document.getElementsByClassName("btn-edit");
// const commentText = document.getElementById("id_body");
// const commentForm = document.getElementById("commentForm");
// const submitButton = document.getElementById("submitButton");

// /* Initializes edit functionality for the provided edit buttons */
// for (let editButton of editButtons) {
//   editButton.addEventListener("click", (e) => {
//     let commentId = e.target.getAttribute("comment_id");
//     let commentContent = document.getElementById(`comment${commentId}`).innerText;
//     commentText.value = commentContent;
//     submitButton.innerText = "Update";
//     commentForm.setAttribute("action", `edit_comment/${commentId}`);
//   });
// }


