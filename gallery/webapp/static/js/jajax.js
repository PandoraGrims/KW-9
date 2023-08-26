$(document).ready(function() {
    $(".add-favorite, .remove-favorite").on("click", function() {
        var button = $(this);
        var itemId = button.data("id");
        var action = button.hasClass("add-favorite") ? "add" : "remove";

        $.ajax({
            type: "POST",
            url: "/api/favorites/" + action + "/",
            data: { id: itemId },
            success: function(response) {
                if (response.success) {
                    if (action === "add") {
                        button.text("Удалить из избранного").removeClass("add-favorite").addClass("remove-favorite");
                    } else {
                        button.text("Добавить в избранное").removeClass("remove-favorite").addClass("add-favorite");
                    }
                }
            },
            error: function(error) {
                console.log("Ошибка:", error);
            }
        });
    });
});