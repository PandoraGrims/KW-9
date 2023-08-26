function getCookie(name) {
    var value = "; " + document.cookie;
    var parts = value.split("; " + name + "=");
    if (parts.length == 2) return parts.pop().split(";").shift();
}

let token = getCookie('bea35504a85e0c06e0f73f719d3c75906fe7ce99');

let likeButton = document.getElementById('like-button');

likeButton.addEventListener('click', async () => {
    let postId = likeButton.dataset.postId;
    let response = await fetch(`/api/posts/${postId}/like_users/`, {
        method: 'POST',
        headers: {
            'Authorization': `Token bea35504a85e0c06e0f73f719d3c75906fe7ce99`,
            'Content-Type': 'application/json',
        },
    });
    if (response.ok) {
        console.log('Лайкнул/Лайкнула');
    } else {
        console.error('Ошибка');
    }
});

let unlikeButton = document.getElementById('unlike-button');

unlikeButton.addEventListener('click', async () => {
    let likeId = unlikeButton.dataset.likeId;
    let response = await fetch(`/api/likes/${likeId}/`, {
        method: 'DELETE',
        headers: {
            'Authorization': `Token bea35504a85e0c06e0f73f719d3c75906fe7ce99`,
        },
    });
    if (response.ok) {
        console.log('Лайкнул/Лайкнула');
    } else {
        console.error('Ошибка');
    }
});