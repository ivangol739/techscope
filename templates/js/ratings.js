const ratingButtons = document.querySelectorAll('.like-button');

ratingButtons.forEach(button => {
    button.addEventListener('click', event => {
        // Проверяем, не заблокирована ли кнопка
        if (!event.target.closest('.btn').classList.contains('disabled')) {
            // Получаем значение рейтинга и ID поста
            const value = 1; // Лайк
            const postId = parseInt(event.target.closest('.like-button').dataset.post);
            const ratingSum = button.querySelector('.rating-sum');
            const iconHeart = button.querySelector('i');

            const formData = new FormData();
            formData.append('post_id', postId);
            formData.append('value', value);

            fetch("/rating/", {
                method: "POST",
                headers: {
                    "X-CSRFToken": csrftoken,
                    "X-Requested-With": "XMLHttpRequest",
                },
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                if (data.error) {
                    alert(data.error); // Показать ошибку, если не авторизован
                } else {
                    // Обновляем счетчик лайков
                    ratingSum.textContent = data.rating_sum;

                    // Обновляем иконку сердечка (заполненное или пустое)
                    if (iconHeart.classList.contains('far')) {
                        iconHeart.classList.remove('far');
                        iconHeart.classList.add('fas');
                    } else {
                        iconHeart.classList.remove('fas');
                        iconHeart.classList.add('far');
                    }
                }
            })
            .catch(error => console.error(error));
        }
    });
});