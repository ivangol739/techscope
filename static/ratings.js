document.addEventListener('DOMContentLoaded', () => {
    const ratingButtons = document.querySelectorAll('.rating-button');

    ratingButtons.forEach(button => {
        button.addEventListener('click', event => {
            event.preventDefault();
            const postId = parseInt(button.dataset.post);

            const formData = new FormData();
            formData.append('post_id', postId);

            fetch("/rating/", {
                method: "POST",
                headers: {
                    "X-CSRFToken": csrftoken,
                    "X-Requested-With": "XMLHttpRequest",
                },
                body: formData
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                if (data.error) {
                    alert(data.error);
                    return;
                }
                button.innerHTML = `<i class="bi bi-heart${data.action === 'added' ? '-fill' : ''}"></i> ${data.rating_sum}`;
                button.classList.toggle('btn-danger', data.action === 'added');
                button.classList.toggle('btn-outline-primary', data.action !== 'added');
            })
            .catch(error => {
                console.error('Error:', error);
                alert('Произошла ошибка при обработке лайка');
            });
        });
    });
});